import * as types from '../constants/actions';

const createContentBlock = block => ({
  type: types.CREATE_CONTENT_BLOCK,
  block,
});

export default createContentBlock;
