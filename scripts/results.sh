#!/bin/bash

# grab elex results for everything
elex results 2016-11-08 --national-only -o json > master.json

# get the raceids we care about
races=`cat scripts/alabama-races.json`

# filter results
cat master.json \
| jq -c --argjson races "$races" '[
  .[] |
  select(.raceid as $id | $races|index($id)) |
  {
    fipscode: .fipscode,
    first: .first,
    last: .last,
    level: .level,
    officename: .officename,
    party: .party,
    polid: .polid,
    polnum: .polnum,
    precinctsreporting: .precinctsreporting,
    precinctsreportingpct: .precinctsreportingpct,
    precinctstotal: .precinctstotal,
    statepostal: .statepostal,
    votecount: .votecount,
    votepct: .votepct,
    winner: .winner
  }
]' # gzip and copy to s3 after this

# take master results and insert to django