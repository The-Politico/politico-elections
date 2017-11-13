import { applyMiddleware, compose, createStore } from 'redux';
import thunkMiddleware from 'redux-thunk';
import reducers from '../reducers/';
import actions from '../actions/';
import refreshRates from '../constants/api';
import { COMPARE_RESULTS, COMPARE_CONTEXT } from '../constants/actions';

const store = createStore(reducers, compose(
  applyMiddleware(thunkMiddleware),
  window.devToolsExtension ? window.devToolsExtension() : f => f,
));

store.dispatch(actions.fetchInitialData());

/**
 * Set intervals to refresh context and results.
 * Fetched with a last modified timestamp.
 */
setInterval(() => {
  const { resultsModified } = store.getState().fetch;
  store.dispatch(actions.fetchResults(resultsModified));
}, refreshRates.results);

setInterval(() => {
  const { contextModified } = store.getState().fetch;
  store.dispatch(actions.fetchContext(contextModified));
}, refreshRates.context);


store.subscribe(() => {
  window.state = store.getState();
});


export default store;
