import assign from 'lodash/assign';
import * as types from '../constants/actions';

export default(currentState, action) => {
  const initialState = {
    blocks: {},
  };

  if (typeof currentState === 'undefined') {
    return initialState;
  }

  switch (action.type) {
    case types.CREATE_CONTENT_BLOCK:
      return assign({}, currentState, {
        blocks: action.block,
      });
    default:
      break;
  }
  return currentState;
};
