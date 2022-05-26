<template>
  <div class="detail_container">

    <figure class="image-container">
      <img class="backdrop" :src="backdroppath" alt="backdrop">
    </figure>
    <div class="overview-container">
      <h2 class="movie-title text_position1">{{ movie.title }}</h2>
      <p class="original-title">{{movie.original_title}}</p>
      <v-progress-linear class="line"
        color="#F4F8FB"
        rounded
        value="100"
      ></v-progress-linear>
      <p class="movie-small-explain">
        {{ movie.release_date }} 개봉작 | 런타임 {{movie.runtime }}분</p>
      <p class="movie-small-explain-1">선호도</p>
      <v-chip class="chips-popularity" color="pink" text-color="white">
        <span>{{movie.popularity}}</span>
      </v-chip>
      <p class="movie-small-explain-2">평점</p>
      <v-chip class="chips-popularity2" color="pink" text-color="white">
        <span>{{ movie.vote_average }}</span>
      </v-chip>
      <p class="tagline">"{{movie.tagline }}"</p>
      <div>
      </div>
      <div class="please">
       <v-chip outlined class="chips" color="indigo darken-3" v-for="genre in movie.genres" v-bind:key="genre.id">
        <span>{{genre.name}}</span>
      </v-chip>
      </div>
      <p class="text_small">{{ movie.overview }}</p>
    </div>
    <div class="flex">
      <img class="poster" :src="posterUrl" alt="포스터">
    </div>
        <!-- {{ movie }} -->
    <p class="middle_size_text">영화 미리보기</p>
    <div class="youtube_movie">
      <YouTube :movietitle="movie.title" class="real"/>
    </div>
        <!-- <div class="abc">{{ movie }}</div> -->

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
      movie: this.$store.state.movies.movieDetailAxios,
      // rating: parseInt(this.movie.vote_average / 2)
    }
  },
  computed: {
    posterUrl() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.poster_path
    },
    backdroppath() {
      return 'https://image.tmdb.org/t/p/w500' + this.movie.backdrop_path
    },
  },
  methods: {
  },
}
</script>

<style scoped>
.abc {
  margin-top: 3rem;
}
.detail_container {
  position: relative;
}
.backdrop {
    width: 100%;
    display: block;
}

.image-container .backdrop {
  width: 100%;
  height: 100%;
  object-fit: cover;
  -webkit-mask-image: linear-gradient(to top, transparent 0.5%, black 80%);
  mask-image: linear-gradient(to top, transparent 0.5%, black 100%);
} 
.movie-title {
  font-family: 'LeferiPoint-BlackA';
  font-weight: 300;
  font-size: 45px;
  line-height: 63px;
  color: #F4F8FB;
  text-shadow: 0px 1px 7px rgba(0, 0, 0, 1);
  align-items: center;
  text-align: center;
}

.original-title {
  font-family: 'LeferiBaseType-RegularA';
  font-weight: 300;
  font-size: 25px;
  line-height: 63px;
  color: #F4F8FB;
  text-shadow: 0px 1px 7px rgba(0, 0, 0, 1);
  align-items: center;
  text-align: center;
  position: absolute;
  left: calc(50% - 481px/2 - 500.5px);
  top: 15%;
}
/* 제목 */
.text_position1 {
  position: absolute;
  left: calc(50% - 481px/2 - 500.5px);
  top: 13%;
}
.text_position2 {
  position: absolute;
  left: calc(50% - 481px/2 - 500.5px);
  top: 20%;
}
.overview-container {
  display: flex;
}
.text_small {
  margin-top: 100px;
  margin-right: 50%;
  position: absolute;
  font-family: 'LeferiPoint-WhiteA';
  font-weight: 100;
  font-size: 23px;
  line-height: 29px;
  display: flex;
  align-items: center;
  text-align: left;
  color: #F4F8FB;
  text-shadow: 0px 0px 15px rgba(0, 0, 0, 1);
  left: calc(50% - 481px/2 - 494.5px);
  top: 650px;
}
.poster {
  position: absolute;
  width: 450px;
  left: calc(62%);
  top: calc(13%);
  box-shadow: 5px 5px 5px #000;
}
/* 영화 미리보기 */
.middle_size_text {
  position: absolute;
  font-family: 'LeferiPoint-BlackA';
  font-weight: 500;
  font-size: 48px;
  line-height: 63px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #F4F8FB;
  text-shadow: 0px 1px 7px rgba(0, 0, 0, 1);
  left: 45%;
  top: 1150px;
}
.youtube_movie {
  margin-left: 580px; 
  margin-bottom: 400px;
}
.real {
  width: 100%
}
.line {
  position: absolute;
  width: 750px;
  left: 19%;
  top: 17%;
}
/* release runtime */
.movie-small-explain {
  position: absolute;
  font-family: 'LeferiPoint-WhiteA';
  font-weight: 100;
  font-size: 15px;
  line-height: 63px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #F4F8FB;
  text-shadow: 0px 1px 7px rgba(0, 0, 0, 1);
  left: 19%;
  top: 420px;
}
.chips {
  margin-right: 5px;
}

/* chips */
.chips-popularity {
  height: 28px;
  position: absolute;
  left: 21%;
  top:465px;
}
.chips-popularity2 {
  height: 28px;
  position: absolute;
  left: 25.5%;
  top: 465px;
}
.movie-small-explain-1 {
  position: absolute;
  font-family: 'LeferiPoint-WhiteA';
  font-weight: 100;
  font-size: 15px;
  line-height: 63px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #F4F8FB;
  text-shadow: 0px 1px 7px rgba(0, 0, 0, 1);
  left: 19%;
  top: 450px;
}
.movie-small-explain-2 {
  position: absolute;
  font-family: 'LeferiPoint-WhiteA';
  font-weight: 100;
  font-size: 15px;
  line-height: 63px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #F4F8FB;
  text-shadow: 0px 1px 7px rgba(0, 0, 0, 1);
  left: 24%;
  top: 450px;
}
/* tagline */
.tagline {
  position: absolute;
  font-family: 'LeferiBaseType-RegularA';
  font-weight: 500;
  font-size: 40px;
  line-height: 63px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #F4F8FB;
  text-shadow: 0px 1px 7px rgba(0, 0, 0, 1);
  left: 19%;
  top: 600px;
}
.please {
  position: absolute;
  left: 74%;
  top: 40%;
}

</style>