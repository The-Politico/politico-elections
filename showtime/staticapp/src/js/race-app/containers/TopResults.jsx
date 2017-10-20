import React from 'react';

import ResultsBar from '../components/ResultsBar';
import ResultsMap from '../components/ResultsMap';

const TopResults = (props) => {
  return (
    <div className="top-results">
      <ResultsBar />
      <ResultsMap />
    </div>
  );
};

export default TopResults;
