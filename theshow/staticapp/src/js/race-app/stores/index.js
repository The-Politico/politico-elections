import { applyMiddleware, compose, createStore } from 'redux';
import thunkMiddleware from 'redux-thunk';
import { cloneDeep, isEqual } from 'lodash';
import reducers from '../reducers/';
import actions from '../actions/';
import refreshRates from '../constants/api';
import { COMPARE_RESULTS, COMPARE_CONTEXT } from '../constants/actions';

const store = createStore(reducers, compose(
  applyMiddleware(thunkMiddleware),
  window.devToolsExtension ? window.devToolsExtension() : f => f,
));

store.dispatch(actions.fetchInitialData());

setInterval(() => {
  const { resultsModified } = store.getState().fetch;
  store.dispatch(actions.fetchResults(resultsModified));
}, refreshRates.results);

setInterval(() => {
  const { contextModified } = store.getState().fetch;
  store.dispatch(actions.fetchContext(contextModified));
}, refreshRates.context);


let compareResultsState = null;
let compareContextState = null;

function compareResults(state) {
  const datetime = new Date().toUTCString();
  const resultsState = cloneDeep(state.orm.Result.itemsById);
  if (!isEqual(compareResultsState, resultsState)) {
    compareResultsState = resultsState;
    store.dispatch(actions.setResultsModifiedTime(datetime));
    store.dispatch(actions.notifyNewResults());
  }
}

function compareContext(state) {
  const datetime = new Date().toUTCString();
  const contextState = cloneDeep(state);
  // Don't compare with results or fetch
  delete contextState.orm.Result;
  delete contextState.fetch;
  if (!isEqual(compareContextState, contextState)) {
    compareContextState = contextState;
    store.dispatch(actions.setContextModifiedTime(datetime));
  }
}

store.subscribe(() => {
  const state = store.getState();
  if (state.lastAction === COMPARE_RESULTS) compareResults(state);
  if (state.lastAction === COMPARE_CONTEXT) compareContext(state);
});


export default store;
