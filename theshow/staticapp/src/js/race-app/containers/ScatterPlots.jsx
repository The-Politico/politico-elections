import React from 'react';

import ScatterPlot from '../components/ScatterPlot';
import NerdBox from '../../common/components/CollapsibleNerdBox';

const ScatterPlots = (props) => {
  const censusVariables = [
    {
      variable: 'B03002',
      data_key: 'white_alone',
      trendX: 'minority',
      title: 'Minority (nonwhite) population',
      accessor: d => ((d.total - d.white_alone) / d.total),
    },
    {
      variable: 'B15003',
      data_key: 'college_educated',
      trendX: 'educated',
      title: 'College educated population',
      accessor: d => d.college_educated / d.total,
    },
    {
      variable: 'B19001',
      data_key: 'middle_class',
      trendX: 'middle class',
      title: 'Middle class population',
      accessor: d => d.middle_class / d.total,
    },
    {
      variable: 'B17020',
      data_key: 'impoverished',
      trendX: 'impoverished',
      title: 'Population below the poverty line',
      accessor: d => d.impoverished / d.total,
    },
  ];
  return (
    <div className="scatter-plots row-fluid section content-extra-extra-large">
      <div className="section-header-wrap">
        <div className="header-line" />
        <h2 className="section-title">Voting bloc trends</h2>
      </div>
      <div className="chatter">
        <p>
        Which voting blocs track closest with a party line? These charts use
        county-level data from the U.S. Census Bureau to estimate how effectively
        each party pulls votes from key demographic groups. The
        sliding scale tells you how strong the relationship was in this
        election, while the scatter-plot charts show which party benefited most from
        that group’s support. Each dot is a county that will update as votes come in.
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
        <NerdBox
          note="
          These charts show the relationship between the percentage of the population in
          each county that identifies
          with a demographic characteristic (minority, college-educated, etc.) and
          the split of that county&rsquo;s vote
          between the Democratic and Republican candidate (GOP 45% - Dem. 40% = GOP +5).
          The relationship with party vote shows the value of the&nbsp;
          [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient),
          which is a statistic that measures the correlation
          between that demographic
          value and the vote split. We take the absolute value of
          that number -- which is always between -1 and 1 and strongest at both ends --
          to show how strong the relationship is,
          regardless of whether it&rsquo;s positive or negative. Our demographic data
          come from the latest U.S. Census American Community Survey. We use total
          population estimates as a proxy for the voting-age population that actually
          turns out on Election Day, so, political strategists, take these stats
          with a pinch of salt. 😊 🇺🇸
          "
        />
        <div className="clear" />
      </div>
    </div>
  );
};

export default ScatterPlots;
