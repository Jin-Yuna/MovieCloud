<template>
  <div class="flex">
    <BasicMovieCard 
      v-for="movie in topMovies"
      :key="movie.id"
      :movie="movie"
    />
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
      topMovies:[],
    }
  },
  methods: {
    getTopRated() {
      const config = {
        params: {
          'api_key': process.env.VUE_APP_TMDB_API_KEY,
          'language': 'ko',
          'limit': '10',
        }
      }
      const TMDB_TOP_RATED_URL='https://api.themoviedb.org/3/movie/top_rated'
      axios.get(TMDB_TOP_RATED_URL, config)
        .then(response => {
          this.topMovies=response.data.results.slice(0,10)
          console.log(this.topMovies)
        })
    }
  },
  created() {
    this.getTopRated()
  }
}
</script>

<style>
.flex {
  display: flex;
}
</style>