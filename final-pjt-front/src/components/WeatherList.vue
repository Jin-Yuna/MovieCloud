<template>
  <div>
    <p>{{ textContent }}</p>
    <router-link :to="{ name: 'MovieWeather' }">movie
    </router-link>
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
  created() {
    this.geofind()
  },
  methods: {
    showLocations() {
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
        })
        .catch((error) => console.log(error))
    },
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

      this.showLocations()

      this.textContent = 'Your location data is ' + this.$store.state.latitude + ', ' + this.$store.state.longitude + " ( " + this.$store.state.city + " ) "
      + 'weather is ' + this.$store.state.weather_simple + this.$store.state.weather_description
      + 'temperature is ' + this.$store.state.temp
      }, err => {
      this.textContent = err.message;
      })
    }
  }
}
</script>

<style>

</style>