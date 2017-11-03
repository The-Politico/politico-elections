import React from 'react';

import ResultsBar from '../components/ResultsBar';
import ResultsMap from '../components/ResultsMap';

const TopResults = (props) => {
  return (
    <div className="top-results row-fluid section">
    <div class="content-extra-large">
        <div className="loading-bar">
          <p>Checking for new results</p>
        </div>
      {/*<div className="loading-bar new-results">
          <p class="new-results"> We found new results!</p>
      </div>*/}
        <div className="bar">
          <ResultsBar session={props.session} />
        </div>
        <div className="map">
          <ResultsMap session={props.session} />
        </div>
        <div class="clear"></div>
    </div>
    </div>
  );
};

export default TopResults;
