import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import Actions from '../actions/';
import TopResults from './TopResults';
import SwingChartContainer from './SwingChartContainer';
import CensusMaps from './CensusMaps';
import ScatterPlots from './ScatterPlots';
import orm from '../../common/models';

const App = (props) => {
  const actions = bindActionCreators(Actions, props.dispatch);
  return (
    <div>
      <TopResults
        session={orm.session(props.db.orm)}
        actions={actions}
        fetch={props.db.fetch}
      />
      <SwingChartContainer
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
  );
};


const mapStateToProps = state => ({
  db: state,
});

export default connect(mapStateToProps)(App);
