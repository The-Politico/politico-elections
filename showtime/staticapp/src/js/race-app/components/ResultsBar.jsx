import React from 'react';

const ResultsBar = (props) => {
  const db = props.session;

  const election = db.Election.first();

  if (!election) return null;

  const state = db.Division
    .filter(d => d.level === 'state' && d.id === window.appConfig.stateFips)
    .toModelArray();

  const results = election.serializeResults(state)
  console.log(results);

  return (
    <div className="results-bar">
      <h3>😋 <purple>||||||||||||||</purple><green>-------</green> 😡</h3>
    </div>
  );
};

export default ResultsBar;
