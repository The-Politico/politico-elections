import { assign } from 'lodash';
import * as apiActions from './api';
import * as contentActions from './content';
import * as ormActions from './orm';

const actions = assign(
  {},
  apiActions,
  contentActions,
  ormActions,
);

export default actions;
