import React from 'react';
import CountdownFetch from 'politico-countdown-fetch';
import debounce from 'lodash/debounce';
import refreshRates from '../constants/api';

// Initialize the chart
const chart = CountdownFetch();

class ResultsMap extends React.Component {
  /**
   * constructor lets us bind custom methods to our component class.
   */
  constructor(props) {
    super(props);
    // Bind our custom methods (using ES7 bind syntax "::").
    this.drawChart = ::this.drawChart;
    this.newResults = ::this.newResults;
  }

  // Called first time our component is mounted, i.e., just once.
  componentDidMount() {
    this.drawChart();

    // Attach a resize func here!
    window.addEventListener('resize', debounce(() => {
      chart.resize();
    }, 400));
  }

  // Called every time our component's props update,
  // i.e., whenever our data updates.
  componentDidUpdate() {
    this.drawChart();
    if (this.props.fetch.notifyNew) this.newResults();
  }

  /* eslint-disable class-methods-use-this */
  // Calls our chart's create function.
  // (Must be able to be called multiple times, i.e., idempotent charts!)
  drawChart() {
    chart.create('#fetch-refresh-widget-component', {
      refreshTime: refreshRates.results / 1000,
      width: 160,
      height: 30,
      originOffset: -15,
    });
  }

  newResults() {
    chart.succeed();
    this.props.actions.resetNotifyResults();
  }
  /* eslint-enable class-methods-use-this */

  // START HERE
  render() {
    return (
      <div>
        <div id="fetch-refresh-widget-component" />
      </div>
    );
  }
}

export default ResultsMap;
