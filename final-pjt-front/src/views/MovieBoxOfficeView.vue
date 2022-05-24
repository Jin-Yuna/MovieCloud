<template>
  <div>
    <h1>MovieBoxOfficeView</h1>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  components : {

  },
  data() {
    return {
      date: '',
      boxOfficeList : [],
    }
  },
  methods : {
    getBoxOffice () {
      const BoxOfficeURL ='http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
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