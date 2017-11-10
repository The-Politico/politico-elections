Starting up
===========

Prerequisites
--------------
 - Have PostgreSQL installed and a local database called :code:`elections`
 - Have python3 installed
 - Have virtualenv installed
 - Have jq installed (:code:`brew install jq`)
 - Have :code:`topojson` and :code:`topojson-simplify` installed globally

Steps
-----

1. Clone this repo to a local directory
2. Start a virtualenv in the directory

  ::

    $ virtualenv -p python3 venv

3. Start the virtual environment and source any environment variables.

  ::

    $ source venv/bin/activate
    $ source .env


4. Bootstrap the database.

  ::

    $ fab data.bootstrap_db


5. Move to :code:`theshow/staticapp` directory and yarn install node dependencies.

  ::

    $ yarn

6. Run :code:`gulp` to start developing.

  ::

    $ gulp
