Why this?
=========

Beginning with the 2018 election cycle, the POLITICO Interactives Team will be handling POLITICO's coverage of election results. Our plans include covering everything from statehouses to presidential elections. Thus, we needed a centralized, reusable system to collect, manage and publish election results. This system also needs to integrate with a larger campaign database managed by all of POLITICO.

Principles
----------

Election Results Done Quick
''''''''''''''''''''''''''''

A primary function of this rig is to publish election results from the AP Elections API. We want to do that as quickly and efficiently as possible, so this system gets as much data as possible before the election begins into our database. That includes candidates, parties, and geographical information. We bake all of this data out before the election begins.

Once we gather this information, all we have to do for results is gather data from the AP Elections API (using `elex <https://elex.readthedocs.io>`_, the best tool for working with AP election results), do minimal filtering in bash, and publish JSON to Amazon S3.

Relational election data
''''''''''''''''''''''''

This system contains a fully relational model for election data. We borrowed a lot of inspiration from the fine folks making OpenCivicData, but we also account for modeling vote totals. This model will end up becoming a part of a larger campaign database that will include FEC data and campaign staff information, so the highly relational model is important to us.

See :ref:`models`.


Modular data visualization
'''''''''''''''''''''''''''

The front-end code within this system does not handle any data visualization. Instead, we do all of that work in separate repos that we install as node modules and use across the application. That means we can use, for example, a county results map, on multiple types of pages with ease.

What's in it
------------

The backend
'''''''''''

- `Django`_ as the overarching backend framework
- `PostgreSQL`_ as the database of choice
- `Django REST Framework`_ to serialize our models to JSON
- `Elex`_ to process AP election results
- `Fabric`_ to handle server management and data processing

And lots more...

The frontend
''''''''''''

- `redux-orm` to take serialized JSON and build the relationships between live results and contextual data
- `Preact` to manage front-end views