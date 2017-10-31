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
  $ python manage.py loaddata geography entity
  ```

7. Move to `theshow/staticapp` directory and yarn install node dependencies.

  ```
  $ yarn
  ```

8. Run `gulp` to start developing.

  ```
  $ gulp
  ```

### Loading fixtures

Presumes you have installed node libraries `topojson` and `topojson-simplify`, globally.

1. Run these management commands in sequence:

  ```bash
  $ python manage.py load_geography
  $ python manage.py load_jurisdictions
  $ python manage.py load_fed
  ```

2. Bootstrap races, elections and candidates from the AP:

  ```bash
  $ python manage.py bootstrap 2017-11-07
  ```


### Getting results data

Presumes you have `AP_API_KEY` exported as an environment variable.

First, bootstrap the results data for a particular election

```bash
$ python manage.py bootstrap 2017-11-07
```

Then, get all of the race ids for each file you need to create

```bash
$ python manage.py prepare_races 2017-11-07
```

Finally, run the daemon that will get results every ten seconds

```bash
$ fab staging daemons.deploy
```

### Creating census data

This app contains models and commands to create county-level census data files you can use in your dataviz.

Before you begin, make sure you have these environment variables set:

```
export AWS_S3_PUBLISH_BUCKET="com.politico.interactives.politico.com"
export AWS_ACCESS_KEY_ID="<YOUR ACCESS KEY>"
export AWS_SECRET_ACCESS_KEY="<YOUR SECRET ACCESS KEY>"
```

##### Steps

1. From the root of the `elections` project, startup the development server:

  ```
  $ python manage.py runserver
  ```

2. Login to the backend admin at `http://localhost:8000/admin`

3. Under Demographic, click to add a new Census Table.

4. Create the table you want using Census table and variable codes. (Use [Social Explorer](https://www.socialexplorer.com/explore/tables) to find the codes.) **Be sure to append an "E" to variable codes to get the census estimate, not the margin of error.** For example, `001E`.

5. Once you've created your table, you're ready to run the census command that will create your tables on the server. Specify states by FIPS codes to create county-level Census data files by state:

  ```
  $ python manage.py runserver 51 34
  ```
6. You can find your new data at a URL specified with this pattern:

  ```
  https://dy1ht16ivl5br.cloudfront.net/elections/data/us-census/{series code}/{table year}/{state fips}/{table code}.json
  ```

  For example:
  ```
  https://dy1ht16ivl5br.cloudfront.net/elections/data/us-census/acs5/2015/34/B03002.json
  ```


### Colors

Always use class names to target data-driven colors.

Our convention for color class names is:

```
.{palette}-{length}-{index}-{property}
```

- **palette**

    The name of the palette. For example, `gop` or `dem`.

- **length**

    If applicable, the length of the palette ramp. For example, `8` for an 8-color palette ramp.

- **index**

    If applicable, the index of the color within the palette ramp to use. For example, `1` for the first color in the palette ramp.

- **property**

  The property to target with the specified color. For example, `stroke` or `fill`. Concatenate multipart properties into camel-case, for example, `backgroundColor`.


Some example of fully specified color classes:

- `.gop-4-1-stroke`
- `.gop-fill`
- `.dem-backgroundColor`
