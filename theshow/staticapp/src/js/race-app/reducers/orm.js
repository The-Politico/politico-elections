import * as types from '../constants/actions';
import orm from '../../common/models/';

export default(dbState, action) => {
  if (typeof dbState === 'undefined') {
    return orm.getEmptyState();
  }

  const session = orm.session(dbState);
  const {
    Division,
    Office,
    APMeta,
    Party,
    Candidate,
    Election,
    Result,
  } = session;

  switch (action.type) {
    case types.CREATE_DIVISION:
      Division.upsert(action.division);
      break;
    case types.CREATE_OFFICE:
      Office.upsert(action.office);
      break;
    case types.CREATE_APMETA:
      APMeta.upsert(action.apMeta);
      break;
    case types.CREATE_PARTY:
      Party.upsert(action.party);
      break;
    case types.CREATE_CANDIDATE:
      Candidate.upsert(action.candidate);
      break;
    case types.CREATE_ELECTION:
      Election.upsert(action.election);
      break;
    case types.CREATE_RESULT:
      Result.upsert(action.result);
      break;
    case types.UPDATE_GEO:
      Division
        .filter(d => d.code === action.fips)
        .update({ topojson: action.topojson });
      break;
    default:
      break;
  }
  return session.state;
};
