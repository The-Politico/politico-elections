import React from 'react';

import ScatterPlot from '../components/ScatterPlot';

const ScatterPlots = (props) => {
  const censusVariables = [
    {
      variable: 'B03002',
      data_key: 'white_alone',
      trendX: 'minority',
      title: 'Minority (nonwhite) people',
      accessor: d => ((d.total - d.white_alone) / d.total),
    },
    {
      variable: 'B15003',
      data_key: 'college_educated',
      trendX: 'educated',
      title: 'College educated people',
      accessor: d => d.college_educated / d.total,
    },
    {
      variable: 'B19001',
      data_key: 'middle_class',
      trendX: 'middle class',
      title: 'Middle class people',
      accessor: d => d.middle_class / d.total,
    },
    {
      variable: 'B17020',
      data_key: 'impoverished',
      trendX: 'impoverished',
      title: 'People below the poverty line',
      accessor: d => d.impoverished / d.total,
    },
  ];
  return (
    <div className="scatter-plots row-fluid section content-extra-extra-large">
      <div className="section-header-wrap">
        <div className="header-line" />
        <h2 className="section-title">Voting block trends</h2>
      </div>
      <div className="chatter">
        <p>
        These charts use county-level data from the U.S. Census Bureau
        to estimate how strong was the relationship between different demographic
        groups and each party in this election.
        The sliding scale tells you how strong the relationship was, while the
        scatterplots show
        which party benefitted most from that group&rsquo;s support. Each dot is
        a county.
        </p>
      </div>
      <div className="plot-container">
        {censusVariables.map((obj, index) => (
          <div className="col-sm-3">
            <h3>{obj.title}</h3>
            <ScatterPlot
              session={props.session}
              data_key={obj.data_key}
              key={index}
              variable={obj.variable}
              trendX={obj.trendX}
              accessor={obj.accessor}
            />
          </div>
        ))}
        <div className="clear" />
      </div>
    </div>
  );
};

export default ScatterPlots;
