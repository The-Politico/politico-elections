import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import Dateline from 'dateline';
import App from './race-app/containers/App';
import store from './race-app/stores/';

import '../scss/main.scss';

const RaceApp = () => (
  <Provider store={store}>
    <App />
  </Provider>
);

render(
  <RaceApp />,
  document.getElementById('app'),
);

const lastUpdated = document.querySelector('.live-results span.red');

function getLastUpdated() {
  fetch(window.appConfig.api.lastUpdated).then(response => response.json()).then((data) => {
    const date = new Date(data.date);
    const APDate = Dateline(date);
    const dateStr = `${APDate.getAPDate()}, ${APDate.getAPTime({ includeMinutes: true })} EST`;

    lastUpdated.textContent = dateStr;
  });
}

getLastUpdated();
setInterval(getLastUpdated, 5000);
