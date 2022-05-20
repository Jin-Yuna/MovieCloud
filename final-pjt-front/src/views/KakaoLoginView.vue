<template>
  <div>
    <button @click="kakaoLogin"><img src="http://gi.esmplus.com/buybye1/page/kakao-login.png" style="height:60px;width:auto;"></button>
  </div>
</template>

<script>
  export default {
    name: 'KakaoLoginView',
    methods: {
      kakaoLogin() {
        const params = {
          redirectUri:'http://localhost:8080/',
        }
        window.Kakao.Auth.authorize(params)
      }
    },
  }
</script>

<style></style>
