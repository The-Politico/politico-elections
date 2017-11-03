import React from 'react';

// import ResultsBar from '../components/ResultsBar';


const ScatterPlots = (props) => {
  return (
    <div className="scatter-plots row-fluid section content-extra-extra-large">
    <h2>Where did different voting blocks land? </h2>
    <p class="sans">
      <strong>Each dot respresents a county.</strong> The further left the dot the more Democratic the county voted, the futher right, the more Republican. The closer to the top of the chart the more the county identifies with the census group. The top line shows how strong of a predictor TK.
    </p>

      <div className="col-sm-3">
        <h3>Education</h3>
        <figure>
          <img src="http://via.placeholder.com/300x300?text=Scatter"/>
        </figure>
      </div>
      <div className="col-sm-3">
          <h3>Minority (nonwhite)</h3>
          <figure>
            <img src="http://via.placeholder.com/300x300?text=Scatter"/>
          </figure>
      </div>
      <div className="col-sm-3">
          <h3>Below the poverty line</h3>
          <figure>
            <img src="http://via.placeholder.com/300x300?text=Scatter"/>
          </figure>
      </div>
      <div className="col-sm-3">
          <h3>Middle class</h3>
          <figure>
            <img src="http://via.placeholder.com/300x300?text=Scatter"/>
          </figure>
      </div>
      <div class="clear"></div>
    </div>
  );
};

export default ScatterPlots;
