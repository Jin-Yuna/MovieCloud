<template>
  <div>
    <h3>{{ boxOffice.movieNm }}</h3>
    <img :src="poster" alt="">
    <p>{{ boxOffice }}</p>
    <p>{{ overview }}</p>
    <div v-if="imgs.length" class="flex">
      <BoxOfficeImg
        v-for="img in imgs"
        :key="img"
        :img="img"
      />
    </div>
    <h4 v-else>이 영화는 이미지가 없습니다.</h4>
  </div>
</template>

<script>
import axios from 'axios'
import BoxOfficeImg from '@/components/Movies/BoxOfficeImg.vue'
export default {
  props: {
    boxOffice: Object,
  },
  components: {
    BoxOfficeImg,
  },
  data () {
    return {
      movieName: '',
      tmdb_movie_id: 0,
      imgs: [],
      poster: '',
      overview: '',
    }
  },
  methods: {
    getIMG() {
      let config = {
        params: {
          'api_key': process.env.VUE_APP_TMDB_API_KEY,
          'language': 'ko',
          'query': this.movieName,
        }
      }
      const TMDB_SEARCH_URL='https://api.themoviedb.org/3/search/movie'
      axios.get(TMDB_SEARCH_URL, config)
        .then(response => {
          // 더 필요한 데이터가 있다면 여기 response(tbdb)에서 한번 찾아보기
          // 장르는 장르 번호로 되어 있음.
          this.overview = response.data.results[0].overview
          const tmdb_movie_id = response.data.results[0].id
          config = {
            params: {
              'api_key': process.env.VUE_APP_TMDB_API_KEY,
            }
          }
          const TBDM_IMG_URL = `https://api.themoviedb.org/3/movie/${tmdb_movie_id}/images`
          axios.get(TBDM_IMG_URL, config)
            .then(response => {
              const posterobjects = response.data.posters
              for (const poster of posterobjects) {
                if (poster.iso_639_1 == 'ko' ) {
                  this.poster = 'https://image.tmdb.org/t/p/w500' + poster.file_path
                }
              }
              if (!this.poster) {
                this.poster = 'https://image.tmdb.org/t/p/w500' + response.data.posters[0].file_path
              }
              const imgobjects = response.data.backdrops
              for (const img of imgobjects) {
                this.imgs.push(img.file_path)
              }
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
.flex {
  display: flex;
}

</style>