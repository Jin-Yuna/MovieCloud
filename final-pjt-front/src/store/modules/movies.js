import axios from "axios"
import router from '@/router'

export default {
  state: {
    today: '',
    boxOffie: null,
    movieId: 0,
    movieDetailAxios: null,
    movies_title: [],
  },
  getters: {

  },
  mutations: {
    GET_TODAY(state, newToday ) {
      state.today = newToday
    },
    GET_MOVIE_DETAIL_AXIOS(state, movieDetailAxios) {
      state.movieDetailAxios = movieDetailAxios
    },
    SET_MOVIE_ID(state, movieId) {
      state.movieId = movieId
    },
    GET_BOX_OFFICE(state, boxOffie) {
      state.boxOffie = boxOffie
    },
    SET_MOVIES_TITLE(state, movies_title) {
      state.movies_title = movies_title
    }
  },
  actions: {
    getToday({ commit }) {
      const nowDay = new Date()
      const year = nowDay.getFullYear()
      const month = ('0' + nowDay.getMonth() + 1).slice(-2)
      const day = ('0' + nowDay.getDate()).slice(-2)
      const newToday = year + month + day
      commit('GET_TODAY', newToday )
    },
    getBoxOffice ({commit, state}) {
      const BoxOfficeURL ='http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
      const config = {
        params: {
          key: process.env.VUE_APP_BOX_OFFICE_API_KEY,
          targetDt: state.today,
        }
      }
      axios.get(BoxOfficeURL, config)
        .then(response => {
          commit('GET_BOX_OFFICE', response.data.boxOfficeResult.dailyBoxOfficeList)
        })
    },
    getMovieDetailAxios({ commit, dispatch }, movieId) {
      const config = {
        params: {
          'api_key': process.env.VUE_APP_TMDB_API_KEY,
          'language': 'ko-KR'
        }
      }
      const TMDB_DETAIL_URL = `https://api.themoviedb.org/3/movie/${movieId}`
      axios.get(TMDB_DETAIL_URL, config)
        .then(response => {
          commit('GET_MOVIE_DETAIL_AXIOS', response.data)
          dispatch('SET_MOVIE_ID', movieId)
          router.push({
            name: 'MovieDetail',
            params: { moviePk: movieId }
          })
        })
    },
    setMoviesTitle({ commit, state }) {
      if (!state.movies_title.length) {
        axios.get('http://127.0.0.1:8000/movies/get_movie_title/')
          .then(response => {
          // const movies_title = response.data
          // movie_id와 title 가져옴
          commit('SET_MOVIES_TITLE', response.data)
      })
      }
    }
  },
}
