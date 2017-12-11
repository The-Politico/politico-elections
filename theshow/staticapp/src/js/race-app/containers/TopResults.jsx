import React from 'react';

import ResultsBar from '../components/ResultsBar';
import ResultsMap from '../components/ResultsMap';
import FetchRefresh from '../components/FetchRefresh';

const TopResults = (props) => {
  const status = getStatus(props);
  const doneWithResults = status.tabulated || status.precinctsReportingPct === 1;

  return (
    <div className="top-results row-fluid section">
      <div className="content-extra-large">
        <div className="loading-bar">
          <FetchRefresh fetch={props.fetch} actions={props.actions} hidden={doneWithResults} />
        </div>
        <div className="precincts-reporting-topline" hidden={doneWithResults}>
          <span>Precincts reporting: {(status.precinctsReportingPct * 100).toFixed(1)}%</span>
        </div>
        <div className="bar">
          <ResultsBar session={props.session} />
          <div className="precincts-reporting-topline" hidden={!doneWithResults}>
            <span>Precincts reporting: {(status.precinctsReportingPct * 100).toFixed(1)}%</span>
          </div>
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

function getStatus(props) {
  const db = props.session;
  const stateResults = getStateResults(db);

  if (!stateResults) return { precinctsReportingPct: 0, tabulated: false };
  if (Object.keys(stateResults.divisions).length === 0) return { precinctsReportingPct: 0, tabulated: false };
  return {
    precinctsReportingPct: stateResults.divisions[window.appConfig.statePostal].precinctsReportingPct,
    tabulated: stateResults.status.tabulated
  };
}

export default TopResults;
