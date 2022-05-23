<template>
  <div>
    {{ boxOffice }}
  </div>
</template>

<script>
import axios from 'axios'
export default {
  props: {
    boxOffice: Object,
  },
  data () {
    return {
      movieName: '',
      tmdb_movie_id: 0,
      result: null,
    }
  },
  methods: {
    getIMG() {
      // const KEY = process.env.VUE_APP_TMDB_API_KEY
      let config = {
        params: {
          'api_key': '52b6ad83bc7c8b6b80a9cf2ccba6366f',
          'language': 'ko',
          'query': this.movieName,
        }
      }
      const TMDB_SEARCH_URL='https://api.themoviedb.org/3/search/movie'
      axios.get(TMDB_SEARCH_URL, config)
        .then(response => {
          config = {
            params: {
              'api_key': '52b6ad83bc7c8b6b80a9cf2ccba6366f',
            }
          }
          const tmdb_movie_id = response.data.results[0].id
          const TBDM_IMG_URL = `https://api.themoviedb.org/3/movie/${tmdb_movie_id}/images`
          axios.get(TBDM_IMG_URL, config)
            .then(response => {
              console.log(response.data)
            })
        })
    }
  },
  created () {
    this.movieName = this.boxOffice.movieNm
    this.getIMG()
  }
}
</script>

<style>

</style>