import { applyMiddleware, compose, createStore } from 'redux';
import thunkMiddleware from 'redux-thunk';
import assign from 'lodash/assign';
import cloneDeep from 'lodash/cloneDeep';
import isEqual from 'lodash/isEqual';
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

/**
 * We want to compare results and context updates.
 * Whenever either change, update the last modified
 * timestamp and notify user new results were received.
 */
let previousResultsState = null;
let previousContextState = null;

function compareResults(state) {
  const datetime = new Date().toUTCString();
  const resultsState = state.orm.Result.itemsById;
  if (!isEqual(previousResultsState, resultsState)) {
    previousResultsState = resultsState;
    store.dispatch(actions.setResultsModifiedTime(datetime));
    store.dispatch(actions.notifyNewResults());
  }
}

function compareContext(state) {
  const datetime = new Date().toUTCString();
  const contextState = state;
  // Don't compare with results or fetch props
  delete contextState.orm.Result;
  delete contextState.fetch;
  if (!isEqual(previousContextState, contextState)) {
    previousContextState = contextState;
    store.dispatch(actions.setContextModifiedTime(datetime));
  }
}

/**
 * Subscribe to store changes, but we don't want to fire
 * expensive comparison operations unless we've just
 * finished loading new results or context.
 *
 * See actions/api.js for when we fire these compare actions.
 */
store.subscribe(() => {
  const state = store.getState();
  if (
    state.lastAction !== COMPARE_RESULTS &&
    state.lastAction !== COMPARE_CONTEXT
  ) return;

  const cloneState = cloneDeep(store.getState());
  if (state.lastAction === COMPARE_RESULTS) compareResults(cloneState);
  if (state.lastAction === COMPARE_CONTEXT) compareContext(cloneState);
});


export default store;
