<template>
  <div></div>
</template>

<script>
import { getKakaoToken } from '@/services/login'

export default {
  created() {
      if (this.$route.query.code) {
        this.setKakaoToken();
      }
    },
  methods: {
    async setKakaoToken () {
        console.log('카카오 인증 코드', this.$route.query.code);
        const { data } = await getKakaoToken(this.$route.query.code);
        if (data.error) {
            alert('카카오톡 로그인 오류입니다.');
            this.$router.replace('/login');
            return;
        }
    },
  }
}
</script>

<style>

</style>