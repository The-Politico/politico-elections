import React from 'react';
import turnoutPct from 'politico-elections-turnout';
import debounce from 'lodash/debounce';

// Initialize the chart
const chart = turnoutPct();

class TurnoutChart extends React.Component {
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
    window.addEventListener('resize', debounce(() => {
      chart.resize();
    }, 400));
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
        d.level === 'county' &&
        d.code.substr(0, 2) === window.appConfig.stateFips)
      .toModelArray();

    return election.serializeResults(counties);
  }

  // Calls our chart's create function.
  // (Must be able to be called multiple times, i.e., idempotent charts!)
  drawChart() {
    const results = this.fetchData();
    const db = this.props.session;

    if (!results || Object.keys(results.divisions).length < 1) return;

    const state = db.Division
      .filter(d => d.level === 'state')
      .first();

    if (!state || !state.topojson) return;

    chart.create(
      '#turnout-chart',
      results,
      state.topojson,
      `https://www.politico.com/interactives/elections/cdn/historical-results/2016-11-08/president/${window.appConfig.stateSlug}/data.json`,
      {
        range: ['#2b6abd', '#fd5639'],
        circlePadding: 4,
        minimumToShow: 6,
        rangeMax: 20,
        mapWidth: 100,
        mapHeight: 100,
        circleRadius: document.body.clientWidth < 450 ? 4 : 6,
      },
    );
  }

  // START HERE
  render() {
    return (
      <div className="turnout-chart">
        <div id="turnout-chart" />
      </div>
    );
  }
}

export default TurnoutChart;
