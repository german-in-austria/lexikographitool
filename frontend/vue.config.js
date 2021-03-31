// vue.config.js
module.exports = {
    runtimeCompiler:true,
    devServer: {
        proxy: {
            '/api': {
                target: process.env.VUE_APP_API_ENDPOINT,
                pathRewrite: {'^/api': ''},
            },
        },
    },
}