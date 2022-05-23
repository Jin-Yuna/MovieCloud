import drf from '@/api/drf'
import axios from 'axios'

export default {
  state: {
    weather_movies: {},
  },
  getters: {
    weather_movies: state => state.weather_movies

  },
  mutations: {
    SET_WEATHER_MOVIES: (state, movies) => state.weather_movies = movies
  },
  actions: {
    get_weather_movies({ commit }, id) {
      axios({
        url: drf.weathers.weather(id),
        methods: 'get',
      })
        .then(res => {
          const movies = res.data
          commit('SET_WEATHER_MOVIES', movies)
        })
    }
  },
}
