import React from 'react';


/*
  serialize_election(election, [divisions]);

  returns {
    electionStatus: {
      precinctsReporting: 00,
      precinctsReportingPct: 0.00,
      precinctsTotal: 00,
      called: false,
      tabulated: false,
      overrideApCall: false,
      overrideApVotes: false,
    },
    results: [{
      candidate: {
        id: '',
        firstName: '',
        lastName: '',
        middleName: '',
        suffix: '',
        party: {
          code: '',
          label: '',
          shortLabel: '',
        },
        winner: False,
      },
      division: {
        fipsCode: '',
        label: '',
        shortLabel: '',
        postalCode: '',
      },
      voteCount: 00,
      votePct: 0.00,
    }],
  }

 */

const ResultsBar = (props) => {
  const db = props.session;

  const election = db.Election.first();

  if (!election) return null;

  const state = db.Division
    .filter(d => d.level === 'state' && d.id === window.appConfig.stateFips)
    .toModelArray()[0];

  console.log('state', state);

  election.candidates.all().toModelArray().forEach((d) => {
    const results = d.resultSet
      .filter(r => r.division === state.postalCode);
    console.log(results.toRefArray());
  });

  return (
    <div className="results-bar">
      <h3>😋 <purple>||||||||||||||</purple><green>-------</green> 😡</h3>
    </div>
  );
};

export default ResultsBar;
