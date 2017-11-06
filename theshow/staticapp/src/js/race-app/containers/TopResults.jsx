import React from 'react';

import ResultsBar from '../components/ResultsBar';
import ResultsMap from '../components/ResultsMap';
import FetchRefresh from '../components/FetchRefresh';

const TopResults = (props) => {
  const db = props.session;
  const stateResults = getStateResults(db);

  const precinctsReportingPct = stateResults ? stateResults.divisions[window.appConfig.statePostal].precinctsReportingPct : 0;

  return (
    <div className="top-results row-fluid section">
      <div className="content-extra-large">
        <div className="loading-bar">
          <FetchRefresh fetch={props.fetch} actions={props.actions} />
        </div>
        <div className="precincts-reporting-topline">
          <span>Precincts reporting: {precinctsReportingPct * 100}%</span>
        </div>
        <div className="bar">
          <ResultsBar session={props.session} />
        </div>
        <div className="map">
          <ResultsMap session={props.session} />
        </div>
        <div className="clear" />
      </div>
    </div>
  );
}

function getStateResults(db) {
  const election = db.Election.first();
  if (!election) return null;

  const state = db.Division
    .filter(d =>
      d.level === 'state' &&
      d.code === window.appConfig.stateFips)
    .toModelArray();

  return election.serializeResults(state);
}

export default TopResults;
