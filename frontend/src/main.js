import Vue from 'vue'
import App from './App.vue'
import vuetify from '@/plugins/vuetify'
import router from "./router";
import store from './store'
import './assets/css/main.css';
import axios from 'axios'
import PerfectScrollbar from 'vue2-perfect-scrollbar'
import 'vue2-perfect-scrollbar/dist/vue2-perfect-scrollbar.css'
Vue.config.productionTip = false
require('@/store/subscriber')
Vue.use(PerfectScrollbar)
// axios.defaults.baseURL = '/api/'
axios.defaults.baseURL = process.env.VUE_APP_API_ENDPOINT
console.log(process.env.VUE_APP_API_ENDPOINT)

require('./assets/css/main.css');
store.dispatch('auth/attempt', localStorage.getItem('token')).then(() => {
  new Vue({
    render: h => h(App),
    vuetify,
    router,
    store,
  }).$mount('#app')   
  
})
