import axios from 'axios'
import _ from 'lodash'

import drf from '@/api/drf'
import router from '@/router'


export default {
  state: {
    drop: {},
  },
  getters: {
    drop: state => state.drop,
    // isAuthor 안됨
    isAuthor: (state, getters) => {
      return state.drop.user.username === getters.accounts.currentUser.username
    },
    isDrop: state => !_.isEmpty(state.drops.drop),
  },
  mutations: {
    SET_DROP: (state, drop) => state.drop = drop,
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
          console.log(drop)
          router.push({
            name: 'DropListView',
          })
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
      /* 게시글 수정
      PUT: drop URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.drop에 저장
          dropDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
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
  },
}
