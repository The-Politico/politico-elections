import React from 'react';
import demographicPlot from 'politico-module-elections-demographic-vote-trend-scatterplots';
import { debounce } from 'lodash';

class ResultsBar extends React.Component {
  /**
   * constructor lets us bind custom methods to our component class.
   */
  constructor(props) {
    const chart = demographicPlot();
    super(props);
    // Bind our custom methods (using ES7 bind syntax "::").
    this.drawChart = ::this.drawChart;
    this.fetchData = ::this.fetchData;
    this.chart = chart;
  }

  // Called first time our component is mounted, i.e., just once.
  componentDidMount() {
    this.drawChart();

    // Attach a resize func here!
    window.onresize = debounce(() => {
      this.chart.resize();
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
        d.level === 'county' &&
        d.code.substr(0,2) === window.appConfig.stateFips
      ).toModelArray();

    return election.serializeResults(counties);
  }

  // Calls our chart's create function.
  // (Must be able to be called multiple times, i.e., idempotent charts!)
  drawChart() {
    const results = this.fetchData();

    if (!results || Object.keys(results.divisions).length < 1) {
      return
    };

    console.log(this.props)

    this.chart.create(
      `#scatterplot-${this.props.data_key}`, 
      results, 
      `https://www.politico.com/interactives/elections/data/us-census/acs5/2015/${window.appConfig.stateFips}/${this.props.variable}.json`,
      {
        dataKeys: {
          y: 'Percent',
          x: 'MarginOfError',
          n: 'GeographicArea',
          geoid: 'TargetGeoId2'
        },
        trendX: this.props.trendX,
        censusAccessor: (d) => d[this.props.data_key] / d.total,
        footnote: '',
      }
    );
  }

  // START HERE
  render() {
    return (
      <div className="scatterplot-wrapper">
        <div className="scatterplot" id={`scatterplot-${this.props.data_key}`} />
      </div>
    );
  }
}

export default ResultsBar;
