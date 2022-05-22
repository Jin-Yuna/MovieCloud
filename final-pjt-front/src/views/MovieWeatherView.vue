<template>
 <div>
  <p>'Your location data is ' + {{this.$store.state.latitude}} + ', ' +  {{this.$store.state.longitude}} + " ( " +  {{this.$store.state.city}} + " ) "
      + 'weather is ' + {{this.$store.state.weather_simple}}  + {{this.$store.state.weather_description}}
      + 'temperature is ' +  {{this.$store.state.temp}}</p>
</div>
</template>

<script>

export default {
  name: 'MovieWeatherView', 
  methods: {
  }
}
</script>

<style>

</style>