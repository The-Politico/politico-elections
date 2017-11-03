import React from 'react';

import ResultsBar from '../components/ResultsBar';
import ResultsMap from '../components/ResultsMap';

const TopResults = (props) => {
  return (
    <div className="top-results row-fluid section">
    <div class="content-extra-large">
        <div className="loading-bar">
          <p>Checking for results bar</p>
        </div>
        <div className="bar">
          <ResultsBar session={props.session} />
        </div>
        <div className="map">
          <ResultsMap session={props.session} />
        </div>
        <div class="clear"></div>
    </div>
      <div class="content-group ad">
          <p>Advertisement</p>
          <div class="ad-slot flex horizontal" id="pol-06" ></div>
      </div>

    </div>
  );
};

export default TopResults;
