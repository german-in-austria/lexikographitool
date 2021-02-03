// // vue.config.js
// module.exports = {
//     devServer: {
//         proxy: {
//             '/api': {
//                 target:'http://'+ process.env.VUE_APP_API_ENDPOINT+':8000/',
//                 pathRewrite: { '^/api': '' },
//             },
//         }
// }}