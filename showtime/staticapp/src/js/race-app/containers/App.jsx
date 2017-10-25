import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import Actions from '../actions/';
import TopResults from './TopResults';
import orm from '../models';

const App = (props) => {
  const actions = bindActionCreators(Actions, props.dispatch);
  return (
    <div>
      <TopResults
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
