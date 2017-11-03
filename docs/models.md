![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# The Models

### Basic definitions

An **ElectionCycle** comprises many **ElectionDays**.

An **ElectionDay** is a date on which one or many **Elections** can be held.

An **Election** is a specific contest in a **Race** -- a primary or general election (specified through an **ElectionType**).

A **Race** is run for an **Office** -- U.S. House District 3.

An **Office** is part of a legislative **Body**, unless an office is an executive office, i.e., the president and state governors.

A **Body** has a **Jurisdiction** -- the Federal Government for the U.S. Senate and House. (Executive offices are directly attached to a Jurisdiction -- the presidency is part of the Fed.)

A **Jurisdiction** is represented by a political geography called a **Division** -- the state of Texas.

**Divisions** have different **DivisionLevels** -- state or county -- and intersections -- counties and congressional districts.


**Candidates** are **Persons** engaged in a **Race**.

A **CandidateElection** is an abstraction that allows us to associate different types of votes -- e.g., popular and electoral college votes -- on the relationship between a **Candidate** and an **Election**.
