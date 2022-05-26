<template>
  <div @click="getMovieDetailAxios(movie.id)" class="myhover">
    <!-- <img :src="getPoster" class="img_size" alt="">
    <h4>[ {{ movie.title }} ]</h4> -->
  <!--  -->
    <v-hover v-slot="{ hover }">
      <v-card
        class="mx-auto"
        color="grey lighten-4"
        min-width="250"
      >
      <!-- 너비/높이 -->
        <v-img
          :aspect-ratio="400/600"
          :src="getPoster"
        >
          <v-expand-transition>
            <div
              v-if="hover"
              class="d-flex transition-fast-in-fast-out grey lighten-3 v-card--reveal text-h2 white--text"
              style="height: 100%;"
            >
            <p class="myfont">{{ movie.title }}</p>
            <br>
            <p class="myfont">{{ movie.vote_average }}</p>
            </div>
          </v-expand-transition>
        </v-img>
      </v-card>
    </v-hover>
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
  },
  created(){
    console.log(this.movie)
  }
}
</script>

<style scoped>
.img_size {
  width: 17rem;
  height: 25rem;
}
.myhover{
  margin: 10px;
}
.myfont {
  left: calc(50% - 288px/2 - 58px);
  top: calc(50% - 26px/2 - 551.5px);
  font-family: 'LeferiBaseType-RegularA';
  font-style: normal;
  font-weight: 700;
  font-size: 25px;
  line-height: 129.49%;
  display: flex;
  align-items: center;
  text-align: center;
  color: #1A2940;
}
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: .6;
  position: absolute;
  width: 100%;
}
</style>