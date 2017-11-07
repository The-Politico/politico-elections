import React from 'react';

import SwingChart from '../components/SwingChart';

import NerdBox from '../../common/components/CollapsibleNerdBox';


const SwingChartContainer = props => (
  <div className="swing-chart row-fluid section">
    <div className="content-large">
      <div className="section-header-wrap">
        <div className="header-line" />
        <h2 className="section-title">Vote shift from 2016</h2>
      </div>
      <div className="chatter">
        <p>
        Is it a Trump bump or the Trump slump? As the votes come in, we&rsquo;re watching
        how the candidates&rsquo; vote share differs from the 2016 presidential election.
        We&rsquo;re using the head-to-head vote split in this chart to show what
        Republicans or Democrats have
        gained or lost against each other, removing any third parties from the equation.
        Watch for the bars for each county to update as results come in.
        </p>
      </div>
      <SwingChart session={props.session} />
      <div>
        <NerdBox
          note="
          Vote percents represent the head-to-head vote split between only Democrats and Republicans
          and don&rsquo;t include third party votes. So, for example, Dem. votes /
          (Dem. votes + GOP votes) = Dem. percent.
          "
        />
      </div>
    </div>
    <div className="content-group ad">
      <p>Advertisement</p>
      <div className="ad-slot flex horizontal" id="pol-06" />
    </div>
  </div>
);

export default SwingChartContainer;
