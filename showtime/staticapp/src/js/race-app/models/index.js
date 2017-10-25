import { fk, many, oneToOne, attr, Model, ORM } from 'redux-orm';

class Election extends Model {
  serializeResults(divisions) {
    console.log(divisions);
    return { election: this };
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
