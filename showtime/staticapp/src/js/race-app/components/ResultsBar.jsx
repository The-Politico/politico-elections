import React from 'react';
import CandidateResultsBar from 'candidate-results-bar';
import _ from 'lodash';

// Initialize the chart
const chart = CandidateResultsBar();

class ResultsBar extends React.Component {
  /**
   * constructor lets us bind custom methods to our component class.
   */
  constructor(props) {
    super(props);
    // Bind our custom methods (using ES7 bind syntax "::").
    this.drawChart = ::this.drawChart;
    this.fetchData = ::this.fetchData;
  }

  // Called first time our component is mounted, i.e., just once.
  componentDidMount() {
    this.drawChart();

    // Attach a resize func here!
    window.onresize = _.debounce(() => {
      chart.resize();
    }, 400);
  }

  // Called every time our component's props update,
  // i.e., whenever our data updates.
  componentDidUpdate() {
    this.drawChart();
  }

  // Gets data from our client database
  fetchData() {
    const db = this.props.session;

    const election = db.Election.first();
    if (!election) return null;

    const state = db.Division
      .filter(d =>
        d.level === 'state' &&
        d.code === window.appConfig.stateFips)
      .toModelArray();

    return election.serializeResults(state);
  }

  // Calls our chart's create function.
  // (Must be able to be called multiple times, i.e., idempotent charts!)
  drawChart() {
    const results = this.fetchData();

    if (!results) return;

    chart.create('#candidateResultsBar', results.divisions.VA);
  }

  // START HERE
  render() {
    return (
      <div className="results-bar">
        <div id="candidateResultsBar" />
      </div>
    );
  }
}

export default ResultsBar;
