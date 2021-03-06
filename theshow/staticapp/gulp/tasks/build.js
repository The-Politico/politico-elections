const gulp = require('gulp');
const spawn = require('child_process').spawn;
const webpack = require('webpack');
const prodConfig = require('../../webpack-prod.config.js');
const webpackStream = require('webpack-stream');

module.exports = (cb) =>
  gulp.src('src/js/main.js')
    .pipe(webpackStream(prodConfig, webpack))
    .pipe(gulp.dest('./../static/theshow/'));
