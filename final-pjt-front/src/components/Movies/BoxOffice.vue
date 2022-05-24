<template>
  <div>
    <BasicMovieCard 
      :movie="boxOfficeMovie"
    />
  </div>
</template>

<script>
import axios from 'axios'
import BasicMovieCard from '@/components/Movies/BasicMovieCard.vue'
export default {
  props: {
    boxOffice: Object
  },
  components: {
    BasicMovieCard,
  },
  data () {
    return {
      movieName: '',
      boxOfficeMovie: {},
    }
  },
  methods: {
    boxOfficeTMDB() {  
      const config = {
        params: {
          'api_key': process.env.VUE_APP_TMDB_API_KEY,
          'language': 'ko',
          'query': this.movieName,
        }
      }
      const TMDB_SEARCH_URL='https://api.themoviedb.org/3/search/movie'
      axios.get(TMDB_SEARCH_URL, config)
        .then(response => {
          this.boxOfficeMovie = response.data.results[0]
        })
    }
  },
  created () {
    this.movieName = this.boxOffice.movieNm
    this.boxOfficeTMDB()
  }
}
</script>

<style>

</style>