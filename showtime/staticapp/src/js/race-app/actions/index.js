import _ from 'lodash';
import * as apiActions from './api';
import * as ormActions from './orm';

export default _.assign({},
  apiActions,
  ormActions,
);