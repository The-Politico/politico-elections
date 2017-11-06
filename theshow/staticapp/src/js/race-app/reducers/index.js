import { combineReducers } from 'redux';
import content from './content';
import orm from './orm';
import fetch from './fetch';

/**
 * We store the last run action type to intercept updates
 * to results and context data. See stores/index.js.
 */
const lastAction = (state = null, action) => action.type; // eslint-disable-line no-unused-vars

export default combineReducers({
  content,
  orm,
  fetch,
  lastAction,
});
