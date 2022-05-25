<template>
  <div>
    <router-link :to="{ name: 'MovieBoxoffice' }">
      BoxOffice
    </router-link>
    <Map />
    <div class="d-flex"> 
      <BoxOffice 
        v-for="boxOffice in boxOfficeList" 
        :key=boxOffice.movieCd
        :boxOffice="boxOffice"
      />
    </div> 
  </div>
</template>

<script>
import Map from '@/components/Map'

import BoxOffice from '@/components/Movies/BoxOffice.vue'
import { mapActions } from 'vuex'

export default {
  components: {
    Map,
    BoxOffice,
  },
  data() {
    return {
      boxOfficeList : this.$store.state.movies.boxOffie,
    }
  },
  methods : {
    ...mapActions(['getBoxOffice'])
  },
  created() {
    this.getBoxOffice()
  }
};
</script>

<style>
.flex {
  display: flex;
}
</style>
