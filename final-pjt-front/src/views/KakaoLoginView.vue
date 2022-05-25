<template>
<div></div>
</template>

<script>
import { getKakaoToken } from '@/services/login'
import axios from 'axios'

export default {
  name: 'KakaoLoginView',
  created() {
      if (this.$route.query.code) {
        this.setKakaoToken();
      }
    },
  methods: {
    async setKakaoToken () {
      // 카카오 인증 코드
      const { data } = await getKakaoToken(this.$route.query.code);
      if (data.error) {
          alert('카카오톡 로그인 오류입니다.');
          this.$router.replace('/login');
          return;
      }
      console.log(data)
      window.Kakao.Auth.setAccessToken(data.access_token);
      this.$cookies.set('access-token', data.access_token, '1d');
      this.$cookies.set('refresh-token', data.refresh_token, '1d');
      const token_header = {
            'Token': data.access_token,
            'code': this.$route.query.code,
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json; charset = utf-8'
      }
      axios.get('/kakaoLogin/', { headers: token_header })
        .then(response => {
          console.log(response)
          const token = response.data.key

          this.$store.dispatch('saveToken', token)
          this.$store.dispatch('fetchCurrentUser')
          this.$router.push({ name: 'MovieHome' })
        })
    },
  }
}

</script>