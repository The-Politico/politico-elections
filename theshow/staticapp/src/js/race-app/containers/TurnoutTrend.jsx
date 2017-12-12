import React from 'react';

import TurnoutChart from '../components/TurnoutChart';
import NerdBox from '../../common/components/CollapsibleNerdBox';


const TurnoutChartContainer = props => props.hidden ? null : (
  <div className="turnout-chart row-fluid section">
    <div className="content-large">
      <div className="section-header-wrap">
        <div className="header-line" />
        <h2 className="section-title">Tale of the turnout</h2>
      </div>
      <div className="chatter">
        <p>
        Whether it&rsquo;s a midterm or a special election, fewer voters show up to the polls when they aren&rsquo;t voting for a president. That decrease in participation changes the electorate and may benefit one party more than another.
        </p>
        <div className="clearfix float-box">
          <h4>How to read this chart</h4>
          <div className="float-left left">
            <p>
            This chart measures the change in the number of votes cast between the 2016 presidential election and this one. We compare that change with the same shift in the head-to-head vote split. Look for counties further in the corners of the chart. They are areas where a change in turnout overwhelming benefited one party.
            </p>
          </div>
          <div className="float-left right">
            <img
              alt="How to read these charts"
              src="https://www.politico.com/interactives/elections/cdn/images/2017-12-12/turnout-chart-hint.jpg"
            />
          </div>
        </div>
      </div>
      <TurnoutChart session={props.session} />
      <div className="footnote">
        <small>
          All numbers represent the change from the 2016 presidential election.
        </small>
      </div>
      <div>
        <NerdBox
          note="
          Change in turnout in this chart is estimated using the percent change in the raw number of votes by county. Large changes in the number of registered voters in a county can make that change in the raw vote a less effective measure of turnout.
          "
        />
      </div>
    </div>
  </div>
);

export default TurnoutChartContainer;
