#!/bin/bash

# grab elex results for everything
elex results 2016-11-08 --national-only -o json > master.json


for file in ./output/races/*.json ; do
  if [ -e "$file" ] ; then
    races=`cat $file`
    # filter results
    cat master.json \
    | jq -c --argjson races "$races" '[
      .[] |
      select(.raceid as $id | $races|index($id)) |
      {
        fipscode: .fipscode,
        level: .level,
        party: .party,
        polid: .polid,
        polnum: .polnum,
        precinctsreporting: .precinctsreporting,
        precinctsreportingpct: .precinctsreportingpct,
        precinctstotal: .precinctstotal,
        raceid: .raceid,
        statepostal: .statepostal,
        votecount: .votecount,
        votepct: .votepct,
        winner: .winner
      }
    ]' > $file # gzip and copy to s3 after this
  fi
done

# take master results and insert to django