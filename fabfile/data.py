from fabric.api import local, task


@task
def bootstrap_db():
    local('dropdb elections')
    local('createdb elections')
    local('python manage.py migrate')
    local('python manage.py load_geography')
    local('python manage.py load_jurisdictions')
    local('python manage.py load_fed')
    local('python manage.py bootstrap 2017-11-07')
