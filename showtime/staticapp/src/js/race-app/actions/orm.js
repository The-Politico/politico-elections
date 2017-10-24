import * as types from '../constants/actions';

export const createDivision = division => {
  return {
    type: types.CREATE_DIVISION,
    division,
  }
}

export const createElection = election => {
  return {
    type: types.CREATE_ELECTION,
    election,
  }
}

export const createOffice = office => {
  return {
    type: types.CREATE_OFFICE,
    office,
  }
}

export const createApMeta = apMeta => {
  return {
    type: types.CREATE_APMETA,
    apMeta,
  }
}

export const createParty = party => {
  return {
    type: types.CREATE_PARTY,
    party,
  }
}

export const createCandidate = candidate => {
  return {
    type: types.CREATE_CANDIDATE,
    candidate,
  }
}

export const createResult = result => {
  return {
    type: types.CREATE_RESULT,
    result,
  }
}

