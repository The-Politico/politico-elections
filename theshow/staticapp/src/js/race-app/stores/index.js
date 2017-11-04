import { applyMiddleware, compose, createStore } from 'redux';
import thunkMiddleware from 'redux-thunk';
import { assign } from 'lodash';
import reducers from '../reducers/';
import actions from '../actions/';

const store = createStore(reducers, compose(
  applyMiddleware(thunkMiddleware),
  window.devToolsExtension ? window.devToolsExtension() : f => f,
));

store.dispatch(actions.fetchInitialData());

setInterval(() => {
  console.log('It fetches results');
  store.dispatch(actions.fetchResults());
}, 5000);
//
// setInterval(() => {
//   console.log('It fetches context');
//   store.dispatch(actions.fetchContext());
// }, 10000);

store.subscribe(() => {
  window.store = assign({}, store.getState());
});

export default store;
