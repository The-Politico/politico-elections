import React from 'react';

import SwingChart from '../components/SwingChart';


const SwingChartContainer = (props) => {
  return (
    <div className="swing-chart row-fluid section">
    <div class="content-large">
      <h2>How did voters shift from 2016?</h2>
      <p>
      Placeholder text from Jon - that talks about what the blue and red lines mean - doubling down that this a shift.
      </p>
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
