<template>
  <div>    
    <Map />
    <router-link :to="{ name: 'MovieBoxoffice' }">
      BoxOffice
    </router-link></div>
</template>

<script>
import Map from '@/components/Map'

export default {
  components: {
    Map,
  }
};
</script>

<style>
</style>
