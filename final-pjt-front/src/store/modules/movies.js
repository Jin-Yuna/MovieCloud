import axios from 'axios'

export default {
  state: {
    today: '',
    boxOffie: [],
  },
  getters: {

  },
  mutations: {
    GET_TODAY(state, newToday ) {
      state.today = newToday
    } 
  },
  actions: {
    getToday({ commit }) {
      console.log('실행')
      const nowDay = new Date()
      const year = nowDay.getFullYear()
      const month = ('0' + nowDay.getMonth() + 1).slice(-2)
      const day = ('0' + nowDay.getDate()).slice(-2)
      const newToday = year + month + day
      commit('GET_TODAY', newToday )
    },
  },
}
