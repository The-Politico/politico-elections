import React from 'react';
import { render } from 'react-dom';
// import { Provider } from 'react-redux';
import orm from './race-app/models/'
import App from './race-app/containers/App';
import store from './race-app/stores/';

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
