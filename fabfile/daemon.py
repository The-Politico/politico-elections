import json
import os
import server_config
import sys

from fabric.api import execute, local, require, settings, task
from fabric.state import env
from glob import glob
from time import sleep, time


@task
def deploy(run_once=False):
    """
    Gets results data and deploys to s3
    """
    require('settings', provided_by=['production', 'staging'])
    try:
        with settings(warn_only=True):
            main(run_once)
    except KeyboardInterrupt:
        sys.exit(0)


@task
def test(run_once=False):
    """
    Loops through test data and moves to static folder for local testing
    """
    try:
        with settings(warn_only=True):
            begin_test(run_once)
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
            fetch_results()

        if run_once:
            print('run once specified, exiting')
            sys.exit(0)

        sleep(1)


def fetch_results():
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


def begin_test(run_once=False):
    """
    Main loop
    """
    results_start = 0
    i = 1
    while True:
        now = time()

        if (now - results_start) > server_config.DAEMON_INTERVAL:
            results_start = now
            test_dir = '/tmp/ap-elex-recordings/{0}/national'.format(
                server_config.CURRENT_ELECTION
            )
            cmd = 'ls {} | sort -t \- -k 2,2 | head -n {} | tail -n 1'.format(
                test_dir, i
            )
            file = '{0}/{1}'.format(test_dir, local(cmd, capture=True))
            print(file, i)
            local('bash scripts/results.sh {0}'.format(file))
            i += 10

        if run_once:
            print('run once specified, exiting')
            sys.exit(0)

        sleep(1)


def move_test_file():
    test_dir = '/tmp/ap-elex-recordings/{0}/national'.format(
        server_config.CURRENT_ELECTION
    )

    top_file = local('ls {0} | sort -t _ -k 2,2 | head -n -1').format(
        test_dir
    )

    local('mv {0}/{1} master.json').format(test_dir, top_file)
    fabric.env('current_test_file', )

    print(fabric.env('current_test_file'))
