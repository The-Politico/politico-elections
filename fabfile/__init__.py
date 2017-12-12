import os
import server_config

from fabric.api import local, settings, task
from fabric.state import env

# Other fabfiles
from . import bake, bootstrap, daemon, data, servers

"""
Base configuration
"""
env.user = server_config.SERVER_USER
env.forward_agent = True

env.hosts = []
env.test = False


"""
Environments
Changing environment requires a full-stack test.
An environment points to both a server and an S3
bucket.
"""


@task
def test():
    env.test = True


@task
def production():
    """
    Run as though on production.
    """
    env.settings = 'production'
    server_config.configure_targets(env.settings)
    env.hosts = server_config.SERVERS
    env.db = os.environ.get('PRODUCTION_DATABASE_URL')
    env.bucket = os.environ.get('AWS_S3_PRODUCTION_BUCKET')


@task
def staging():
    """
    Run as though on staging.
    """
    env.settings = 'staging'
    server_config.configure_targets(env.settings)
    env.hosts = server_config.SERVERS
    env.db = os.environ.get('DATABASE_URL')
    env.bucket = os.environ.get('AWS_S3_STAGING_BUCKET')


@task
def local():
    env.settings = 'local'
    server_config.configure_targets(env.settings)
    env.db = os.environ.get('DATABASE_URL')
    env.bucket = None

"""
Branches

Changing branches requires deploying that branch to a host.
"""


@task
def stable():
    """
    Work on stable branch.
    """
    env.branch = 'stable'


@task
def master():
    """
    Work on development branch.
    """
    env.branch = 'master'


@task
def branch(branch_name):
    """
    Work on any specified branch.
    """
    env.branch = branch_name


@task
def deploy_server():
    servers.checkout_latest()
    servers.restart_service('uwsgi')
