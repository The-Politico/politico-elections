import _ from 'lodash';
import * as apiActions from './api';
import * as ormActions from './orm';

const actions = _.assign(
  {},
  apiActions,
  ormActions,
);

export default actions;
