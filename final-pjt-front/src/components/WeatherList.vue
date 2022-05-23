<template>
  <div>
    <p>{{ textContent }}</p>
    <router-link :to="{ name: 'MovieWeather' }">Weather</router-link>
    {{ weather_movies }}
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'WeaherList',
  data() {
    return {
      textContent: '',
    }
  },
  computed: {
    ...mapGetters(['location', 'weather', 'weather_movies'])
  },
  mounted() {
    this.showWeather()
    console.log(this.weather.weather_id)
    this.get_weather_movies(this.weather.weather_id)
  },
  methods: {
    showWeather() {
      console.log(this.location.latitude)
      let apiKey = "8b0343f881770cdb1dbb079901414e9e"
      let weatherUrl = "https://api.openweathermap.org/data/2.5/weather?lat=" + this.location.latitude
              + "&lon=" + this.location.longitude
              + "&appid=" + apiKey; 
      //요청
      axios.get(weatherUrl)
        .then(response => {
          const weather = {
            weather_id: response.data.weather[0].id,
            weather_description: response.data.weather[0].description,
            weather_simple: response.data.weather[0].main,
            city: response.data.name,
            temp: response.data.main.temp - 273,
          }
          this.$store.dispatch('saveWeather', weather)
          
          this.textContent = 'Your location data is ' + this.location.latitude + ', ' + this.location.longitude + " ( " + this.location.city + " ) "
          + 'weather is ' + this.weather.weather_simple + ' ' + this.weather.weather_description
          + 'temperature is ' + this.weather.temp 
        })
        .catch((error) => console.log(error))
    },
    ...mapActions(['get_weather_movies'])
  }
}
</script>

<style>

</style>