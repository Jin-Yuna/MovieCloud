<template>
  <div>
    <h1>Logout</h1>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    methods: {
      ...mapActions(['logout'])
    },
    computed: {
      ...mapGetters(['isLoggedIn', 'profile'])
    },
    created() {
      if(this.profile.nickname) {
        this.$store.dispatch('removeToken')
        alert('성공적으로 logout!')
        this.$router.push({ name: 'login' })
      }
      else {
        if (this.isLoggedIn) {
          this.logout()
        } else {
          alert('잘못된 접근')
          this.$router.back()
        }
      }
    },
  }
</script>

<style></style>
