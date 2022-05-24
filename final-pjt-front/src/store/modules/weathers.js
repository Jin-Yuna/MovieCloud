import drf from '@/api/drf'
import axios from 'axios'

export default {

  state: {
    weather_movies: [],
    weather_genres: {
        800: [12, 14, 28], // 800 맑은 날
        801: [16, 878, 36, 37],//  8801 구름 조금
        80: [35, 10402],  // 880x 구름 많음
        6: [18, 10751, 99],    // 86xx: Snow
        2: [80, 27, 9648, 53, 10752],  // 8Group 2xx: Thunderstorm
        7: [35, 10402], // 87xx: Atmosphere
        5: [10749, 10770],   // 8Group 3xx: Drizzle, Group 5xx: Rain
        3: [10749, 10770]
    },
    genres:{
      28: "Action",
      12: "Adventure",
      16:"Animation",
      35:"Comedy",
      80:"Crime",
      99:"Documentary",
      18:"Drama",
      10751:"Family",
      14:"Fantasy",
      36:"History",
      27:"Horror",
      10402:"Music",
      9648:"Mystery",
      10749: "Romance",
      878: "Science Fiction",
      10770:"TV Movie",
      53:"Thriller",
      10752:"War",
      37:"Western"}
  },
  getters: {
    weather_movies: state => state.weather_movies,
    weather_genres: state => state.weather_genres,
    genres: state => state.genres
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
