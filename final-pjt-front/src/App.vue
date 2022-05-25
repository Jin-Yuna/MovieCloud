<template>
  <v-app>
    <NavBar></NavBar>
    <hr />
    <router-view></router-view>
  </v-app>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'
  import { mapActions } from 'vuex'

  export default {
    name: 'App',
    components: { NavBar },
    created() {
      this.fetchCurrentUser()
      this.geofind()
    },
    methods: {
      ...mapActions(['fetchCurrentUser']),
    geofind() {
      if(!("geolocation" in navigator)) {
        this.textContent = 'Geolocation is not available.';
        return;
      }
      this.textContent = 'Locating...'
      
      // get position
      navigator.geolocation.getCurrentPosition(pos => {
      const loc = {
        latitude: pos.coords.latitude,
        longitude: pos.coords.longitude,
      }
      
      this.$store.dispatch('saveLocation', loc)
      // console.log(this.$store.state.latitude)

      }, err => {
      this.textContent = err.message;
      })
    }
    },
  }
</script>

<style></style>

