const gulp = require('gulp');
const spawn = require('child_process').spawn;
const webpack = require('webpack');
const prodConfig = require('../../webpack-prod.config.js');
const webpackStream = require('webpack-stream');

module.exports = (cb) =>
  gulp.src('src/js/main.js')
    .pipe(webpackStream(prodConfig, webpack))
    .pipe(gulp.dest('./../static/theshow/'));
    // Eliminating this for now in favor of calling from Python mgmtcmd
    // .on('end', () => {
    //   const publish = spawn('python', ['../../manage.py', 'publish_statics'])
    //   publish.stdout.on('data', (data) => {
    //     console.log(`stdout: ${data}`);
    //   });
    //   publish.stderr.on('data', (data) => {
    //     console.log(`stderr: ${data}`);
    //   });
    //   publish.on('close', (code, signal) => {
    //     process.exit();
    //   });
    // });
