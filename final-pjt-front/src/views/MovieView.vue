<template>
  <div>
    <WeatherList />
    <BoxOfficeList />
    <router-link :to="{ name: 'MovieBoxoffice' }">
      BoxOffice
    </router-link>
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