Page views
==========

Page view are constructed to support both a live preview and a .


Export Inheritance
''''''''''''''''''

To swap out key script references on the server once we bake out pages, each view class generally has a child that inherits from it. For example, if there is a :code:`RacePage` view, there will also be a :code:`RacePageExport` view.

The child view uses a template that also inherits from the parent's template, but overrides any resources that will be baked out.

For example, a parent template may reference a script on the server like this:

.. code-block:: python

  class RacePage(ClassView):
    template = 'page.html'

.. code-block:: jinja

  <!-- page.html -->

  {%block foot%}
  <script src="{% static 'theshow/js/app.js'%}"></script>
  {%endblock%}

... while the export view's template would override that reference with the script's URL on AWS:

.. code-block:: python

  class RacePageExport(ClassView):
    template = 'page.export.html'

.. code-block:: jinja

  <!-- page.export.html -->

  {%block foot%}
  <script src="http://politico.com/election-results/cdn/{{election_day}}/js/app.js"></script>
  {%endblock%}


View classes
------------

.. toctree::
    :maxdepth: 2

    Cycle pages <views/cycles>
    State pages <views/states>
    Body pages <views/bodies>
    Race pages <views/races>
