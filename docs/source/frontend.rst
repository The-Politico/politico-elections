The Front End
=============

Front-end applications are built in this repo using `generator-politico-django <https://github.com/The-Politico/generator-politico-django>`_ in ``theshow/staticapp``.

Stack
-----

- `redux <https://redux.js.org/>`_
- `redux-orm <https://github.com/tommikaikkonen/redux-orm>`_
- `preact <https://preactjs.com/>`_

.. _front-end-models:

Front-end Models
------

We let the client resolve the relationships between our slim results data and the context of any campaigns, passing only the keys needed to deserialize ``results.json`` and ``context.json``.

To ensure we're reliably setting and querying relationships between our data, we use a front-end ORM. We also centralize in model methods all the logic needed to resolve any overrides of AP data we set in the backend and pass clean data to all our front-end components.

Model files for the front-end are in ``theshow/staticapp/src/js/common/models/`` and include models for:

- Division
- Office
- Election
- Party
- Candidate
- AP election status
- AP results
- Override results from our backend

See `redux-orm <https://github.com/tommikaikkonen/redux-orm>`_ for details on interacting with models.

Each model contains a ``serialize()`` method except Election, which contains a ``serializeResults(divisions)`` method that serializes results for an election in the given division(s) and handles all AP overrides. Most dataviz components consume the serialized results returned from an Election model.

Static files
------------

JS, CSS and images are shared across page types. We bake them out to static paths we can reference absolutely in our baked pages suffixed with a random hash.

::

  /election-results/cdn/{election day}/{js|css|images}/{filename}-{hash}.{ext}

See :ref:`commands-bake-statics`.
