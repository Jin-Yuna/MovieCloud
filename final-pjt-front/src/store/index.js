import Vue from 'vue'
import Vuex from 'vuex'

import accounts from './modules/accounts'
import drops from './modules/drops'
import createPersistedState from 'vuex-persistedstate';


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    latitude: 36.355560,
    longitude: 127.298388,
    temp: 0,
    city: '',
    weather_simple: '',
    weather_description: '', 
  },
  getters: {
  },
  mutations: {
    SET_LOCATION(state, loc) {
      state.latitude = loc.latitude
      state.longitude = loc.longitude
    },
    SET_WEATHER(state, weather) {
      state.weather_description = weather.weather_description
      state.weather_simple = weather.weather_simple
      state.city = weather.city
      state.temp = weather.temp
    }
  },
  actions: {
    saveLocation({ commit }, loc) {
      commit('SET_LOCATION', loc)
      localStorage.setItem('loc', loc)
    },
    saveWeather({ commit }, weather) {
      commit('SET_WEATHER', weather)
      localStorage.setItem('weather', weather)
    },
  },
  modules: {  
    accounts,
    drops,
  },
  //vuex plugin 명시 
  plugins: [createPersistedState()]

})
