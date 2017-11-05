import React from 'react';

import SwingChart from '../components/SwingChart';


const SwingChartContainer = (props) => {
  return (
    <div className="swing-chart row-fluid section">
    <div class="content-large">
      <div class="section-header-wrap"><div class="header-line"></div><h2 class="section-title">How did voters shift from 2016?</h2></div>
      <SwingChart session={props.session} />
    </div>
    <div class="content-group ad">
        <p>Advertisement</p>
        <div class="ad-slot flex horizontal" id="pol-06" ></div>
    </div>
    </div>
  );
};

export default SwingChartContainer;
