import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'


export default {
  state: {
    drop: {},
  },
  getters: {
    drop: state => state.drop
  },
  mutations: {
    SET_DROP: (state, drop) => state.drop = drop,
    SET_DROP_COMMENTS: (state, comments) => (state.drop.comments = comments),
  },
  actions: {
    createDrop({ commit, getters }, drop ) {
      axios({
        url: drf.drops.newDrop(),
        method: 'post',
        data: drop,
        headers: getters.authHeader,
      })
        .then(response => {
          commit('SET_DROP', response.data)
          router.push({
            name: 'DropListView'
          })
        })
        .catch(err=>{
          console.lpg(err)
          router.push('login')
        })
    },
    getDrop({ commit, getters }, dropPk) {
      axios({
        url: drf.drops.drop(dropPk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(response => {
          commit('SET_DROP', response.data)
        })
        .catch(error => {
          console.error(error.response)
          if (error.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
    updateDrop({ commit, getters }, { dropPk, title, content, user_vote, movie }) {
      axios({
        url: drf.drops.drop(dropPk),
        method: 'put',
        data: { title, content, user_vote, movie },
        headers: getters.authHeader,
      })
        .then(response => {
          commit('SET_DROP', response.data)
          router.push({
            name: 'DropDetailView',
            params: { dropPk: dropPk }
          })
        })
    },
    deleteDrop({ commit, getters }, dropPk) {  
      if (confirm('삭제하시겠습니까?')) {
        axios({
          url: drf.drops.drop(dropPk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_DROP', {})
            router.push({ name: 'DropListView' })
          })
          .catch(error => console.error(error.response))
      }
    },
    likeDrop({ commit, getters }, dropPk) {
      axios({
        url: drf.drops.likeDrop(dropPk),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(response => commit('SET_DROP', response.data))
        .catch(error => console.error(error.response))
    },
    createComment({ commit, getters }, { dropPk, content }) {
      const comment = { content }
      axios({
        url: drf.drops.comments(dropPk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(response => {
          commit('SET_DROP_COMMENTS', response.data)
        })
        .catch(error => console.error(error.response))
    },
    updateComment({ commit, getters }, payload ) {
      const comment = payload.content
      axios({
        url: drf.drops.comment(payload.dropPk, payload.commentPk),
        method: 'put',
        data: { content : comment },
        headers: getters.authHeader,
      })
        .then(response => {
          commit('SET_DROP_COMMENTS', response.data)
        })
        .catch(error => console.error(error.response))
    },
    deleteComment({ commit, getters }, payload ) {
      axios({
        url: drf.drops.comment(payload.dropPk, payload.commentPk),
        method: 'delete',
        headers: getters.authHeader,
      })
        .then(response => {
          commit('SET_DROP_COMMENTS', response.data)
        })
        .catch(error => console.error(error.response))
    },
  },
}
