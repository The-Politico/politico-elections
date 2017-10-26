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
    const results = [];
    const aggregatedResults = [];

    this.candidates.toModelArray().forEach((candidate) => {
      divisions.forEach((division) => {
        const result = candidate.fetchResult(division);
        // Some county divisions don't have results...
        if (!result) {
          console.log('No results for division:', division.id);
          return;
        }

        const resultObj = {
          candidate: candidate.serialize(),
          division: division.serialize(),
          voteCount: result.voteCount,
          votePct: result.votePct,
          precinctsReporting: result.precinctsReporting,
          precinctsTotal: result.precinctsTotal,
          precinctsReportingPct: result.precinctsReportingPct,
        };

        // Aggregate aggregable candidates' vote totals
        // and percents by division
        if (candidate.aggregable) {
          const divisionResult = _.find(
            aggregatedResults,
            d => d.division.id === division.id,
          );
          if (divisionResult) {
            aggregatedResults.pop(divisionResult);
            divisionResult.voteCount += resultObj.voteCount;
            divisionResult.votePct += resultObj.votePct;
            aggregatedResults.push(divisionResult);
          } else {
            resultObj.candidate = 'other';
            aggregatedResults.push(resultObj);
          }
        } else {
          results.push(resultObj);
        }
      });
    });

    return {
      id: this.id,
      status: this.serializeStatus(),
      office: this.office.serialize(),
      results: results.concat(aggregatedResults),
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
