#!/usr/bin/env python

"""
Project-wide application configuration.

DO NOT STORE SECRETS, PASSWORDS, ETC. IN THIS FILE.
They will be exposed to users. Use environment variables instead.
See get_secrets() below for a fast way to access them.
"""

import logging
import os

"""
NAMES
"""
# Project name to be used in urls
# Use dashes, not underscores!
PROJECT_SLUG = 'elections'

# Project name to be used in file paths
PROJECT_FILENAME = 'elections'

# The name of the repository containing the source
REPOSITORY_NAME = 'elections'
GITHUB_USERNAME = 'The-Politico'
REPOSITORY_URL = 'git@github.com:%s/%s.git' % (
    GITHUB_USERNAME, REPOSITORY_NAME
)

PRODUCTION_SERVERS = ['']
STAGING_SERVERS = ['18.221.240.252']

SERVER_USER = 'ubuntu'
SERVER_PYTHON = 'python3'
SERVER_PROJECT_PATH = '/home/%s/apps/%s' % (SERVER_USER, PROJECT_FILENAME)
SERVER_REPOSITORY_PATH = '%s/repository' % SERVER_PROJECT_PATH
SERVER_VIRTUALENV_PATH = '%s/virtualenv' % SERVER_PROJECT_PATH

UWSGI_SOCKET_PATH = '/run/uwsgi/%s.uwsgi.sock' % PROJECT_FILENAME

# Services are the server-side services we want to enable and configure.
# A three-tuple following this format:
# (service name, service deployment path, service config file extension)
SERVER_SERVICES = [
    ('app', '/etc/uwsgi/sites', 'ini'),
    ('uwsgi', '/etc/init', 'conf'),
    ('nginx', '/etc/nginx/sites-available', 'conf'),
    ('deploy', 'etc/init', 'conf')
]

# These variables will be set at runtime. See configure_targets() below
SERVERS = []
SERVER_BASE_URL = None
SERVER_LOG_PATH = None
DEBUG = True

"""
Logging
"""
LOG_FORMAT = '%(levelname)s:%(name)s:%(asctime)s: %(message)s'


"""
Utilities
"""


def get_secrets():
    """
    A method for accessing our secrets.
    """
    secrets_dict = {}

    for k, v in os.environ.items():
        if k.startswith(PROJECT_FILENAME):
            k = k[len(PROJECT_FILENAME) + 1:]
            secrets_dict[k] = v

    return secrets_dict


def configure_targets(deployment_target):
    """
    Configure deployment targets. Abstracted so this can be
    overriden for rendering before deployment.
    """
    global SERVERS
    global SERVER_BASE_URL
    global SERVER_LOG_PATH
    global DEBUG
    global DEPLOYMENT_TARGET
    global LOG_LEVEL
    global DAEMON_INTERVAL
    global ELEX_FLAGS
    global CURRENT_ELECTION

    secrets = get_secrets()

    if deployment_target == 'production':
        SERVERS = PRODUCTION_SERVERS
        SERVER_BASE_URL = 'http://%s/%s' % (SERVERS[0], PROJECT_SLUG)
        SERVER_LOG_PATH = '/var/log/%s' % PROJECT_FILENAME
        LOG_LEVEL = logging.WARNING
        DEBUG = False
        DAEMON_INTERVAL = 10
        ELEX_FLAGS = ['--national-only', '--test']
        CURRENT_ELECTION = '2017-11-07'
    elif deployment_target == 'staging':
        SERVERS = STAGING_SERVERS
        SERVER_BASE_URL = 'http://%s/%s' % (SERVERS[0], PROJECT_SLUG)
        SERVER_LOG_PATH = '/var/log/%s' % PROJECT_FILENAME
        LOG_LEVEL = logging.DEBUG
        DEBUG = True
        DAEMON_INTERVAL = 10
        ELEX_FLAGS = ['--national-only', '--test']
        CURRENT_ELECTION = '2017-11-07'
    else:
        SERVERS = []
        SERVER_BASE_URL = 'http://127.0.0.1:8001/%s' % PROJECT_SLUG
        SERVER_LOG_PATH = '/tmp'
        LOG_LEVEL = logging.DEBUG
        DEBUG = True
        DAEMON_INTERVAL = 10
        ELEX_FLAGS = ['--national-only', '--test']
        CURRENT_ELECTION = '2017-11-07'

    DEPLOYMENT_TARGET = deployment_target

"""
Run automated configuration
"""
DEPLOYMENT_TARGET = os.environ.get('DEPLOYMENT_TARGET', None)

configure_targets(DEPLOYMENT_TARGET)
