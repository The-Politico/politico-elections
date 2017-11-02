import React from 'react';

// import ResultsBar from '../components/ResultsBar';


const ScatterPlots = (props) => {
  return (
    <div className="scatter-plots row-fluid section content-extra-extra-large">
    <h2>How these groups voted</h2>
    <p class="sans">
      We probably want some chatter to help orient you to these charts. Robo text saying, <strong>nonwhite voters skewed TK</strong>, voters with <strong>high levels of education tk</strong>.
    </p>

      <div className="bar col-sm-3">
        <h3>Education</h3>
        <figure>
          <img src="http://via.placeholder.com/300x300?text=Scatter"/>
        </figure>
      </div>
      <div className="bar col-sm-3">
          <h3>Minority (nonwhite)</h3>
          <figure>
            <img src="http://via.placeholder.com/300x300?text=Scatter"/>
          </figure>
      </div>
      <div className="bar col-sm-3">
          <h3>Below the poverty line</h3>
          <figure>
            <img src="http://via.placeholder.com/300x300?text=Scatter"/>
          </figure>
      </div>
      <div className="bar col-sm-3">
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
