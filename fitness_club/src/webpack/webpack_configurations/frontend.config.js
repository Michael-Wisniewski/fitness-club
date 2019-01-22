const staticRoot = '/fitness_club/static';
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const TerserPlugin = require('terser-webpack-plugin');
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const webpack = require("webpack");

module.exports = {
    entry: {
        'base_templates/frontendBase': './src/base_templates/frontend.js',
        'blog/blog': './src/blog/blog.js',
        'landing_page/landing_page': './src/landing_page/landing_page.js'
    },
    output: {
        path: staticRoot,
		filename: "[name].bundle.js"
    },
    optimization: {
        minimizer: [
            new TerserPlugin({
                cache: true,
                parallel: true,
                sourceMap: true,
                extractComments: {
                    condition: /^\**!|@preserve|@license|@cc_on/i,
                    filename: function(file) {
                        return `${file.slice(0,-10)}.LICENSE`;
                    },
                    banner: function(licenseFile) {
                        return `\tLicense information can be found in:\nhttp://fitness.pl/static/${licenseFile}`;
                    }
                }
            }),
            new OptimizeCSSAssetsPlugin({})
        ]
    },
    module: {
        rules: [
            {
                test: /\.css$/, 
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader'
                ]
            },
            {
                test: /\.scss$/, 
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'postcss-loader',
                    'sass-loader'
                ]
            },
            {
                test: /\.(svg|eot|ttf|woff|woff2)?$/, 
                use: [{
                    loader: 'file-loader',
                    options: {
                        name: 'frontEndBase.bundle.[ext]',
                        outputPath: 'base_templates/',
                        publicPath: '/static/base_templates/'
                    }
                }] 
            }
        ]
    },
    plugins: [      
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            Util: 'exports-loader?Util!bootstrap/js/dist/util'
        }),
        new MiniCssExtractPlugin({
            filename: "[name].bundle.css"
        })
    ]
}