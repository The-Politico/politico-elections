import * as types from '../constants/actions';
import orm from '../models/';

export default(dbState, action) => {
  if (typeof dbState === undefined) {
    return orm.getEmptyState();
  }

  const session = orm.session(dbState);
  const { Division, Office, APMeta, Party, Candidate, Election, Result } = session;

  switch (action.type) {
    case types.CREATE_DIVISION:
      Division.create(action.division);
      break;
    case types.CREATE_OFFICE:
      Office.create(action.office);
      break;
    case types.CREATE_APMETA:
      APMeta.create(action.apMeta);
      break;
    case types.CREATE_PARTY:
      Party.create(action.party);
      break;
    case types.CREATE_CANDIDATE:
      Candidate.create(action.candidate);
      break;
    case types.CREATE_ELECTION:
      Election.create(action.election);
      break;
    case types.CREATE_RESULT:
      Result.create(action.result);
      break;
    default:
      break;
  }
  return session.state;
};