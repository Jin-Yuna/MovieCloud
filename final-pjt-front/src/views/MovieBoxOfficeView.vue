<template>
  <div>
    <BoxOffice 
      v-for="boxOffice in boxOfficeList" 
      :key=boxOffice.movieCd
      :boxOffice="boxOffice"
    />
  </div>
</template>

<script>
import axios from 'axios'
import BoxOffice from '@/components/Movies/BoxOffice.vue'
export default {
  components : {
    BoxOffice,
  },
  data() {
    return {
      date: '',
      boxOfficeList : [],
    }
  },
  methods : {
    getBoxOffice () {
      const BoxOfficeURL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
      const config = {
        params: {
          key: process.env.VUE_APP_BOX_OFFICE_API_KEY,
          targetDt: this.date,
        }
      }
      axios.get(BoxOfficeURL, config)
        .then(response => {
          this.boxOfficeList = response.data.boxOfficeResult.dailyBoxOfficeList
        })
    }
  },
  created() {
    const nowDay = new Date()
    const year = nowDay.getFullYear()
    const month = ('0' + nowDay.getMonth() + 1).slice(-2)
    const day = ('0' + nowDay.getDate()).slice(-2)
    this.date = year + month + day
    this.getBoxOffice()
  }
}
</script>

<style>

</style>