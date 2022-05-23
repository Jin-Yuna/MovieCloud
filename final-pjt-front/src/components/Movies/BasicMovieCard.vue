<template>
  <div>
    <img :src="getPoster" class="img_size" alt="">
    <h4>[ {{ movie.title }} ]</h4>
  </div>
</template>

<script>
export default {
  props: {
    movie: Object,
  },
  computed: {
    getPoster() {
      return 'https://image.tmdb.org/t/p/w500'+this.movie.poster_path
    }
  }
}
</script>

<style>
.img_size {
  width: 200px;
  height: 300px;
}
</style>