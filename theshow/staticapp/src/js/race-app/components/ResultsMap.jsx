import React from 'react';
import resultCounty from 'politico-module-elections-results-county-map';
import _ from 'lodash';

// Initialize the chart
const chart = resultCounty();

class ResultsMap extends React.Component {
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

    const counties = db.Division
      .filter(d =>
        d.level === 'county')
      .toModelArray();

    return election.serializeResults(counties);
  }

  // Calls our chart's create function.
  // (Must be able to be called multiple times, i.e., idempotent charts!)
  drawChart() {
    const db = this.props.session;
    const results = this.fetchData();

    if (!results) return;

    const state = db.Division
      .filter(d => d.level === 'state')
      .first();

    if (!state.topojson) return;

    console.log('Map data', results, state.topojson);

    chart.create('#resultsMap', results.divisions.VA);
  }

  // START HERE
  render() {
    return (
      <div className="results-map">
        <div id="resultsMap" />
      </div>
    );
  }
}

export default ResultsMap;
