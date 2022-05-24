<template>
  <div>
    {{ movie }}
    <h3>영화 디테일 페이지</h3>
    <h1>{{ movie.title }}</h1>
    <img :src="posterUrl" alt="포스터">
    <p>{{ movie.overview }}</p>
    <!-- {{ movie }} -->
    <YouTube :movietitle="movie.title" />
  </div>
</template>

<script>
import YouTube from '@/components/Movies/YouTube.vue'
export default {
  components: {
    YouTube,
  },
  data() {
    return {
      movie: this.$store.state.movies.movieDetailAxios
    }
  },
  computed: {
    posterUrl() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
    },
  },
  methods: {
  },
}
</script>

<style>

</style>