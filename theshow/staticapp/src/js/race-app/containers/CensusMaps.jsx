import React from 'react';

import CensusMap from '../components/CensusMap';


const CensusMaps = (props) => {
  const censusVariables = [
    {
      variable: 'B03002',
      data_key: 'white_alone',
      title: 'Minority (nonwhite)',
      accessor: d => ((d.total - d.white_alone) / d.total) * 100,
    },
    {
      variable: 'B15003',
      data_key: 'college_educated',
      title: 'Education',
      accessor: d => (d.college_educated / d.total) * 100,
    },
    {
      variable: 'B19001',
      data_key: 'middle_class',
      title: 'Middle class',
      accessor: d => (d.middle_class / d.total) * 100,
    },
    {
      variable: 'B17020',
      data_key: 'impoverished',
      title: 'Below the poverty line',
      accessor: d => (d.impoverished / d.total) * 100,
    },
  ]

  return (
    <div className="census-maps content-extra-large row-fluid section">
    <div class="section-header-wrap"><div class="header-line"></div><h2 class="section-title">Who lives where?</h2></div>
      {censusVariables.map((obj, index) => {
        return (<div className="col-sm-6 census-map">
          <h3 class="census-map-title">{obj.title}</h3>
          <CensusMap
            session={props.session}
            variable={obj.variable}
            data_key={obj.data_key}
            title={obj.title}
            accessor={obj.accessor}
          />
        </div>)
      })}

      <div class="clear"></div>
    </div>
  );
};

export default CensusMaps;
