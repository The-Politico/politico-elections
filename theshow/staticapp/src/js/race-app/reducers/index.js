import { combineReducers } from 'redux';
import content from './content';
import orm from './orm';
import fetch from './fetch';

const lastAction = (state = null, action) => action.type;

export default combineReducers({
  content,
  orm,
  fetch,
  lastAction,
});
