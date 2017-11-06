import React from 'react';

import ResultsBar from '../components/ResultsBar';
import ResultsMap from '../components/ResultsMap';
import FetchRefresh from '../components/FetchRefresh';

const TopResults = props => (
  <div className="top-results row-fluid section">
    <div className="content-extra-large">
      <div className="loading-bar">
        <FetchRefresh fetch={props.fetch} actions={props.actions} />
      </div>
      <div className="bar">
        <ResultsBar session={props.session} />
      </div>
      <div className="map">
        <ResultsMap session={props.session} />
      </div>
      <div className="clear" />
    </div>
  </div>
);

export default TopResults;
