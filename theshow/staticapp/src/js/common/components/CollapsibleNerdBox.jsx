import React from 'react';
import { Collapse } from 'react-collapse';
import ReactMarkdown from 'react-markdown';

class NerdBox extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      open: false,
    };
  }
  render(props, state) {
    const buttonText = state.open ?
      'Thanks, got it!' : 'How we made this';
    const buttonSymbol = state.open ? '-' : '+';
    return (
      <div className="collapsible-nerd-box">
        <button
          onClick={() => this.setState({ open: !state.open })}
          className={state.open ? 'open' : 'closed'}
        >
          {buttonText}
          <span className="float-right">{buttonSymbol}</span>
        </button>
        <Collapse
          isOpened={state.open}
        >
          <div className="footnote">
            <ReactMarkdown source={props.note} />
          </div>
        </Collapse>
      </div>
    );
  }
}

export default NerdBox;
