import axios from 'axios'

export default {
  state: {
    today: '',
    boxOffie: [],
  },
  getters: {

  },
  mutations: {
    GET_TODAY({state}) {
      // yyyymmdd
      const nowDay = new Date()
      const year = nowDay.getFullYear()
      const month = ('0' + nowDay.getMonth() + 1).slice(-2)
      const day = ('0' + nowDay.getDate()).slice(-2)
      state.today = year + month + day
      console.log(state.day)
    }
  },
  actions: {
    getBoxOffice({commit}) {
      commit('GET_TODAY')
      console.log(commit)
      // const BoxOfficeURL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
      // const config = {
      //   params: {
      //     key: process.env.BOX_OFFICE_API_KEY,
      //     part: 'snippet',
      //     type: 'Trailer',
      //     q: this.inputValue
        // }
      // }
    }
  },
}
