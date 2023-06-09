import Vue from 'vue'
import VueCookies from 'vue-cookies'

import App from './App.vue'
import router from './router'
import store from './store'

import VueCompositionApi from '@vue/composition-api';
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

Vue.use(VueCompositionApi);
Vue.use(VueCookies)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')

window.Kakao.init(process.env.VUE_APP_KAKAO_JAVASCRIPT_API_KEY)
