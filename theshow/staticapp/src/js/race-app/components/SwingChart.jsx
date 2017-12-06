import React from 'react';
import countySwing from 'politico-module-elections-county-arrow-swing-chart';
import debounce from 'lodash/debounce';

// Initialize the chart
const chart = countySwing();

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
        d.code.substr(0,2) === window.appConfig.stateFips
      ).toModelArray();

    return election.serializeResults(counties);
  }

  // Calls our chart's create function.
  // (Must be able to be called multiple times, i.e., idempotent charts!)
  drawChart() {
    const results = this.fetchData();
    const db = this.props.session;

    if (!results || Object.keys(results.divisions).length < 1) {
      return
    };

    const state = db.Division
      .filter(d => d.level === 'state')
      .first();

    if (!state || !state.topojson) return;

    chart.create('#county-swing', results, state.topojson, `https://www.politico.com/interactives/elections/cdn/historical-results/2016-11-08/president/${window.appConfig.stateSlug}/data.json`,
    {
      range: ['#2b6abd', '#fd5639'],
      legendHeight: 0,
      legendPadding: 15,
      linePadding: 3,
      mapWidth: 100,
      mapHeight: 100,
      minimumToShow: 0,
      margin: {
        top: 20,
        right: 35,
        bottom: 30,
        left: 35,
      },
      rangeMax: 20,
      tooltip: {
        active: false,
        xStyle: null,
        yStyle: null,
        fips: null,
        datum: null,
        voteShare: 0,
    },
    });
  }

  // START HERE
  render() {
    return (
      <div className="swing-chart">
        <div id="county-swing" />
      </div>
    );
  }
}

export default ResultsBar;
