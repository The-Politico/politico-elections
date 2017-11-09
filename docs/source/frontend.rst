The Front End
=============

Front-end applications are built in this repo using `generator-politico-django <https://github.com/The-Politico/generator-politico-django>`_.

Stack
-----

- `redux <https://redux.js.org/>`_
- `redux-orm <https://github.com/tommikaikkonen/redux-orm>`_
- `preact <https://preactjs.com/>`_

Models
------

To make our results as fast as possible, we prefer to do the bare minimum processing on raw AP API election night results. Instead, we let the client resolve the relationships between slim results and the context of any campaigns.

To make that matching reliable, we use front-end models to...
