import * as types from '../constants/actions';

export const storeChatter = chatter => ({
  type: types.CREATE_CHATTER,
  chatter,
});

