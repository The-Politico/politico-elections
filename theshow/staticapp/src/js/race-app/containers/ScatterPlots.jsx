import React from 'react';

import ScatterPlot from '../components/ScatterPlot';

const ScatterPlots = (props) => {
  const censusVariables = [
    {
      variable: 'B03002',
      data_key: 'white_alone',
      trendX: 'minority',
      title: 'Minority (nonwhite)',
      accessor: d => ((d.total - d.white_alone) / d.total),
    },
    {
      variable: 'B15003',
      data_key: 'college_educated',
      trendX: 'educated',
      title: 'Education',
      accessor: d => d.college_educated / d.total,
    },
    {
      variable: 'B19001',
      data_key: 'middle_class',
      trendX: 'middle class',
      title: 'Middle class',
      accessor: d => d.middle_class / d.total,
    },
    {
      variable: 'B17020',
      data_key: 'impoverished',
      trendX: 'impoverished',
      title: 'Below the poverty line',
      accessor: d => d.impoverished / d.total,
    },
  ];
  return (
    <div className="scatter-plots row-fluid section content-extra-extra-large">
    <div class="section-header-wrap"><div class="header-line"></div><h2 class="section-title">Voting block trends</h2></div>
    <div class="plot-container">
      {censusVariables.map((obj, index) => {
        return (<div className="col-sm-3">
          <h3>{obj.title}</h3>
          <ScatterPlot
            session={props.session}
            data_key={obj.data_key}
            key={index}
            variable={obj.variable}
            trendX={obj.trendX}
            accessor={obj.accessor}
          />
        </div>)
      })}

      <div class="clear"></div>
      </div>
    </div>
  );
};

export default ScatterPlots;
