from fabric.api import local, task

import server_config


@task
def bootstrap_db():
    local('dropdb elections')
    local('createdb elections')
    local('python manage.py migrate')
    local('python manage.py loaddata geography')
    local('python manage.py load_jurisdictions')
    local('python manage.py load_fed')
    local('python manage.py loaddata person')
    local('python manage.py loaddata personimage')
    local('python manage.py loaddata demographic')
    local('python manage.py bootstrap {0}'.format(
        server_config.CURRENT_ELECTION
    ))
    local('python manage.py prepare_races {0}'.format(
        server_config.CURRENT_ELECTION
    ))
    local('python manage.py createsuperuser')


@task
def bootstrap_geodb():
    local('dropdb elections')
    local('createdb elections')
    local('python manage.py migrate')
    local('python manage.py load_geography')
    local('python manage.py load_jurisdictions')
    local('python manage.py load_fed')
    local('python manage.py loaddata demographic')
    local('python manage.py bootstrap {0}'.format(
        server_config.CURRENT_ELECTION
    ))
    local('python manage.py createsuperuser')


@task
def migrate_db():
    local('python manage.py migrate')
    local('python manage.py loaddata geography')
    local('python manage.py load_jurisdictions')
    local('python manage.py load_fed')
    local('python manage.py bootstrap {0}'.format(
        server_config.CURRENT_ELECTION
    ))
    local('python manage.py createsuperuser')


@task
def prepare_races():
    local('python manage.py prepare_races {0}'.format(
        server_config.CURRENT_ELECTION
    ))
