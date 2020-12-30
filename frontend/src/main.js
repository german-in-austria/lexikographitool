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
axios.defaults.baseURL = 'http://localhost:8000/'
store.dispatch('auth/attempt', localStorage.getItem('token')).then(() => {
  new Vue({
    render: h => h(App),
    vuetify,
    router,
    store
  }).$mount('#app')   
  
})
