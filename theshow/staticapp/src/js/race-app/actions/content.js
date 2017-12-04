import * as types from '../constants/actions';

export const createPageContentBlock = block => ({
  type: types.CREATE_PAGE_CONTENT_BLOCK,
  block,
});

export const createPageTypeContentBlock = block => ({
  type: types.CREATE_PAGE_TYPE_CONTENT_BLOCK,
  block,
});

export const createMapAnnotation = mapAnnotation => ({
  type: types.CREATE_MAP_ANNOTATION,
  mapAnnotation,
});