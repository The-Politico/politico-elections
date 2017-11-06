import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import Actions from '../actions/';
import TopResults from './TopResults';
import Chatter from './Chatter';
import SwingChartContainer from './SwingChartContainer';
import CensusMaps from './CensusMaps';
import ScatterPlots from './ScatterPlots';
import orm from '../../common/models';

const App = (props) => {
  const actions = bindActionCreators(Actions, props.dispatch);
  const hasVotes = checkResultStatus(props.db);

  const beforeVotesChatter = hasVotes ? null : (
    <div>
      <p>Check back soon!</p>
    </div>
  );

  const voteDependentModules = hasVotes ? (
    <div>
      <SwingChartContainer
          content={props.db.content}
          session={orm.session(props.db.orm)}
          actions={actions}
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
    ) : null;

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


function checkResultStatus(initDb) {
  const db = orm.session(initDb.orm);
  const election = db.Election.first();
  if (!election) return false;
  
  const state = [db.Division.withId(window.appConfig.statePostal)];
  const data = election.serializeResults(state);
  const results = data.divisions[window.appConfig.statePostal].results;
  const voteTotal = results.reduce((a, b) => a + b.voteCount, 0);
  return voteTotal > 0;

}


const mapStateToProps = state => ({
  db: state,
});

export default connect(mapStateToProps)(App);
