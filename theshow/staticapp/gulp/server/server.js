const path = require('path');
const fs = require('fs-extra');
const open = require('open');
const express = require('express');
const webpack = require('webpack');
const webpackMiddleware = require('webpack-dev-middleware');
const webpackHotMiddleware = require('webpack-hot-middleware');
const webpackConfig = require('../../webpack-dev.config.js');
const proxyProc = require('express-http-proxy');

const app = express();

module.exports = {
  startServer: (port, proxy) => {
    const compiler = webpack(webpackConfig(port));
    const middleware = webpackMiddleware(compiler, {
      publicPath: '/static/theshow/',
      stats: {
        colors: true,
      },
    });
    app.use(middleware);
    app.use(webpackHotMiddleware(compiler));
    app.use('/', proxyProc(`localhost:${proxy}`));

    app.listen(port, function() {
      app.keepAliveTimeout = 0;
    })

    middleware.waitUntilValid(() => {
      console.log(`app started on port ${port}`);
      open(`http://localhost:${port}`);
    });
  },
}
