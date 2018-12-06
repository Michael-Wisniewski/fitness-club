const ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
    entry: {
        'blog/posts_list/posts_list': './src/blog/posts_list/posts_list.js'
    },
    output: {
        path: '/fitness_club/static',
		filename: "[name].bunle.js"
    },
    module: {
        rules: [
            {
                test: /\.css$/, 
                use: ExtractTextPlugin.extract({
                    fallback: 'style-loader', 
                    use: 'css-loader',
                    publicPath: '/fitness_club/static'})
            },
            {
                test: /\.scss$/, 
                use: ExtractTextPlugin.extract({
                    fallback: 'style-loader', 
                    use: ['css-loader', 'sass-loader'],
                    publicPath: '/fitness_club/static'})
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin({
            filename: "[name].bunle.css",
            disable: false,
            allChunks: true
        }),
    ]
}