import React from 'react';

// import ResultsBar from '../components/ResultsBar';


const ScatterPlots = (props) => {
  return (
    <div className="scatter-plots row-fluid section content-extra-extra-large">
    <h2>Scatter plot title</h2>
    <p>Any explainer here</p>
      <div className="bar col-sm-3">
        <h3> scatter plot 1</h3>
        <figure>
          <img src="http://via.placeholder.com/300x300?text=Scatter"/>
        </figure>
      </div>
      <div className="bar col-sm-3">
          <h3> scatter plot 2</h3>
          <figure>
            <img src="http://via.placeholder.com/300x300?text=Scatter"/>
          </figure>
      </div>
      <div className="bar col-sm-3">
          <h3> scatter plot 3</h3>
          <figure>
            <img src="http://via.placeholder.com/300x300?text=Scatter"/>
          </figure>
      </div>
      <div className="bar col-sm-3">
          <h3> scatter plot 4</h3>
          <figure>
            <img src="http://via.placeholder.com/300x300?text=Scatter"/>
          </figure>
      </div>
      <div class="clear"></div>
    </div>
  );
};

export default ScatterPlots;
