import React from 'react';

import ResultsBar from '../components/ResultsBar';
import ResultsMap from '../components/ResultsMap';
import FetchRefresh from '../components/FetchRefresh';

const TopResults = (props) => {
  const precinctsReportingPct = getPrecinctsReporting(props);

  return (
    <div className="top-results row-fluid section">
      <div className="content-extra-large">
        <div className="loading-bar">
          <FetchRefresh fetch={props.fetch} actions={props.actions} />
        </div>
        <div className="precincts-reporting-topline">
          <span>Precincts reporting: {(precinctsReportingPct * 100).toFixed(1)}%</span>
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

function getPrecinctsReporting(props) {
  const db = props.session;
  const stateResults = getStateResults(db);

  if (!stateResults) return 0;
  if (Object.keys(stateResults.divisions).length === 0) return 0;
  return stateResults.divisions[window.appConfig.statePostal].precinctsReportingPct;
}

export default TopResults;
