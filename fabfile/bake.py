import json
import os
import sys

from fabric.api import local, settings, require, shell_env, task
from fabric.state import env
from glob import glob
from time import sleep, time


@task
def election(election_date):
    require('settings', provided_by=['production', 'staging', 'local'])

    cmd = 'python manage.py bake_election {0}'.format(election_date)
    if env.settings == 'production':
        cmd = '{0} --production'.format(cmd)

    with shell_env(DATABASE_URL=env.db):
        local(cmd)


@task
def context(election_date):
    require('settings', provided_by=['production', 'staging', 'local'])

    cmd = 'python manage.py bake_context {0}'.format(election_date)
    if env.settings == 'production':
        cmd = '{0} --production'.format(cmd)

    with shell_env(DATABASE_URL=env.db):
        local(cmd)


@task
def geography(fips):
    require('settings', provided_by=['production', 'staging', 'local'])

    cmd = 'python manage.py bake_geography {0}'.format(fips)
    if env.settings == 'production':
        cmd = '{0} --production'.format(cmd)

    with shell_env(DATABASE_URL=env.db):
        local(cmd)


@task
def results(election_date, run_once=False):
    require('settings', provided_by=['production', 'staging', 'local'])
    try:
        main(election_date, run_once)
    except KeyboardInterrupt:
        sys.exit(0)


def main(election_date, run_once=False):
    """
    Main loop
    """
    results_start = 0
    daemon_interval = 10

    while True:
        now = time()

        if (now - results_start) > daemon_interval:
            results_start = now
            fetch_results(election_date)

        if run_once:
            print('run once specified, exiting')
            sys.exit(0)

        sleep(1)


def fetch_results(election_date):
    if env.test:
        print('writing test files')
        test_path = '/tmp/ap-elex-recordings/{0}/national'.format(
            election_date
        )
        os.environ['ELEX_RECORDING'] = 'flat'
        os.environ['ELEX_RECORDING_DIR'] = test_path

        if not os.path.exists(test_path):
            os.makedirs(test_path)

    if not os.path.exists('output'):
        os.makedirs('output')

    cmd = 'bash scripts/results.sh -d {0}'.format(election_date)

    if env.settings in ['production', 'staging']:
        cmd = '{0} -t {1}'.format(cmd, env.bucket)

    if env.test:
        cmd = '{0} -s "--test"'

    local(cmd)
