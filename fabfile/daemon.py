import json
import os
import server_config
import sys

from time import sleep, time
from fabric.api import execute, local, require, settings, task
from fabric.state import env


@task
def deploy(run_once=False):
    """
    Harvest data and deploy cards
    """
    require('settings', provided_by=['production', 'staging'])
    try:
        with settings(warn_only=True):
            main(run_once)
    except KeyboardInterrupt:
        sys.exit(0)


def main(run_once=False):
    """
    Main loop
    """
    results_start = 0

    while True:
        now = time()

        if (now - results_start) > server_config.DAEMON_INTERVAL:
            results_start = now
            process()

        if run_once:
            print('run once specified, exiting')
            sys.exit(0)

        sleep(1)


def process():
    if '--test' in server_config.ELEX_FLAGS:
        print('writing test files')
        test_path = '/tmp/ap-elex-recordings/{0}/national'.format(
            server_config.CURRENT_ELECTION
        )
        os.environ['ELEX_RECORDING_DIR'] = test_path

        if not os.path.exists(test_path):
            os.makedirs(test_path)

    if not os.path.exists('output'):
        os.makedirs('output')

    local('bash scripts/results.sh')

    if not os.path.exists('scripts/times_run.json'):
        with open('scripts/times_run.json', 'w') as writefile:
            json.dump({
                'times_run': 0
            }, writefile)

    with open('scripts/times_run.json') as readfile:
        data = json.load(readfile)
        data['times_run'] += 1
        print(data['times_run'])

    if data['times_run'] % 10 == 0:
        local('python manage.py update_results')

    with open('scripts/times_run.json', 'w') as writefile:
        json.dump(data, writefile)
