import assign from 'lodash/assign';
import * as types from '../constants/actions';

export default(currentState, action) => {
  const initialState = {
    notifyNew: false,
    resultsModified: null,
    contextModified: null,
  };

  if (typeof currentState === 'undefined') {
    return initialState;
  }

  switch (action.type) {
    case types.NOTIFY_NEW_RESULTS:
      return assign({}, currentState, {
        notifyNew: true,
      });
    case types.RESET_NOTIFY_RESULTS:
      return assign({}, currentState, {
        notifyNew: false,
      });
    case types.SET_RESULTS_MODIFIED_TIME:
      return assign({}, currentState, {
        resultsModified: action.time,
      });
    case types.SET_CONTEXT_MODIFIED_TIME:
      return assign({}, currentState, {
        contextModified: action.time,
      });
    default:
      break;
  }
  return currentState;
};
