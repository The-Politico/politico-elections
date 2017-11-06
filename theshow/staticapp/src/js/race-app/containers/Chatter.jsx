import React from 'react';

const Chatter = props => {
  const blocks = props.content.blocks;
  return blocks.chatter ? (
    <div 
      className="chatter row-fluid section" 
      dangerouslySetInnerHTML={{ __html: blocks.chatter }}>
    </div>
  ) : null;
};

export default Chatter;