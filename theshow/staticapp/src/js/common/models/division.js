import { fk, attr, Model } from 'redux-orm';

class Division extends Model {
  serialize() {
    return this.ref;
  }

  static get fields() {
    return {
      id: attr(),
      code: attr(),
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

export default Division;
