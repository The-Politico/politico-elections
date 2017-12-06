Running results on election night
=================================

You can run our results deployment for an election night on either your local computer or on a server. This will walk through both.

Local computer
''''''''''''''

To run results on your local computer, first ensure you are connected to the correct database and have your AP API key. You can do this by putting the correct environment variables in your :code:`.env` file. The environment variables are:

::
  export AP_API_KEY="YOURAPIKEYHERE"
  export DATABASE_URL="postgresql://username:password@url:port/elections"


Next, check :code:`server_config.py` and ensure the correct global variables are set. These are set per deployment target (production, staging and local). For election nights, make sure they are correct for production. For testing, make sure they are correct for staging and local. 

You will want to pay special attention to the following:

- :code:`ELEX_FLAGS`: An array of the flags that elex will run. Consult the `elex docs <http://elex.readthedocs.io/en/stable/cli.html>`_.
- :code:`CURRENT_ELECTION`: The election date we care about

Finally, go into :code:`scripts/results.sh` and make sure the elex command matches the elex flags in your server config (we don't have a good way of matching these yet).


With these variables set, you can bootstrap the AP data. Do that by running :code:`fab data.prepare_races`.

.. warning::

  Do **not** run the Fabric command that would wipe the production database.

.. note::
    
  For special elections, you will need to go into your Django admin and set the Election :code:`special` boolean to :code:`True`. Then, run :code:`python manage.py bootstrap_results_elex <election-date (YYYY-MM-DD)>` and :code:`python manage.py bootstrap_content <election-date (YYYY-MM-DD)>`.

Context
~~~~~~~

For results pages, we bake out most things like candidate names, election labels and geography labels to the page in a JSON file for each page. You can bake out that information with the following management command:

::

  python manage.py bake_election <election-date (YYYY-MM-DD)>


If we are getting results for a new state, you will also need to bake out the geography for those pages. Consult the [geography docs](./geography.md) for how to do that.

Live Results
~~~~~~~~~~~~

You can publish live results from your personal computer. First, make sure you have your AP API key exported as an environment variable:

::

  


Also, make sure you are connected to the production database as demonstrated above and you have bootstrapped the current election date to the production database.

Then, you can run :code:`fab production daemon.deploy`. This will begin deploying live results to S3.

Once the race is over and AP has finished tabulating results, you can run :code:`python manage.py bootstrap_results_db (YYYY-MM-DD)` to update the database with the AP's tabulated results.

Replaying Tests
~~~~~~~~~~~~~~~

The results daemon process will record results automatically. Currently, they are recorded to :code:`/tmp/ap-elex-recordings/<election-date>/national/`. You can check that folder to ensure recording is working if you run `fab staging daemon.deploy` during a live AP test.

To replay a test, run `fab staging daemon.test`, which will loop through the files in this folder and serve them locally and to your deployment target.

Server
''''''

TKTK