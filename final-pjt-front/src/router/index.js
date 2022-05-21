import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from '../store'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import KakaoLoginView from '@/views/KakaoLoginView.vue'

import NotFound404 from '../views/NotFound404.vue'

import DropListView from '@/views/DropListView.vue'

Vue.use(VueRouter)

const routes = [
  /*
  intro
    / => StartView.vue

  accounts
    /login => LoginView - AccountErrorList
    /logout => LogoutView 
    /signup => SignupView - AccountErrorList
    /kakaoLogin => KakaoLoginView - login.js
    
  movie
    /movies => MovieView - WeatherList, BoxOfficeList - SimpleMovieCard / Map, UserBasedList - BasicMovieCard / MovieDropList - DropCard
    /movies/:moviePk => MovieDetailView - DropCard
    /movies/weather => MovieWeatherView - MovieWeatherCard
    /movies/boxoffice => MovieBoxofficeView - MapDetail, BoxOfficeList - BoxOfficeMovieCard
  
  cloud
    /cloud/:username => CloudView - Profile, CloudDropList - Dropcard
    /drops/new => DropNewView - DropCreate (DropForm)
    /drops/:dropPk => DropDetailView - CommentListForm, CommentListItem
    /drops/:dropPk/edit => DropEditView - DropCreate (DropForm)

    /404 => NotFound404
    * => /404
  */

  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/kakaoLogin',
    name: 'kakaoLogin',
    component: KakaoLoginView
  },
  { 
    path: '/drops',
    name: 'DropList',
    component: DropListView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  // {
  //   path: '*',
  //   redirect: '/404'
  // },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})


// router.beforeEach((to, from, next) => {
//   // 이전 페이지에서 발생한 에러메시지 삭제
//   store.commit('SET_AUTH_ERROR', null)

//   const { isLoggedIn } = store.getters

//   const noAuthPages = ['login', 'signup', 'kakaoLogin']

//   const isAuthRequired = !noAuthPages.includes(to.name)

//   if (isAuthRequired && !isLoggedIn) {
//     alert('Require Login. Redirecting..')
//     next({ name: 'login' })
//   } else {
//     next()
//   }

// })

export default router
