import { fk, attr, Model } from 'redux-orm';

class OverrideResult extends Model {
  serialize() {
    return this.ref;
  }

  /**
   * Serializes the precinct status of an election.
   * @return {Object}   Status.
   */

  static get fields() {
    return {
      id: attr(),
      voteCount: attr(),
      votePct: attr(),
      precinctsReporting: attr(),
      precinctsTotal: attr(),
      precinctsReportingPct: attr(),
      winner: attr(),
      division: fk('Division'),
      candidate: fk('Candidate'),
    };
  }
}

OverrideResult.modelName = 'OverrideResult';

export default OverrideResult;
