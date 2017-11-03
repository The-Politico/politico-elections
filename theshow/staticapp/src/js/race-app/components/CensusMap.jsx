import React from 'react';
import usDemographic from 'politico-module-elections-demographic-county-map';
import { debounce } from 'lodash';
import * as d3 from 'd3';

class CensusMap extends React.Component {
  /**
   * constructor lets us bind custom methods to our component class.
   */
  constructor(props) {
    const chart = usDemographic();
    super(props);
    // Bind our custom methods (using ES7 bind syntax "::").
    this.drawChart = ::this.drawChart;
    this.chart = chart;
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

  // Calls our chart's create function.
  // (Must be able to be called multiple times, i.e., idempotent charts!)
  drawChart() {
    const db = this.props.session;

    const state = db.Division
      .filter(d => d.level === 'state')
      .first();

    if (!state || !state.topojson) return;

    this.chart.create(
      `#demographic-map-${this.props.data_key}`,
      state.topojson,
      `https://www.politico.com/interactives/elections/data/us-census/acs5/2015/${window.appConfig.stateFips}/${this.props.variable}.json`,
      {
        range: ['#f7e9c9', '#f3ddac', '#edcd83', '#e7bc5a', '#c8951e'],
        projection: d3.geoMercator,
        scaleType: d3.scaleThreshold,
        noData: '#e2e2e2',
        censusAccessor: this.props.accessor,
      }
    );
  }

  // START HERE
  render() {
    return (
      <div className="demograhic-map-wrapper">
        <div className="demographic-map" id={`demographic-map-${this.props.data_key}`} />
      </div>
    );
  }
}

export default CensusMap;
