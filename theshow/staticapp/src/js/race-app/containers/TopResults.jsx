import React from 'react';

import ResultsBar from '../components/ResultsBar';
import ResultsMap from '../components/ResultsMap';

const TopResults = (props) => {
  return (
    <div className="top-results">
      <ResultsBar session={props.session} />
      <ResultsMap session={props.session} />
    </div>
  );
};

export default TopResults;
