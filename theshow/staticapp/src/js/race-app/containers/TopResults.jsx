import React from 'react';

// import ResultsBar from '../components/ResultsBar';
import ResultsMap from '../components/ResultsMap';

const TopResults = (props) => {
  return (
    <div className="top-results">

      <ResultsMap session={props.session} />
    </div>
  );
};

export default TopResults;
