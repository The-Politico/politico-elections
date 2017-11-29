.. _page-structure:

Page structure
==============

Most of this project is organized around the structure of the pages it's built to produce.

We produce pages that aggregate elections for legislative bodies and states and individual pages of election results for executive offices, i.e., the president and state governors.

Here is a non-exhaustive sample of the pages we build for.

- **Home**

  - :code:`/election-results/2020/`

- **President**

  - :code:`/election-results/2020/president/`
  - :code:`/election-results/2020/president/texas/`

- **U.S. House and Senate**

  - :code:`/election-results/2020/senate/`
  - :code:`/election-results/2020/senate/texas/`
  - :code:`/election-results/2020/house/`
  - :code:`/election-results/2020/house/texas/`

- **State races**

  - :code:`/election-results/2020/texas/`
  - :code:`/election-results/2020/texas/governor/`
  - :code:`/election-results/2020/texas/senate/`
  - :code:`/election-results/2020/texas/house/`

- **Special elections**

  - :code:`/election-results/2017/alabama/special-election/dec-12/`

We can deconstruct those into page types that correspond to our models: **ElectionCycle**, **Office**, **Body** and **Division**.

- Election cycle page
- Federal executive office page (president)
- State federal executive office page (state results)
- Federal legislative body page (U.S. Senate or House)
- State federal legislative body page (state results)
- State page (all races)
- State executive office page (governor)
- State legislative body page (state house or senate)

See :ref:`models-election`.
