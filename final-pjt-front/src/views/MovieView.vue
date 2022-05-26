<template>
  <div>
    <WeatherList />
    <BoxOfficeList />
    <TopRatedList />
  </div>
</template>

<script>
import WeatherList from '@/components/WeatherList.vue'
import BoxOfficeList from '@/components/BoxOfficeList.vue'
import TopRatedList from '@/components/Movies/TopRatedList.vue'
import { mapActions } from 'vuex'

export default {
  name: 'MovieHome',
  components: {
    WeatherList,
    BoxOfficeList,
    TopRatedList,
  },
  methods: {
    ...mapActions(['getToday'])
  },
  created() {
    this.$store.dispatch('getToday')
  }
}
</script>

<style>
.body {
  height: 100vh;
  background-size: cover; 
}
</style>