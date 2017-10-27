import { attr, Model } from 'redux-orm';

class APMeta extends Model {
  serialize() {
    return {
      called: this.called,
      tabulated: this.tabulated,
      overrideApCall: this.overrideApCall,
      overrideApVotes: this.overrideApVotes,
    };
  }

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

export default APMeta;
