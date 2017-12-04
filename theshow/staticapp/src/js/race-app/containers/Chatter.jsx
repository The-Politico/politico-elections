import React from 'react';

const Chatter = props => {
  const blocks = props.content.page;
  return blocks.chatter ? (
    <div 
      className="chatter row-fluid section" 
      dangerouslySetInnerHTML={{ __html: blocks.chatter }}>
    </div>
  ) : null;
};

export default Chatter;