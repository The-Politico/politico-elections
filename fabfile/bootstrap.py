from fabric.api import local, require, settings, shell_env, task
from fabric.state import env


@task
def prepare_election_day(election_date):
    require('settings', provided_by=['production', 'staging', 'local'])

    with shell_env(DATABASE_URL=env.db):
        cmd = 'python manage.py bootstrap_election {0}'.format(election_date)
        if env.test:
            cmd = '{0} --test'.format(cmd)

        local(cmd)
        local('python manage.py bootstrap_results_elex {0}'.format(
            election_date
        ))
        local('python manage.py bootstrap_content {0}'.format(election_date))


@task
def restart(election_date):
    require('settings', provided_by=['production', 'staging', 'local'])

    if env.settings == 'production':
        print("You are attempting to wipe the production database. Don't.")
        return

    with shell_env(DATABASE_URL=env.db):
        local('dropdb elections')
        local('createdb elections')
        local('python manage.py migrate')
        local('python manage.py loaddata geography')
        local('python manage.py bootstrap_jurisdictions')
        local('python manage.py bootstrap_fed')
        local('python manage.py loaddata person')
        local('python manage.py loaddata personimage')
        local('python manage.py createsuperuser')

    prepare_election_day(election_date)


@task
def migrate_db():
    require('settings', provided_by=['production', 'staging', 'local'])

    with shell_env(DATABASE_URL=env.db):
        local('python manage.py migrate')


@task
def census(fips):
    require('settings', provided_by=['production', 'staging', 'local'])

    with shell_env(DATABASE_URL=env.db):
        local('python manage.py bootstrap_census {0}'.format(fips))


@task
def geography():
    require('settings', provided_by=['production', 'staging', 'local'])

    with shell_env(DATABASE_URL=env.db):
        local('python manage.py bootstrap_geography')
        local('python manage.py bootstrap_jurisdictions')
        local('python manage.py bootstrap_fed')
