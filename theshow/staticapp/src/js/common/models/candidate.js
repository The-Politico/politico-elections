import { fk, attr, Model } from 'redux-orm';
import _ from 'lodash';

class Candidate extends Model {
  serialize() {
    return _.assign(
      {},
      this.ref,
      { party: this.party.ref },
    );
  }

  /**
   * Fetches the result for this candidate in
   * a given division.
   * @param  {Model} division   A division model
   * @return {Model}            A result model
   */
  fetchResult(division) {
    const code = division.level === 'state' ?
      division.postalCode : division.id;
    const results = this.resultSet
      .filter(d => d.division === code);
    return results.toModelArray()[0];
  }

  static get fields() {
    return {
      id: attr(),
      firstName: attr(),
      middleName: attr(),
      lastName: attr(),
      suffix: attr(),
      aggregable: attr(),
      overrideWinner: attr(),
      incumbent: attr(),
      uncontested: attr(),
      image: attr(),
      party: fk('Party'),
    };
  }
}

Candidate.modelName = 'Candidate';

export default Candidate;
