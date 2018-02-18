const webpack = require('webpack')
const path = require('path')
const ExtractTextPlugin = require('extract-text-webpack-plugin')
const CopyWebpackPlugin = require('copy-webpack-plugin')
const BundleTracker = require('webpack-bundle-tracker')
const CleanWebpackPlugin = require('clean-webpack-plugin')

const inProduction = 'production' === process.env.NODE_ENV
const buildPath = path.resolve(__dirname, '.build/')

module.exports = {
  entry: {
    styles: './assets/sass/app.scss',
    fonts: './assets/sass/fonts.scss',
    app: './entries/app.js',
    vendor: [
      'react', 'react-dom', 'react-redux', 'redux-thunk', 'immutable',
      'js-cookie', 'isomorphic-fetch',
    ],
  },

  devtool: inProduction ? 'source-map' : 'eval-source-map',

  output: {
    path: buildPath,
    filename: './bundles/[name]-[hash].js',
  },

  plugins: [
    new CleanWebpackPlugin(['.build']),
    new webpack.optimize.CommonsChunkPlugin({name: 'vendor'}),
    new BundleTracker({filename: './webpack-stats.json'}),
    new ExtractTextPlugin({
      filename: `css/[name]-[hash].css`,
      allChunks: true,
    }),
    new CopyWebpackPlugin([
      {
        from: 'assets/fonts/',
        to: `${buildPath}/fonts/`,
      },
    ]),
  ],

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: [/node_modules/],
        use: [{
          loader: 'babel-loader',
        }],
      },
      {
        test: /\.scss$/,
        exclude: [/node_modules/],
        use: ExtractTextPlugin.extract({
          use: [
            {
              loader: 'css-loader',
              options: {
                url: false,
              },
            },
            {
              loader: 'sass-loader',
              options: {
                //includePaths: ['node_modules/bootstrap/scss/'],
                outputStyle: 'compressed',
              },
            }
          ],
          fallback: 'style-loader',
        }),
      },
    ],
  },
}
