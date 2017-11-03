# Geography

### Creating geo data

Export topojson files with the `export_geography` command. Supply states by FIPS code.

```
$ python manage.py export_geography 34 51
```

JSON files are baked out to URLs with the following pattern:

`https://dy1ht16ivl5br.cloudfront.net/elections/data/geography/{year}/state/{state fips}/counties.json`

`year` is currently 2016.