import React from 'react';
import { render } from 'react-dom';
// import { Provider } from 'react-redux';

import App from './race-app/containers/App';
// import store from './board-app/stores/';

import '../scss/main.scss';


const RaceApp = () => (
  // <Provider store={store}>
  <App />
  // </Provider>
);

render(
  <RaceApp />,
  document.getElementById('app'),
);
