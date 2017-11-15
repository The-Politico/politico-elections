import assign from 'lodash/assign';
import * as types from '../constants/actions';

export default(currentState, action) => {
  const initialState = {
    pageBlocks: {},
    pageTypeBlocks: {},
  };

  if (typeof currentState === 'undefined') {
    return initialState;
  }

  switch (action.type) {
    case types.CREATE_PAGE_CONTENT_BLOCK:
      return assign({}, currentState, {
        pageBlocks: action.block,
      });
    case types.CREATE_PAGE_TYPE_CONTENT_BLOCK:
      return assign({}, currentState, {
        pageTypeBlocks: action.block,
      });
    default:
      break;
  }
  return currentState;
};
