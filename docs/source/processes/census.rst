Preparing Census data
=====================

Creating census data
--------------------

This app contains models and commands to create county-level census data files you can use in your dataviz.

Before you begin, make sure you have these environment variables set:

::

  export AWS_S3_PUBLISH_BUCKET="com.politico.interactives.politico.com"
  export AWS_ACCESS_KEY_ID="<YOUR ACCESS KEY>"
  export AWS_SECRET_ACCESS_KEY="<YOUR SECRET ACCESS KEY>"

Steps
-----

1. From the root of the `elections` project, startup the development server:

  ::

    $ python manage.py runserver

2. Login to the backend admin at ``http://localhost:8000/admin``

3. Under Demographic, click to add a new Census Table.

4. Create the table you want using Census table and variable codes. (Use `Social Explorer <https://www.socialexplorer.com/explore/tables>`_ to find the codes.) **Be sure to append an "E" to variable codes to get the census estimate, not the margin of error.** For example, `001E`.

5. Once you've created your table, you're ready to run the census command that will create your tables on the server. Specify states by FIPS codes to create county-level Census data files by state:

  ::

    $ python manage.py runserver 51 34

6. You can find your new data at a URL specified with this pattern:

  ::

    https://www.politico.com/interactives/elections/data/us-census/{series code}/{table year}/{state fips}/{table code}.json

  For example https://www.politico.com/interactives/elections/data/us-census/acs5/2015/34/B03002.json


Current tables used in modules
------------------------------

- ``B03002`` - Hispanic or Latino Origin by Race
- ``B19001`` - Household Income in the Past 12 months
- ``B17020`` - Poverty Status in the Past 12 Months By Age
- ``B15003`` - Education Attainment for the Population 25 years and Over
