import React from 'react';

import ScatterPlot from '../components/ScatterPlot';

const ScatterPlots = (props) => {
  const censusVariables = [
    {
      variable: 'B03002',
      data_key: 'white_alone',
      trendX: 'minority',
      title: 'Minority (nonwhite)',
    },
    {
      variable: 'B15003',
      data_key: 'college_educated',
      trendX: 'educated',
      title: 'Education',
    },
    {
      variable: 'B19001',
      data_key: 'middle_class',
      trendX: 'middle class',
      title: 'Middle class',
    },
    {
      variable: 'B17020',
      data_key: 'impoverished',
      trendX: 'impoverished',
      title: 'Below the poverty line'
    },
  ];
  return (
    <div className="scatter-plots row-fluid section content-extra-extra-large">
    <h2>Where did different voting blocks land? </h2>
    <p class="sans">
      <strong>Each dot respresents a county.</strong> The further left the dot the more Democratic the county voted, the futher right, the more Republican. The closer to the top of the chart the more the county identifies with the census group. The top line shows how strong of a predictor TK.
    </p>
      {censusVariables.map((obj, index) => {
        return (<div className="col-sm-3">
          <h3>{obj.title}</h3>
          <ScatterPlot
            session={props.session}
            data_key={obj.data_key}
            key={index}
            variable={obj.variable}
            trendX={obj.trendX}
          />
        </div>)
      })}

      <div class="clear"></div>
    </div>
  );
};

export default ScatterPlots;
