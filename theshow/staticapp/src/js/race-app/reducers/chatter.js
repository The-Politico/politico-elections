import * as types from '../constants/actions';

export default(currentState, action) => {
  const initialState = {
    chatter: '',
  };

  if (typeof currentState === 'undefined') {
    return initialState;
  }

  switch (action.type) {
    case types.CREATE_CHATTER:
      return Object.assign({}, currentState, {
        chatter: action.chatter,
      });
    default:
      break;
  }
  return currentState;
}