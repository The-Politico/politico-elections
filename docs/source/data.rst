Data structure
==============

Data to build pages is represented by two types: election **results** from the Associated Press and **context** that helps interpret and display those results.

Results
-------

To process our results as fast as possible, we do the bare minimum data manipulation on election night results from the AP API. The structure contains just the basic keys needed to marry results to the wider context provided by our app. This data is baked out as ``./results.json`` when publishing.

.. code-block:: javascript
  :caption: **results.json**

  {
    "fipscode": "51001",
    "level": "county",
    "polid": "63126",
    "polnum": "49283",
    "precinctsreporting": 17,
    "precinctsreportingpct": 1,
    "precinctstotal": 17,
    "raceid": "47225",
    "statepostal": "VA",
    "votecount": 4879,
    "votepct": 0.457306,
    "winner": true
  }

Context
-------

Context is provided by our app and includes all the information needed to display results on our election night pages. The data itself is created through a number of bootstrap procedures. See also :ref:`serialization`. This data is baked out as ``./context.json`` when publishing.

.. code-block:: javascript
  :caption: **context.json**

  {
  "uid": "<{Body|State|Office} UID>",
  "content": { /* ... */ },
  "elections": [
    {
      "uid": "<Election UID>",
      "date": "2017-11-07",
      "office": { /* ... */},
      "primary_party": null,
      "division": { /* ... */ },
      "candidates": [
        { /* ... */ },
        // ...
      ],
      "override_votes": false,
      "ap_election_id": "47225",
      "called": false,
      "tabulated": false,
      "override_ap_call": true,
      "override_ap_votes": false
    },
    // ...
  ],
  "parties": [
    { /* ... */ },
    // ...
  ],
  "division": {
    /* ... */
    "children": [
      { /* ... */ },
      // ...
    ]
  }
  }

Other data
----------

There are also supplemental data files we bake out. For example, GeoJSON created by :ref:`commands-export-geography` and county-level census data from :ref:`commands-run-census`.
