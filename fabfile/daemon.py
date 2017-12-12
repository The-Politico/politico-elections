import json
import os
import sys
from glob import glob
from time import sleep, time

from fabric.api import execute, local, require, settings, task
from fabric.state import env

import server_config

DAEMON_INTERVAL = 10


@task
def deploy(run_once=False):
    """
    Gets results data and deploys to s3
    """
    require('settings', provided_by=['production', 'staging', 'local'])
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

        if (now - results_start) > DAEMON_INTERVAL:
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
        os.environ['ELEX_RECORDING'] = 'flat'
        os.environ['ELEX_RECORDING_DIR'] = test_path

        if not os.path.exists(test_path):
            os.makedirs(test_path)

    if not os.path.exists('output'):
        os.makedirs('output')

    local('bash scripts/results.sh -t {0} -d {1}'.format(
        server_config.S3_BUCKET, server_config.CURRENT_ELECTION
    ))


def begin_test(run_once=False):
    """
    Main loop
    """
    results_start = 0
    i = 1
    while True:
        now = time()

        if (now - results_start) > DAEMON_INTERVAL:
            results_start = now
            test_dir = '/tmp/ap-elex-recordings/{0}/national'.format(
                server_config.CURRENT_ELECTION
            )
            cmd = 'ls {} | sort -t \- -k 2,2 | head -n {} | tail -n 1'.format(
                test_dir, i
            )
            file = '{0}/{1}'.format(test_dir, local(cmd, capture=True))
            print(file, i)
            local('bash scripts/results.sh -f {0} -t {1} -d {2}'.format(
                file, server_config.S3_BUCKET, server_config.CURRENT_ELECTION
            ))
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
