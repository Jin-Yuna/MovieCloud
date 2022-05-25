<template>
  <div>
    <p>{{ textContent }}</p>
    <router-link :to="{ name: 'MovieWeather' }">Weather</router-link>
    오늘 같은 {{ weather.weather_simple }} 날씨의 추천 영화는 {{ genre_name }}
    <div class="flex">
    <!-- <BasicMovieCard 
      v-for="movie in weather_movies"
      :key="movie.id"
      :movie="movie"
    /> -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions, mapGetters } from 'vuex'
// import BasicMovieCard from '@/components/Movies/BasicMovieCard.vue'

export default {
  name: 'WeaherList',
  components: {
    // BasicMovieCard,
  },
  data() {
    return {
      textContent: '',
      genre_name: [],
    }
  },
  computed: {
    ...mapGetters(['location', 'weather', 'weather_movies', 'weather_genres', 'genres'])
  },
  mounted() {
    this.showWeather()
    this.get_weather_movies(this.weather.weather_id)
    this.recommend_genres(this.weather.weather_id)
  },
  methods: {
    showWeather() {
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
    recommend_genres(id) {
      var based_num = parseInt(id / 100)
      if (based_num === 8) {
        if (id === 800) {
          based_num = 800
        }
        else if (id === 801) {
          based_num = 801
        }
        else {
          based_num = 80
        }
      }
      const genres_id_list = this.weather_genres[based_num]
      for (var genre_id of genres_id_list) {
        for (var genre of this.genres) {
          if (genre_id === genre.id) {
            this.genre_name.push(genre.name)
          }
        }
      }
      return
    },
    ...mapActions(['get_weather_movies'])
  }
}
</script>

<style>

</style>