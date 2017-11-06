import React from 'react';

import SwingChart from '../components/SwingChart';


const SwingChartContainer = props => (
  <div className="swing-chart row-fluid section">
    <div className="content-large">
      <div className="section-header-wrap">
        <div className="header-line" />
        <h2 className="section-title">Vote shift from 2016</h2>
      </div>
      <div className="chatter">
        <p>Did voters shift left or right? This chart shows how both candidates
        compare to the vote in the 2016 presidential election by county.
        </p>
      </div>
      <SwingChart session={props.session} />
    </div>
    <div className="content-group ad">
      <p>Advertisement</p>
      <div className="ad-slot flex horizontal" id="pol-06" />
    </div>
  </div>
);

export default SwingChartContainer;
