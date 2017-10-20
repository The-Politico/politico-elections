![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# elections


## Developing



### Starting up

##### Prereqs
 - Have PostgreSQL installed and a local database called `elections`
 - Have python3 installed
 - Have virtualenv installed

##### Steps

1. Clone this repo to a local directory
2. Start a virtualenv in the directory

  ```
  $ virtualenv -p python3 venv
  ```

3. Start the virtual environment

  ```
  $ source venv/bin/activate
  ```

4. Run initial migrations to create table.

  ```
  $ python manage.py migrate
  ```

5. Create a superuser

  ```
  $ python manage.py createsuperuser
  ```

6. Load sample data into the database:

  ```
  $ python manage.py loaddata geography entity election
  ```

7. Move to `showtime/staticapp` directory and yarn install node dependencies.

  ```
  $ yarn
  ```

8. Run `gulp` to start developing.

  ```
  $ gulp
  ```


### Seeding fixtures

Presumes you have installed node libraries `topojson` and `topojson-simplify`, globally.

Then run these management commands in sequence:

```bash
$ python manage.py load_geography
$ python manage.py load_jurisdictions
$ python manage.py load_fed
```
