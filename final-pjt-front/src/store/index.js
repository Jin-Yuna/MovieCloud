import Vue from 'vue'
import Vuex from 'vuex'

import accounts from './modules/accounts'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    id: '',
    userName: '',
    platform: '',
  },
  mutations: {
    setUser(state, payload) {
      state.id = payload.id
      state.userName = payload.name
      state.platform = payload.platform
    }
  },
  modules: {  
    accounts,
  },
})
