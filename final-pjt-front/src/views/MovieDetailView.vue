<template>
  <div class="detail_container">

    <div class="image-container" sytle="position: absolute; top:0; left:0; z-index: -1">
      <img class="backdrop" :src="backdroppath" alt="backdrop">
    </div>
      <v-card
          class="mx-auto my-0"
          max-width="1500"
          style="background: transparent; box-shadow: initial; position: absolute; top: 250px; left: 20%;"
        >
      <v-list-item three-line>
        <v-list-item-content>
          <div class="mb-4">
            <v-chip class="chips" color="pink" text-color="white" v-for="genre in movie.genres" v-bind:key="genre.id">
              <span>{{genre.name}}</span>
            </v-chip>
          </div>
          <v-list-item-title class="movie-title">
            {{ movie.title }}
          </v-list-item-title>
          <p class="mb-2 original-title">{{movie.original_title}}</p>
          <v-progress-linear class="line"
            color="#F4F8FB"
            rounded
            value="100"
            style="width: 100px;"
          ></v-progress-linear>
          <p class="movie-small-explain">
          {{ movie.release_date }} 개봉작 | 런타임 {{movie.runtime }}분</p>
          <div class="popularity"> 
            <p class="movie-small-explain-1">선호도</p>
            <v-chip outlined class="chips-popularity" color="pink" text-color="white">
              <span>{{movie.popularity}}</span>
            </v-chip>
            <p class="movie-small-explain-2">평점</p>
            <v-chip outlined class="chips-popularity2" color="pink" text-color="white">
              <span>{{ movie.vote_average }}</span>
            </v-chip>
          </div>
        <p style="max-width: 800px;" class="tagline" v-if="movie.tagline">"{{movie.tagline }}"</p>
        <div style="max-width: 800px;">
          <p class="text_small">
            {{ movie.overview }}
          </p>
        </div>
        </v-list-item-content>
  
        <v-list-item-avatar
          class="ma-3 poster"
          width="530"
          height="750"
          tile
        >
        <v-img :src="posterUrl"></v-img>
        </v-list-item-avatar>

        </v-list-item>
      </v-card>
      <div style="position: absolute;">

      </div>
      <p class="middle_size_text">영화 미리보기</p>
        <div class="youtube_movie">
          <YouTube :movietitle="movie.title" class="real"/>
        </div>
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
.detail_container {
  background-color: #1A2940; 
}
.image-container .backdrop {
  width: 100%;
  height: 1300px;
  -webkit-mask-image: linear-gradient(to top, transparent 0.5%, black 80%);
  mask-image: linear-gradient(to top, transparent 0.5%, black 100%);
} 
/* 장르 */
.chips {
  height: 30px;
  margin-right: 7px;
  font-family: 'LeferiPoint-WhiteA';
  align-items: center;
  text-align: center;
  margin-bottom: 20px;
}

/* 타이틀 */
.movie-title {
  margin-left: 0;
  font-family: 'LeferiPoint-BlackA';
  font-weight: 300;
  font-size: 45px;
  line-height: 63px;
  color: #F4F8FB;
  text-shadow: 0px 1px 7px rgba(0, 0, 0, 1);
}
/* 라인 */
.line {
  width: 500px;
  margin-top: 10px;
  margin-bottom: 20px;
}
/* 포스터 */
.poster {
  width: 530px;
  box-shadow: 5px 5px 5px #000;
}
/* 타이틀2 */
.original-title {
  font-family: 'LeferiBaseType-RegularA';
  font-weight: 300;
  font-size: 25px;
  color: #F4F8FB;
  text-shadow: 0px 1px 7px rgba(0, 0, 0, 1);
}
/* release runtime */
.movie-small-explain {
  font-family: 'LeferiPoint-WhiteA';
  font-weight: 100;
  font-size: 15px;
  color: #F4F8FB;
  margin-bottom: 8px;
  text-shadow: 0px 1px 7px rgba(0, 0, 0, 1);
}
/* 선호도 배점 */
.popularity {
  margin: 0;
  padding: 0;
  align-items: center;
  display: flex;
}
.movie-small-explain-1 {
  font-family: 'LeferiPoint-WhiteA';
  margin-bottom: 0;
  margin-right: 7px;
  font-weight: 100;
  font-size: 15px;
  color: #F4F8FB;
  text-shadow: 0px 1px 7px rgba(0, 0, 0, 1);
}
.movie-small-explain-2 {
  font-family: 'LeferiPoint-WhiteA';
  margin-bottom: 0;
  font-weight: 100;
  font-size: 15px;
  margin-right: 7px;
  color: #F4F8FB;
  text-shadow: 0px 1px 7px rgba(0, 0, 0, 1);
}

/* chips */
.chips-popularity {
  height: 28px;
  margin-right: 15px;
}
.chips-popularity2 {
  height: 28px;
}
/* 태그라인 */
.tagline {
  margin-top: 70px;
  font-family: 'LeferiBaseType-RegularA';
  font-weight: 500;
  font-size: 40px;
  line-height: 63px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #F4F8FB;
  text-shadow: 0px 1px 7px rgba(0, 0, 0, 1);
}

/* overview 설명 */
.text_small {
  margin-top: 80px;
  font-family: 'LeferiPoint-WhiteA';
  font-weight: 100;
  font-size: 23px;
  line-height: 33px;
  color: #F4F8FB;
  text-shadow: 0px 0px 15px rgba(0, 0, 0, 1);
}

/* 영화 미리보기 */
.middle_size_text {
  margin-top: 0;
  margin-bottom: 100px;
  font-family: 'LeferiPoint-BlackA';
  font-weight: 500;
  font-size: 48px;
  line-height: 63px;
  text-align: center;
  color: #F4F8FB;
  text-shadow: 0px 1px 7px rgba(0, 0, 0, 1);
}
.youtube_movie {
  margin-left: 28%; 
  margin-bottom: 400px;
}
.real {
  width: 100%
}




</style>