<template>
  <div>
    <h1>Login</h1>
    <account-error-list v-if="authError"></account-error-list>
    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">username: </label>
        <input v-model="credentials.username" type="text" id="username" required />
      </div>
      <div>
        <label for="password">password: </label>
        <input v-model="credentials.password" type="password" id="password" required />
      </div>
      <button>Login</button>
    </form>
    <div>
    <button @click="kakaoLogin"><img src="http://gi.esmplus.com/buybye1/page/kakao-login.png" style="height:60px;width:auto;"></button>
  </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login']),
      kakaoLogin() {
        const params = {
          redirectUri:'http://localhost:8080/kakaoLogin',
        }
        window.Kakao.Auth.authorize(params)
      }
    },
  }
</script>

<style></style>
