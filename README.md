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
