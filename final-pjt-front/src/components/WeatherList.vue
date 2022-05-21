<template>
  <div>
    <p>{{ textContent }}</p>
    <router-link :to="{ name: 'MovieWeather' }">Weather</router-link>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'WeaherList',
  data() {
    return {
      textContent: '',
    }
  },
  mounted() {
    this.showWeather()
  },
  methods: {
    showWeather() {
      let apiKey = "8b0343f881770cdb1dbb079901414e9e"
      let weatherUrl = "https://api.openweathermap.org/data/2.5/weather?lat=" + this.$store.state.latitude
              + "&lon=" + this.$store.state.longitude
              + "&appid=" + apiKey; 
      //요청
      axios.get(weatherUrl)
        .then(response => {
          const weather = {
            weather_description: response.data.weather[0].description,
            weather_simple: response.data.weather[0].main,
            city: response.data.name,
            temp: response.data.main.temp - 273,
          }
          this.$store.dispatch('saveWeather', weather)
          
          this.textContent = 'Your location data is ' + this.$store.state.latitude + ', ' + this.$store.state.longitude + " ( " + this.$store.state.city + " ) "
          + 'weather is ' + this.$store.state.weather_simple + this.$store.state.weather_description
          + 'temperature is ' + this.$store.state.temp
        })
        .catch((error) => console.log(error))
    },
  }
}
</script>

<style>

</style>