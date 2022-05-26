<template>
  <v-container class="mt-10">
    <router-link :to="{ name: 'MovieBoxoffice' }">
      BoxOffice
    </router-link>
    <div class="flex">
      <!--  -->
        <div class="boxcardsize">
        <v-carousel
          cycle
          hide-delimiter-background
          show-arrows-on-hover
        >
          <v-carousel-item
            v-for="boxOffice in boxOfficeList" 
            :key=boxOffice.movieCd
            class="boxcardsize"
          >
            <BoxOffice 
            :boxOffice="boxOffice"
            />
          </v-carousel-item>
        </v-carousel>
        </div>
        <div class="mapsize">
          <Map />
        </div>

      <!--  -->
      <!-- <v-flex> 
        <BoxOffice 
          v-for="boxOffice in boxOfficeList" 
          :key=boxOffice.movieCd
          :boxOffice="boxOffice"
        />
      </v-flex> -->
    </div>
  </v-container>
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
      boxOfficeList : this.$store.state.movies.boxOffie.slice(0,3),
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
.mapsize {
  width: 80rem;
  margin-left: 7rem;
}

.flex {
  display: flex;
}
.boxcardsize {
  position: relative;
  width: 20rem;
  /* left: calc(50% - 190px/2 - 100px);  */
  margin-top: 2rem;
  top: calc(50% - 284px/2 - 100.5px);
}
</style>
