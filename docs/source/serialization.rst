.. _serialization:

Serialization
=============

Our front-end app is built to consume all the necessary context to interpret AP election results through JSON. We use Django REST to serialize our models to provide that context.

Each page we publish has a matching serialization endpoint. In preview we hit that endpoint directly. During publishing we bake out the endpoint as a ``context.json`` file that is published with the page alongside a ``results.json`` created by our daemonized results gathering process.

.. note::

  A second serialization step occurs on the front end when we marry context and results. That data is what is actually fed to our front-end components to display the state of any election. See :ref:`front-end-models`.

.. toctree::
   :maxdepth: 2

   Page serialization <serialization/page>
   Serializers <serialization/serializers>
