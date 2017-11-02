import { combineReducers } from 'redux';
import chatter from './chatter';
import orm from './orm';

export default combineReducers({
  chatter,
  orm,
});
