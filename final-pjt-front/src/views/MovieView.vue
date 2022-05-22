<template>
  <div>
    <WeatherList />
    <BoxOfficeList />
  </div>
</template>

<script>
import WeatherList from '@/components/WeatherList.vue'
import BoxOfficeList from '@/components/BoxOfficeList.vue'

export default {
  name: 'MovieHome',
  components: {
    WeatherList,
    BoxOfficeList,
  },
}
</script>

<style>

</style>