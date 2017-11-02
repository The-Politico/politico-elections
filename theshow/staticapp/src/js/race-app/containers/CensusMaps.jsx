import React from 'react';

// import ResultsBar from '../components/ResultsBar';


const CensusMaps = (props) => {
  return (
    <div className="scatter-plots content-large row-fluid section">
    <h2>Who lives where?</h2>
      <div className="bar col-sm-4">
        <h3>Map 1</h3>
        <figure>
          <img src="http://via.placeholder.com/400x400?text=Map"/>
        </figure>
      </div>
      <div className="bar col-sm-4">
            <h3>Map 2</h3>
          <figure>
            <img src="http://via.placeholder.com/400x400?text=Map"/>
          </figure>
      </div>
      <div className="bar col-sm-4">
            <h3>Map 3</h3>
          <figure>
            <img src="http://via.placeholder.com/400x400?text=Map"/>
          </figure>
      </div>

      <div class="clear"></div>
    </div>
  );
};

export default CensusMaps;
