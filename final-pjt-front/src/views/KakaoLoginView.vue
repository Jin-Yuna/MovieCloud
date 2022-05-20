<template>
  <div>
    <button @click="kakaoLogin()" >카카오 로그인</button>
  </div>
</template>

<script>
  
  export default {
    name: 'KakaoLoginView',
    data() {
    },
    methods: {
      kakaoLogin() {
        const CLIENT_ID = "683d19aa3f66f6c7d4ca3b08f6f139ed";
        const REDIRECT_URI =  "http://localhost:8080/accounts/kakaoLogin";

        const KAKAO_AUTH_URL = `https://kauth.kakao.com/oauth/authorize?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=code`;
        
        window.location.href = KAKAO_AUTH_URL
      }
    },
  }
</script>

<style></style>
