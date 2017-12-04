import assign from 'lodash/assign';
import * as types from '../constants/actions';

export default(currentState, action) => {
  const initialState = {
    page: {},
    pageType: {},
    mapAnnotation: {
      cities: [],
    },
  };

  if (typeof currentState === 'undefined') {
    return initialState;
  }

  switch (action.type) {
    case types.CREATE_PAGE_CONTENT_BLOCK:
      return assign({}, currentState, {
        page: action.block,
      });
    case types.CREATE_PAGE_TYPE_CONTENT_BLOCK:
      return assign({}, currentState, {
        pageType: action.block,
      });
    case types.CREATE_MAP_ANNOTATION:
      const mapAnnotation = assign({}, currentState.mapAnnotation, action.mapAnnotation);
      return assign({}, currentState, {
        mapAnnotation,
      })
    default:
      break;
  }
  return currentState;
};
