import * as types from '../constants/actions';

export const createDivision = division => ({
  type: types.CREATE_DIVISION,
  division,
});

export const createElection = election => ({
  type: types.CREATE_ELECTION,
  election,
});

export const createOffice = office => ({
  type: types.CREATE_OFFICE,
  office,
});

export const createApMeta = apMeta => ({
  type: types.CREATE_APMETA,
  apMeta,
});

export const createParty = party => ({
  type: types.CREATE_PARTY,
  party,
});

export const createCandidate = candidate => ({
  type: types.CREATE_CANDIDATE,
  candidate,
});

export const createResult = result => ({
  type: types.CREATE_RESULT,
  result,
});

export const updateGeo = (fips, topojson) => ({
  type: types.UPDATE_GEO,
  fips,
  topojson,
});

export const createOverrideResult = overrideResult => ({
  type: types.CREATE_OVERRIDE_RESULT,
  overrideResult,
});
