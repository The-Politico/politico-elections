import React from 'react';

import SwingChart from '../components/SwingChart';


const SwingChartContainer = (props) => {
  return (
    <div className="swing-chart row-fluid content-large section">
    <h2>County-by-county shifts</h2>
    <p class="sans">
      Also robo here, <strong>TK counties swung from Dem. to GOP.</strong>, while <strong>TK counties swung from GOP to Dem</strong>.
    </p>
    <SwingChart session={props.session} />
    </div>
  );
};

export default SwingChartContainer;
