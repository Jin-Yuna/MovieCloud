<template>
  <v-app>
    <nav-bar></nav-bar>
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
      this.setMoviesTitle()
    },
    methods: {
      ...mapActions(['fetchCurrentUser', 'setMoviesTitle']),
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

      }, err => {
      this.textContent = err.message;
      })
    },
    
  },
}
</script>

<style>
body {
  padding-top: 40px;
  /* 생략 */
}

/* 가장 두꺼운 거 */
@font-face {
    font-family: 'LeferiPoint-BlackA';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/LeferiPoint-BlackA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
/* 중간 사이즈 */
@font-face {
    font-family: 'LeferiBaseType-RegularA';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/LeferiBaseType-RegularA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

/* 가장 얇은 거 */
@font-face {
    font-family: 'LeferiPoint-WhiteA';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2201-2@1.0/LeferiPoint-WhiteA.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

</style>

