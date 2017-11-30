.. _page-structure:

Page structure
==============

Most of this project is organized around the structure of the pages it's built to produce.

We produce pages that aggregate elections for offices in legislative bodies, individual pages of election results for executive offices, i.e., the president and state governors, and pages that show all races in a particular state.

Here is a non-exhaustive sample of the pages we build for:

.. csv-table::
   :header: "Path", "Page type"
   :widths: 50, 60

   *Home*,
   :code:`/election-results/2020/`, "Homepage for a national general election"

   *President*
   :code:`/election-results/2020/president/`, "National presidential election results"
   :code:`/election-results/2020/president/texas/`, "State presidential election results"

   *U.S. House and Senate*
   :code:`/election-results/2020/senate/`, "U.S. Senate election results"
   :code:`/election-results/2020/senate/texas/`, "U.S. Senate election results in Texas"
   :code:`/election-results/2020/house/`, "U.S. House election results"
   :code:`/election-results/2020/house/texas/`, "U.S. House election results in Texas"

   *State races*
   :code:`/election-results/2020/texas/`, "All elections in Texas"
   :code:`/election-results/2020/texas/governor/`, "Texas governor"
   :code:`/election-results/2020/texas/senate/`, "Texas state senate"
   :code:`/election-results/2020/texas/house/`, "Texas state house"

   *Special elections*
   :code:`/election-results/2017/alabama/special-election/dec-12/`, "Special elections in Alabama on Dec. 12"



Page types correspond to our models: **ElectionCycle**, **Office**, **Body** and **Division**.

- Election cycle page
- Federal executive office page (president)
- State federal executive office page (state results)
- Federal legislative body page (U.S. Senate or House)
- State federal legislative body page (state results)
- State page (all races)
- State executive office page (governor)
- State legislative body page (state house or senate)

.. note::

  Special Elections are a bit of a special case that we host at the state level regardless of the office(s) contested.


See :ref:`models-election`.
