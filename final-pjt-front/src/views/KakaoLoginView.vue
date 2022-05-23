<template>
<div></div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'KakaoLoginView',
  data() {
      return {
        userPk: Number(this.$route.params.kakaoPk),
        userdata: null,
      }
    },
  created() {
    this.Userdataget()
  },
  methods: {
    Userdataget() {
      axios.get(`http://127.0.0.1:8000/kakao_user_info/${this.userPk}/`)
        .then(response => {
          // this.userdata => 현재 유저 정보 
          this.userdata = response.data
          const token = this.userdata.password
          this.$store.dispatch('saveToken', token)
          this.$store.commit('SET_CURRENT_USER', this.userdata)
          this.$store.commit('SET_PROFILE', this.userdata)
          this.$router.push('/movies')
          })
    }
  }
}

</script>