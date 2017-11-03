# Running results on an election night

You can run our results deployment for an election night on either your local computer or on a server. This will walk through both.

## Local computer

To run results on your local computer, first ensure you are connected to the production database. You can do this by putting the correct postgres environment variables in your `.env` file. The environment variables are:

```
export ELECTIONS_POSTGRES_NAME="name_of_production_db"
export ELECTIONS_POSTGRES_USER="production_user"
export ELECTIONS_POSTGRES_PASSWORD="production_password"
export ELECTIONS_POSTGRES_HOST="production_host"
export ELECTIONS_POSTGRES_PORT="production_port"
```

Once you are connected to the production database, you can bootstrap the AP data. Do that by running `python manage.py bootstrap <election-date>`. Do _not_ run the Fabric command that would wipe the production database.

### Context

For results pages, we bake out most things like candidate names, election labels and geography labels to the page in a JSON file for each page. You can bake out that information with the following management command:

```
python manage.py bake_context <election-date (YYYY-MM-DD)>
```

If we are getting results for a new state, you will also need to bake out the geography for those pages. Consult the [geography docs](./geography.md) for how to do that.

### Live Results    

You can publish live results from your personal computer. First, make sure you have your AP API key exported as an environment variable:

```
export AP_API_KEY="YOURAPIKEYHERE"
```

Also, make sure you are connected to the production database as demonstrated above and you have bootstrapped the current election date to the production database.

Then, run `python manage.py prepare_races <election-date (YYYY-MM-DD)>`. You should see files created in `output/elections` after this. 

Once you have those files, you can run `fab production daemons.deploy`. This will begin deploying live results every 10 seconds to S3.

>TK: How to bootstrap the results pages themselves. This is not written yet.

Once the race is over and AP has finished tabulating results, you can run `python manage.py update_results (YYYY-MM-DD)` to update the database with the AP's tabulated results.

## Server

Assuming we have a production server stood up (if not, consult the [server docs](./servers.md)), then you can run some Fabric commands to achieve the same as above (NOTE: TYLER NEEDS TO WRITE THESE FABRIC COMMANDS).

Make sure that, in `server_config.py`, `CURRENT_ELECTION` is set to the election you want to operate on for the `production` deployment target.

They will be something like:

1. `fab production master servers.fabcast:data.bootstrap_elections`
2. `fab production master servers.fabcast:data.prepare_elections`
3. `fab production master servers.start_service:deploy`

This will get the AP data bootstrapped in the production database and start the deploy daemon on the server. To see the output of the deploy daemon, you can ssh onto the server and run `sudo tail -f /var/log/elections/deploy.log`.