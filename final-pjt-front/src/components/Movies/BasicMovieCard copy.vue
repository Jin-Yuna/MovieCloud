<template>
  <div @click="getMovieDetailAxios(movie.id)" class="myhover">
    <img :src="getPoster" class="img_size" alt="">
    <h4>[ {{ movie.title }} ]</h4>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  props: {
    movie: Object,
  },
  computed: {
    getPoster() {
      return 'https://image.tmdb.org/t/p/w500'+this.movie.poster_path
    }
  },
  methods: {
    ...mapActions(['getMovieDetailAxios']),
  }
}
</script>

<style>
.img_size {
  width: 17rem;
  height: 25rem;
}
.myhover{
  margin: 10px;
}
.myhover:hover {
  filter: brightness(50%);
}
</style>