import data
import json
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

            local('python manage.py prepare_races 2016-11-08')
            local('bash scripts/results.sh')
                
            with open('scripts/times_run.json') as readfile:
                data = json.load(readfile)
                data['times_run'] += 1
                print(data['times_run'])

            if data['times_run'] % 10 == 0:
                local('python manage.py update_results')

            with open('scripts/times_run.json', 'w') as writefile:
                json.dump(data, writefile)
        
        if run_once:
            print('run once specified, exiting')
            sys.exit(0)

        sleep(1)