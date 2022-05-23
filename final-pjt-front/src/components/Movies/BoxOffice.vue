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
      movieCd : this.boxOffice.movieCd,
      boxofficedetail : {},
    }
  },
  methods: {
    getBoxOfficeDetail() {
      const KEY = process.env.VUE_APP_BOX_OFFICE_API_KEY

      // const config = {
      //   params: {
      //     key: process.env.VUE_APP_BOX_OFFICE_API_KEY,
      //     targetDt: '20124079',
      //   }
      // }
    const BoxOfficeDetailURL=`https://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=${KEY}&movieCd=${this.movieCd}`
    axios.get(BoxOfficeDetailURL)
      .then(response => {
        this.boxofficedetail = response.data.movieInfoResult.movieInfo
        console.log(this.boxofficedetail)
      })
    }
  },
  created () {
    this.getBoxOfficeDetail()
  }
}
</script>

<style>

</style>