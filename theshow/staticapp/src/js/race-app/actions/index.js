import { assign } from 'lodash';
import * as apiActions from './api';
import * as chatterActions from './chatter';
import * as ormActions from './orm';

const actions = assign(
  {},
  apiActions,
  chatterActions,
  ormActions,
);

export default actions;
