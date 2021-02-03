import Vue from 'vue'
import App from './App.vue'
import vuetify from '@/plugins/vuetify'
import router from "./router";
import store from './store'
import axios from 'axios'
import PerfectScrollbar from 'vue2-perfect-scrollbar'
import 'vue2-perfect-scrollbar/dist/vue2-perfect-scrollbar.css'
Vue.config.productionTip = false
require('@/store/subscriber')
Vue.use(PerfectScrollbar)
// axios.defaults.baseURL = '/api/'
// axios.defaults.baseURL =  process.env.VUE_APP_API_HOST
axios.defaults.baseURL = 'http://'+ process.env.VUE_APP_API_ENDPOINT+':8000/'
// axios.defaults.baseURL = 'http://localhost:8080/api/'
// axios.defaults.baseURL = 'https://lex.dioe.at/api/'
// axios.defaults.baseURL = backend
axios.defaults.headers['Access-Control-Allow-Origin'] = '*'
axios.defaults.headers['Access-Control-Allow-Credentials'] = true
// axios.defaults.headers['Accept'] = 'application/json, text/plain, */*'
// axios.defaults.headers['Access-Control-Allow-Methods'] = 'GET, PUT, POST, DELETE, OPTIONS'


store.dispatch('auth/attempt', localStorage.getItem('token')).then(() => {
  new Vue({
    render: h => h(App),
    vuetify,
    router,
    store,
  }).$mount('#app')   
  
})
