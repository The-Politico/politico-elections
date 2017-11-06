import * as types from '../constants/actions';

export const setResultsModifiedTime = time => ({
  type: types.SET_RESULTS_MODIFIED_TIME,
  time,
});

export const setContextModifiedTime = time => ({
  type: types.SET_CONTEXT_MODIFIED_TIME,
  time,
});

export const notifyNewResults = () => ({
  type: types.NOTIFY_NEW_RESULTS,
});

export const resetNotifyResults = () => ({
  type: types.RESET_NOTIFY_RESULTS,
});
