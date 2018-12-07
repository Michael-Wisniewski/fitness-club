const staticRoot = '/fitness_club/static';
const ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
    entry: {
        'blog/posts_list/posts_list': './src/blog/posts_list/posts_list.js'
    },
    output: {
        path: staticRoot,
		filename: "[name].bunle.js"
    },
    module: {
        rules: [
            {
                test: /\.css$/, 
                use: ExtractTextPlugin.extract({
                    fallback: 'style-loader', 
                    use: 'css-loader',
                    publicPath: staticRoot})
            },
            {
                test: /\.scss$/, 
                use: ExtractTextPlugin.extract({
                    fallback: 'style-loader', 
                    use: ['css-loader', 'sass-loader'],
                    publicPath: staticRoot})
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin({
            filename: "[name].bunle.css",
            disable: true,
            allChunks: true
        }),
    ]
}