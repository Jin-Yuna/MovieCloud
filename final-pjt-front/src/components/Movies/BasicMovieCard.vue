<template>
  <div class="card" style="width: 18rem;" @click="getMovieDetailAxios(movie.id)" >
    <!-- <img :src="getPoster" class="card-img-top" alt="포스터이미지">
    <div class="card-body">
      <p class="card-text">{{movie.title}}.</p>
    </div> -->
    <!--  -->
    {{ movie }}
    <div class="card bg-dark text-white" style="width: 18rem;" @click="getMovieDetailAxios(movie.id)">
      <img :src="getPoster" class="card-img" alt="포스터이미지">
      <div class="card-img-overlay">
        <h5 class="card-title">{{ movie.title}}</h5>
        <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
      </div>
    </div>
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
.myhover:hover {
  filter: brightness(50%);
}
</style>