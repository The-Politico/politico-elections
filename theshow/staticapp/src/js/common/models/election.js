import { fk, many, oneToOne, attr, Model } from 'redux-orm';
import _ from 'lodash';

class Election extends Model {
  /**
   * Serializes the status of this election.
   * @return {Object}   Status object.
   */
  serializeStatus() {
    return _.assign(
      {},
      this.apMeta.serialize(),
    );
  }

  /**
   * Serializes the results of this election in
   * the given divisions.
   * @param  {Array} divisions  Divisions.
   * @return {Object}           Serialized results.
   */
  serializeResults(divisions) {
    const status = this.serializeStatus();
    const divisionResults = {};

    divisions.forEach((division) => {
      const obj = _.assign({}, division.serialize());
      obj.results = [];

      const firstResult = division.resultSet.first();
      if (!firstResult) {
        console.log('No results for division:', division.id);
        return;
      }
      obj.precinctsReporting = firstResult.precinctsReporting;
      obj.precinctsReportingPct = firstResult.precinctsReportingPct;
      obj.precinctsTotal = firstResult.precinctsTotal;

      division.resultSet.toModelArray().forEach((result) => {
        const resultObj = {
          candidate: result.candidate.serialize(),
          voteCount: result.voteCount,
          votePct: result.votePct,
          winner: status.overrideApCall ? result.candidate.override_winnner : result.winner
        };

        // Aggregate aggregable candidates' vote totals
        // and percents by division
        if (result.candidate.aggregable) {
          const other = _.find(
            obj.results,
            d => d.candidate === 'other',
          );
          if (other) {
            obj.results.pop(other);
            other.voteCount += resultObj.voteCount;
            other.votePct += resultObj.votePct;
            obj.results.push(other);
          } else {
            resultObj.candidate = 'other';
            obj.results.push(resultObj);
          }
        } else {
          obj.results.push(resultObj);
        }
      });
      divisionResults[division.id] = obj;
    });

    return {
      id: this.id,
      status: this.serializeStatus(),
      office: this.office.serialize(),
      divisions: divisionResults,
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
