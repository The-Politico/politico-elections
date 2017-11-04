import { combineReducers } from 'redux';
import content from './content';
import orm from './orm';

export default combineReducers({
  content,
  orm,
});
