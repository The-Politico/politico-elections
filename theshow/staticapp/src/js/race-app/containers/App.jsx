import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import Actions from '../actions/';
import TopResults from './TopResults';
import Chatter from './Chatter';
import SwingChartContainer from './SwingChartContainer';
import CensusMaps from './CensusMaps';
import ScatterPlots from './ScatterPlots';
import TurnoutChart from './TurnoutTrend';
import orm from '../../common/models';

const App = (props) => {
  const actions = bindActionCreators(Actions, props.dispatch);
  const resultsStatus = checkResultStatus(props.db);

  const voteDependentModules = resultsStatus.aboveVotesTreshold ? (
    <div>
      <SwingChartContainer
        content={props.db.content}
        session={orm.session(props.db.orm)}
        actions={actions}
      />
      <TurnoutChart
        content={props.db.content}
        session={orm.session(props.db.orm)}
        actions={actions}
        hidden={!resultsStatus.aboveCompleteThreshold}
      />
      <ScatterPlots
        session={orm.session(props.db.orm)}
        actions={actions}
      />
      <CensusMaps
        session={orm.session(props.db.orm)}
        actions={actions}
      />
    </div>
  ) : (
    <div className="content-extra-large too-few-results">
      <p>Check back after polls close for results, maps and live analysis!</p>
    </div>
  );

  return (
    <div>
      <TopResults
        session={orm.session(props.db.orm)}
        actions={actions}
        fetch={props.db.fetch}
      />
      <Chatter
        content={props.db.content}
      />
      {voteDependentModules}
    </div>
  );
};


const checkResultStatus = (initDb) => {
  const db = orm.session(initDb.orm);
  const election = db.Election.first();
  if (!election) return false;

  const counties = db.Division
    .filter(d =>
      d.level === 'county' &&
      d.code.substr(0, 2) === window.appConfig.stateFips)
    .toModelArray();

  const results = election.serializeResults(counties);

  const votesThreshold = Math.floor(Object.keys(results.divisions).length / 10);
  const completeThreshold = votesThreshold;

  let countiesWithVotes = 0;
  let completeCounties = 0;

  Object.keys(results.divisions).forEach((division) => {
    const resultSet = results.divisions[division];
    const voteTotal = resultSet.results.reduce((a, b) => a + b.voteCount, 0);
    if (voteTotal > 0) countiesWithVotes += 1;
    if (resultSet.precinctsReportingPct === 1) completeCounties += 1;
  });

  return {
    countiesWithVotes,
    completeCounties,
    aboveVotesTreshold: countiesWithVotes >= votesThreshold,
    aboveCompleteThreshold: completeCounties >= completeThreshold,
  };
};


const mapStateToProps = state => ({
  db: state,
});

export default connect(mapStateToProps)(App);
