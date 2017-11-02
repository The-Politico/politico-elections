import _ from 'lodash';
import * as apiActions from './api';
import * as chatterActions from './chatter';
import * as ormActions from './orm';

const actions = _.assign(
  {},
  apiActions,
  chatterActions,
  ormActions,
);

export default actions;
