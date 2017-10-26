import { fk, attr, Model } from 'redux-orm';

class Result extends Model {
  serialize() {
    return this.ref;
  }

  /**
   * Serializes the precinct status of an election.
   * @return {Object}   Status.
   */
  serializeStatus() {
    return {
      precinctsReporting: this.precinctsReporting,
      precinctsReportingPct: this.precinctsReportingPct,
      precinctsTotal: this.precinctsTotal,
    };
  }

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

Result.modelName = 'Result';

export default Result;
