import React from 'react';

import ResultsBar from '../components/ResultsBar';
import ResultsMap from '../components/ResultsMap';

const TopResults = (props) => {
  return (
    <div className="top-results row-fluid content-extra-large section">
      <div className="bar">
        <ResultsBar session={props.session} />
      </div>
      <div className="map">
        <ResultsMap session={props.session} />
      </div>
      <div class="clear"></div>
      <p class="text-align-center"> !!!!AD cube ad here!!!! </p>
    </div>
  );
};

export default TopResults;
