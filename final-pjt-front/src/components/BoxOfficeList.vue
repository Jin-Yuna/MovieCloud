<template>
  <v-container class="mt-10">
    <div class="goto">
      <p class="middle_size_text">역시 영화는 영화관이지</p>
      <p class="small_size_text ">내 위치의 주변 반경 20km 내의 영화관을 알려드려요</p>
      <p class="little_small_size_text">BOXOFFICE 순위도 궁금하다면?</p>
        <div style="text-align: center;">
          <v-btn style="display:inline-block;" class="boxoffice-button" x-large dark @click="onClickRedirect()">BOXOFFICE 보러 가기</v-btn>
        </div>
    </div>
      
      <div class="flex">
      <!--  -->
        <div>
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
    ...mapActions(['getBoxOffice']),
    onClickRedirect() {   
      window.open("https://www.kobis.or.kr/kobis/business/main/main.do", "_blank");    
    }
  },
  created() {
    this.getBoxOffice()
  }
};
</script>

<style scoped>
.mapsize {
  width: 65rem;
  margin-left: 15rem;
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
  margin-left: 3rem;
}

.middle_size_text {
  margin-top: 4rem;
  position: relative;
  font-family: 'LeferiPoint-BlackA';
  font-style: normal;
  font-weight: 700;
  font-size: 55px;
  line-height: 63px;
  display: flex;
  align-items: center;
  text-align: center;
  color: #1A2940;
  left: calc(50% - 180px/2 - 205px);
  top: calc(50% - 26px/2 + 318.5px);
}
.small_size_text {
  margin-bottom: 1rem;
  position: relative;
  font-family: 'LeferiPoint-WhiteA';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 129.49%;
  display: flex;
  align-items: center;
  text-align: center;
  color: #1A2940;
  left: calc(50% - 450px/2);
  top: calc(50% - 26px/2 + 300.5px);
}

.little_small_size_text {
  margin-bottom: 2rem;
  position: relative;
  font-family: 'LeferiBaseType-RegularA';
  font-style: normal;
  font-weight: 600;
  font-size: 25px;
  line-height: 129.49%;
  display: flex;
  align-items: center;
  text-align: center;
  color: #1A2940;
  left: calc(50% - 380px/2);
  top: calc(50% - 26px/2 + 300.5px);
}
.boxoffice-button {
  margin-bottom: 6rem;
  color:white;
  font-family: 'LeferiBaseType-RegularA';
  font-size: 18px;
  border: 0;
  border-radius: 7px;
  background: #1A2940;;
  background: linear-gradient(162deg, #1A2940 0%, rgb(56, 77, 110) 50%, #1A2940 100%);
}
a{
  text-decoration: none;
}
</style>
