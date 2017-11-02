import React from 'react';

import ResultsBar from '../components/ResultsBar';
import ResultsMap from '../components/ResultsMap';

const TopResults = (props) => {
  return (
    <div className="top-results row-fluid content-extra-large section">
      <div className="bar col-sm-5">
        <ResultsBar session={props.session} />
      </div>
      <div className="map col-sm-7">
        <ResultsMap session={props.session} />
      </div>
      <div class="clear"></div>
    </div>
  );
};

export default TopResults;
