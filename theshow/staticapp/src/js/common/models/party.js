import { attr, Model } from 'redux-orm';

class Party extends Model {
  serialize() {
    return this.ref;
  }

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

export default Party;
