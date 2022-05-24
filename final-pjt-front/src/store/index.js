import Vue from 'vue'
import Vuex from 'vuex'

import accounts from './modules/accounts'
import drops from './modules/drops'
import movies from './modules/movies'
import weathers from './modules/weathers'

import createPersistedState from 'vuex-persistedstate';


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    location: {
      latitude: 36.355560,
      longitude: 127.298388,
      city: '',
    },
    weather: {
      weather_id: '',
      weather_simple: '',
      weather_description: '', 
      temp: 0,
    }
  },
  getters: {
    location: state => state.location,
    weather: state => state.weather,
  },
  mutations: {
    SET_LOCATION(state, loc) {
      state.location.latitude = loc.latitude
      state.location.longitude = loc.longitude
    },
    SET_WEATHER(state, weather) {
      state.weather.weather_description = weather.weather_description
      state.weather.weather_simple = weather.weather_simple
      state.location.city = weather.city
      state.weather.temp = weather.temp
      state.weather.weather_id = weather.weather_id
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
    weathers,
    movies,
  },
  //vuex plugin 명시 
  plugins: [createPersistedState()]

})
