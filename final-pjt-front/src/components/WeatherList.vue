<template>
  <div class="weather_container">
    <h2 class="weather_text text_position1">오늘 같은 {{ weather.weather_simple }}</h2>
    <h2 class="weather_text text_position2">날씨의 추천 영화는</h2>
    <p class="text_small">오늘의 추천 영화는 {{ genre_name }}
      <br>현재 위치의 날씨에 따른 영화를 추천해드립니다.
    </p>
    <div class="flex">
      <div>
        <BasicMovieCard
          class="weather_card1"
          :movie="weather_movies[0]"
        />
        <BasicMovieCard
          class="weather_card2"
          :movie="weather_movies[1]"
        />
        <BasicMovieCard
          class="weather_card3"
          :movie="weather_movies[2]"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import { mapActions, mapGetters } from 'vuex'
import BasicMovieCard from '@/components/Movies/BasicMovieCard.vue'

export default {
  name: 'WeatherList',
  components: {
    BasicMovieCard,
  },
  data() {
    return {
      textContent: '',
      genre_name: [],
      ramdomMovie: [],
    }
  },
  computed: {
    ...mapGetters(['location', 'weather', 'weather_movies', 'weather_genres', 'genres'])
  },
  mounted() {
    this.showWeather()
    this.get_weather_movies(this.weather.weather_id)
    this.recommend_genres(this.weather.weather_id)
    this.getRamdomMovie()
  },
  methods: {
    showWeather() {
      let weatherUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${this.location.latitude}&lon=${this.location.longitude}&appid=${process.env.VUE_APP_WEATHER_API_KEY}` 
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
        this.genre_name.push(this.genres[genre_id])
        }
         return
      },
      getRamdomMovie() {
      const random = _.sampleSize(this.weather_movies, 3)
      this.ramdomMovie=  random
    },
    ...mapActions(['get_weather_movies'])

    },
    
}
</script>

<style scoped>
.flex {
  display: flex;
}
.weather_container {
  background: linear-gradient(to bottom, #BBDEFB, #f6f8fb);
  position: relative;
  height: 800px;
}
.weather_card1 {
  position: absolute;
  width: 187px;
  height: 259px;
  left: calc(50% - 187px/2 + 10px);
  top: calc(50% - 259px/2 - 10px);

  border-radius: 7px;
}
.weather_card2 {
  position: absolute;
  width: 187px;
  height: 259px;
  left: calc(50% - 187px/2 + 230px);
  top: calc(50% - 259px/2 - 200px);

  border-radius: 7px;
}
.weather_card3 {
  position: absolute;
  width: 187px;
  height: 259px;
  left: calc(50% - 187px/2 + 450px);
  top: calc(50% - 259px/2 - 0px);

  border-radius: 7px;
}
/* 텍스트 */
.weather_text {
  font-family: 'LeferiPoint-BlackA';
  font-style: normal;
  font-weight: 700;
  font-size: 55px;
  line-height: 63px;
  align-items: center;
  text-align: center;
  color: #1A2940;
}
.text_position1 {
  position: absolute;
  left: calc(50% - 481px/2 - 500.5px);
  top: calc(50% - 63px/2 - 180px);
}
.text_position2 {
  position: absolute;
  left: calc(50% - 481px/2 - 500.5px);
  top: calc(50% - 63px/2 - 100px);
}
.text_small {
  position: absolute;
  font-family: 'LeferiBaseType-RegularA';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 29px;
  display: flex;
  align-items: center;
  text-align: left;
  color: #1A2940;
  left: calc(50% - 481px/2 - 494.5px);
  top: calc(50% - 63px/2 + 10px);
}

</style>