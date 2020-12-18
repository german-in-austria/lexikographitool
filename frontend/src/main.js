import Vue from 'vue'
import App from './App.vue'
import vuetify from '@/plugins/vuetify'
import router from "./router";
import store from './store'
import axios from 'axios'
Vue.config.productionTip = false
require('@/store/subscriber')

axios.defaults.baseURL = 'http://localhost:8000/'
store.dispatch('auth/attempt', localStorage.getItem('token')).then(() => {
  new Vue({
    render: h => h(App),
    vuetify,
    router,
    store,
  }).$mount('#app')

})
