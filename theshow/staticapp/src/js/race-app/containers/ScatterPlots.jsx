import React from 'react';

import ScatterPlot from '../components/ScatterPlot';

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
    trend: 'impoverished',
    title: 'Below the poverty line'
  },
];

const ScatterPlots = (props) => {
  return (
    <div className="scatter-plots row-fluid section content-extra-extra-large">
      <h2>How these groups voted</h2>
      <p class="sans">
        We probably want some chatter to help orient you to these charts. Robo text saying, <strong>nonwhite voters skewed TK</strong>, voters with <strong>high levels of education tk</strong>.
      </p>
      {censusVariables.map((obj, index) => {
        return (<div className="bar col-sm-3">
          <h3>{obj.title}</h3>
          <ScatterPlot 
            session={props.session}
            data_key={obj.data_key}
            key={index}
            variable={obj.variable}
          />
        </div>)
      })}
      <div class="clear"></div>
    </div>
  );
};

export default ScatterPlots;
  