#!/bin/bash

# grab elex results for everything
elex results 2017-11-07 --national-only --test -o json > master.json

# cp output/elections/*.json output/results/

for file in ./output/elections/*.json ; do
  if [ -e "$file" ] ; then
    elections=`cat $file | jq '.elections'`
    levels=`cat $file | jq '.levels'`
    path=`cat $file | jq -r '.filename'`
    fullpath="output/results/$path"
    mkdir -p "$(dirname "$fullpath/p")"

    # filter results
    cat master.json \
    | jq -c --argjson elections "$elections" --argjson levels "$levels" '[
      .[] |
      select(.raceid as $id | $elections|index($id)) |
      select(.level as $level | $levels|index($level)) |
      {
        fipscode: .fipscode,
        level: .level,
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
    ]' > "$fullpath/data.json" # gzip and copy to s3 after this
    last_updated="{\"date\":\"`date`\"}"
    echo $last_updated > "$fullpath/last-updated.json"
  fi
done
