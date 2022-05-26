<template>
  <div class="mb-16 rated">
    <p class="middle_size_text">마이너스 점수는 왜 존재하지 않는가</p>
    <p class="small_size_text ">평점 순으로 영화를 추천해드립니다</p>
    <v-carousel hide-delimiters>
      <v-carousel-item
        class="flex"
        v-for="(item, i) in this.items"
        :key="i"
      >
        <v-row justify="center">
          <BasicMovieCard
            v-for="movie in item"
            :key="movie.id"
            :movie="movie"
          />
        </v-row>
      </v-carousel-item>
    </v-carousel>
  </div>
</template>

<script>
import axios from 'axios'
import BasicMovieCard from '@/components/Movies/BasicMovieCard.vue'
export default {
  components: {
    BasicMovieCard,
  },
  data() {
    return {
      items: {
        topMovies1: [],
        topMovies2: [],
        topMovies3: [],
        topMovies4: [],
      }
    }
  },
  methods: {
    getTopRated() {
      let config = {
        params: {
          'api_key': process.env.VUE_APP_TMDB_API_KEY,
          'language': 'ko',
          'page': 1,
        }
      }
      const TMDB_TOP_RATED_URL='https://api.themoviedb.org/3/movie/top_rated'
      axios.get(TMDB_TOP_RATED_URL, config)
        .then(response => {
          this.items.topMovies1=response.data.results.slice(0,10)
          this.items.topMovies2=response.data.results.slice(10,20)
          this.items.topMovies3=response.data.results.slice(11,20)
        }),
      config = {
        params: {
          'api_key': process.env.VUE_APP_TMDB_API_KEY,
          'language': 'ko',
          'page': 2,
        }
      }
      axios.get(TMDB_TOP_RATED_URL, config)
        .then(response => {
          this.items.topMovies3=response.data.results.slice(0,10)
          this.items.topMovies4=response.data.results.slice(10,20)
        })
    }
  },
  created() {
    this.getTopRated()
  }
}
</script>

<style scoped>
.flex {
  display: flex;
  margin-bottom: 13rem;
}
.middle_size_text {
  margin-top: 10rem;
  position: relative;
  font-family: 'LeferiPoint-BlackA';
  font-style: normal;
  font-weight: 700;
  font-size: 55px;
  line-height: 63px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #425E7A;
  left: calc(50% - 290px/2 - 205px);
  top: calc(50% - 26px/2 + 318.5px);
}
.small_size_text {
  margin-bottom: 8rem;
  position: relative;
  font-family: 'LeferiPoint-WhiteA';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 129.49%;
  display: flex;
  align-items: center;
  text-align: center;
  color: #425E7A;
  left: calc(50% - 290px/2 - 0px);
  top: calc(50% - 26px/2 + 300.5px);
}
.rated {
  margin-bottom: 20px;
}
</style>