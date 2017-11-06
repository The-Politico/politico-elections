import React from 'react';

import CensusMap from '../components/CensusMap';


const CensusMaps = (props) => {
  const censusVariables = [
    {
      variable: 'B03002',
      data_key: 'white_alone',
      title: 'Percent of minority (nonwhite) people',
      accessor: d => ((d.total - d.white_alone) / d.total) * 100,
    },
    {
      variable: 'B15003',
      data_key: 'college_educated',
      title: 'Percent of college educated people',
      accessor: d => (d.college_educated / d.total) * 100,
    },
    {
      variable: 'B19001',
      data_key: 'middle_class',
      title: 'Percent of middle class people',
      accessor: d => (d.middle_class / d.total) * 100,
    },
    {
      variable: 'B17020',
      data_key: 'impoverished',
      title: 'Percent of people below the poverty line',
      accessor: d => (d.impoverished / d.total) * 100,
    },
  ];

  return (
    <div className="census-maps content-extra-large row-fluid section">
      <div className="section-header-wrap">
        <div className="header-line" />
        <h2 className="section-title">Who lives where?</h2>
      </div>
      <div className="chatter">
        <p>These maps use U.S. Census Bureau data to show where
        in the state each of several key demographic groups is most
        concentrated.
        </p>
      </div>
      {censusVariables.map((obj, index) => (
        <div className="col-sm-6 census-map">
          <h3 className="census-map-title">{obj.title}</h3>
          <CensusMap
            session={props.session}
            variable={obj.variable}
            data_key={obj.data_key}
            key={index}
            title={obj.title}
            accessor={obj.accessor}
          />
        </div>
      ))}
      <div className="clear" />
    </div>
  );
};

export default CensusMaps;
