Page serialization
==================

Page serialization matches our :ref:`page-structure`. Pages endpoints are always parameterized using an election day.


Cycle pages
-----------

Serializers
```````````

.. autoclass:: theshow.serializers.ElectionDaySerializer
  :members:


Viewsets
`````````

.. autoclass:: theshow.viewsets.ElectionDayList
  :members:

.. autoclass:: theshow.viewsets.ElectionDayDetail
  :members:


State pages
-----------

Serializers
```````````

.. autoclass:: theshow.serializers.StateListSerializer
  :members:

.. autoclass:: theshow.serializers.StateSerializer
  :members:

Viewsets
`````````

.. autoclass:: theshow.viewsets.StateMixin
  :members:

.. autoclass:: theshow.viewsets.StateList
  :members:

.. autoclass:: theshow.viewsets.StateDetail
  :members:

Body pages
----------

Serializers
```````````

.. autoclass:: theshow.serializers.BodyListSerializer
  :members:

.. autoclass:: theshow.serializers.BodySerializer
  :members:

Viewsets
`````````

.. autoclass:: theshow.viewsets.BodyMixin
  :members:

.. autoclass:: theshow.viewsets.BodyList
  :members:

.. autoclass:: theshow.viewsets.BodyDetail
  :members:

Office pages
------------

Serializers
```````````

.. autoclass:: theshow.serializers.OfficeListSerializer
  :members:

.. autoclass:: theshow.serializers.OfficeSerializer
  :members:

Viewsets
`````````

.. autoclass:: theshow.viewsets.OfficeMixin
  :members:

.. autoclass:: theshow.viewsets.OfficeList
  :members:

.. autoclass:: theshow.viewsets.OfficeDetail
  :members:
