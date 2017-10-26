import { fk, many, oneToOne, attr, Model } from 'redux-orm';
import _ from 'lodash';

class Election extends Model {
  /**
   * Serializes the status of this election.
   * @return {Obj} Status object.
   */
  serializeStatus() {
    const result = this.candidates
      .toModelArray()[0]
      .resultSet.first();
    return _.assign(
      {},
      result.serializeStatus(),
      this.apMeta.serialize(),
    );
  }

  /**
   * Serializes the results of this election in
   * a given division.
   * @param  {Array} divisions  Divisions.
   * @return {Obj}              Serialized results.
   */
  serializeResults(divisions) {
    const results = [];

    this.candidates.toModelArray().forEach((candidate) => {
      divisions.forEach((division) => {
        const result = candidate.fetchResult(division);

        const resultObj = {
          candidate: candidate.serialize(),
          division: division.serialize(),
          voteCount: result.voteCount,
          votePct: result.votePct,
        };
        results.push(resultObj);
      });
    });

    return {
      id: this.id,
      status: this.serializeStatus(),
      office: this.office.serialize(),
      results,
    };
  }

  static get fields() {
    return {
      id: attr(),
      date: attr(),
      office: oneToOne('Office'),
      division: fk('Division'),
      candidates: many('Candidate'),
      apMeta: oneToOne('APMeta'),
      party: fk('Party'),
    };
  }
}

Election.modelName = 'Election';

export default Election;
