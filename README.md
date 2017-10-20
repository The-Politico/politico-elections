![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# elections


### Loading fixtures

```bash
$ python manage.py loaddata geography entity election
```


### Seeding fixtures

Presumes you have installed node libraries `topojson` and `topojson-simplify`, globally.

Then run these management commands in sequence:

```bash
$ python manage.py load_geography
$ python manage.py load_jurisdictions
$ python manage.py load_fed
```

### Getting results data

Presumes you have `AP_API_KEY` exported as an environment variable.

First, bootstrap the results data for a particular election

```bash
$ python manage.py bootstrap 2016-11-08
```

Then, get all of the race ids for each file you need to create

```bash
$ python manage.py prepare_races 2016-11-08
```

Finally, run the daemon that will get results every ten seconds

```bash
$ fab staging daemons.deploy
```
