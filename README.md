![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# elections

## Starting up

##### Prereqs
 - Have PostgreSQL installed and a local database called `elections`
 - Have python3 installed
 - Have virtualenv installed
 - Have jq installed (`brew install jq`)
 - Have `topojson` and `topojson-simplify` installed globally

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

4. Bootstrap the database.

  ```
  $ fab data.bootstrap_db
  ```

5. Move to `theshow/staticapp` directory and yarn install node dependencies.

  ```
  $ yarn
  ```

6. Run `gulp` to start developing.

  ```
  $ gulp
  ```


## More

See the `docs` directory in this repo for more documentation.

- [Running election nights](docs/election-night.md)
- [Bootstrapping servers](docs/servers.md)
- [Baking geographic data](docs/geography.md)
- [Baking census data](docs/census.md)
- [Color palette information](docs/colors.md)