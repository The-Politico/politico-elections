import server_config

from fabric.api import local, settings, task
from fabric.state import env

# Other fabfiles
from . import daemon, data, servers

"""
Base configuration
"""
env.user = server_config.SERVER_USER
env.forward_agent = True

env.hosts = []


"""
Environments
Changing environment requires a full-stack test.
An environment points to both a server and an S3
bucket.
"""


@task
def production():
    """
    Run as though on production.
    """
    env.settings = 'production'
    server_config.configure_targets(env.settings)
    env.hosts = server_config.SERVERS


@task
def staging():
    """
    Run as though on staging.
    """
    env.settings = 'staging'
    server_config.configure_targets(env.settings)
    env.hosts = server_config.SERVERS

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
