import { attr, Model } from 'redux-orm';

class Office extends Model {
  serialize() {
    return this.ref;
  }

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

export default Office;
