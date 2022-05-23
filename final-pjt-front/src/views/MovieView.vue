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

export default {
  name: 'MovieHome',
  components: {
    WeatherList,
    BoxOfficeList,
    TopRatedList,
  },
}
</script>

<style>

</style>