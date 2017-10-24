import { applyMiddleware, compose, createStore } from 'redux';
import thunkMiddleware from 'redux-thunk';
import _ from 'lodash';
import reducers from '../reducers/';
import actions from '../actions/';

const store = createStore(reducers, compose(
  applyMiddleware(thunkMiddleware),
  window.devToolsExtension ? window.devToolsExtension() : f => f,
));

store.dispatch(actions.fetchContext());

store.subscribe(() => {
  window.store = _.assign({}, store.getState());
});

setTimeout(() => {
  console.log(store.getState());
}, 1000);

export default store;
