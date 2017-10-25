import { fk, many, oneToOne, attr, Model, ORM } from 'redux-orm';

class Election extends Model {
  serializeResults(divisions) {
    const candidates = this.candidates.toModelArray();

    // grab the first result for precinct numbers
    const firstResult = candidates[0].resultSet.first();
    const electionStatus = {
      precinctsReporting: firstResult.precinctsReporting,
      precinctsReportingPct: firstResult.precinctsReportingPct,
      precinctsTotal: firstResult.precinctsTotal,
      called: this.apMeta.called,
      tabulated: this.apMeta.tabulated,
      overrideApCall: this.apMeta.overrideApCall,
      overrideApVotes: this.apMeta.overrideApVotes,
    }

    // build results
    const results = [];
    candidates.forEach((c) => {
      divisions.forEach((d) => {
        const matchField = d.level === 'state' ? d.postalCode : d.id;
        const result = c.resultSet
          .filter(f => (f.division === matchField))
          .toModelArray()[0];

        const candidate = Object.assign({}, c._fields);
        const party = c.party._fields;
        candidate['party'] = party;

        const resultObj = {
          candidate: candidate,
          division: d._fields,
          voteCount: result.voteCount,
          votePct: result.votePct,
        };
        results.push(resultObj);
      });
    });

    return {
      electionStatus,
      results,
    };
  }

  static get fields() {
    return {
      id: attr(),
      date: attr(),
      office: fk('Office'),
      division: fk('Division'),
      candidates: many('Candidate'),
      apMeta: oneToOne('APMeta'),
      party: fk('Party'),
    };
  }
}

Election.modelName = 'Election';


class Office extends Model {
  static get fields() {
    return {
      id: attr(),
      slug: attr(),
      name: attr(),
      label: attr(),
      short_label: attr(),
    };
  }
}

Office.modelName = 'Office';


class Division extends Model {
  static get fields() {
    return {
      id: attr(),
      level: attr(),
      label: attr(),
      shortLabel: attr(),
      codeComponents: attr(),
      parent: fk('Division'),
      postalCode: attr(),
    };
  }
}

Division.modelName = 'Division';


class Candidate extends Model {
  static get fields() {
    return {
      id: attr(),
      firstName: attr(),
      middleName: attr(),
      lastName: attr(),
      suffix: attr(),
      aggregable: attr(),
      winner: attr(),
      incumbent: attr(),
      uncontested: attr(),
      image: attr(),
      party: fk('Party'),
    };
  }
}

Candidate.modelName = 'Candidate';


class Party extends Model {
  static get fields() {
    return {
      id: attr(),
      label: attr(),
      shortLabel: attr(),
      slug: attr(),
    };
  }
}

Party.modelName = 'Party';


class APMeta extends Model {
  static get fields() {
    return {
      id: attr(),
      called: attr(),
      tabulated: attr(),
      overrideApCall: attr(),
      overrideApVotes: attr(),
    };
  }
}

APMeta.modelName = 'APMeta';


class Result extends Model {
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

const orm = new ORM();
orm.register(Election, Office, Division, Candidate, Party, APMeta, Result);

export default orm;
