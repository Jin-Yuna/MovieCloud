<template>
  <div class="mymargintop">
    <v-flex class="justify-center">
      <h1 class="my_bord_text">DROPS</h1>
    </v-flex>
      <v-container class="mymargintop">
        <v-row justify="center">
          <v-col
            v-for="drop in drops"
            :key="drop.id"
            cols="auto"
          >
            <v-col
              :elevation="drops.length - 1"
              height="300"
              width="200"
            >
              <v-row
                class="fill-height"
                align="center"
                justify="center"
              >
              <RealDropCard 
                :drop="drop"
                class="mr-5" 
              />
              </v-row>
            </v-col>
          </v-col>
        </v-row>
      </v-container>
    <div class="ocean">
      <div class="wave"></div>
      <div class="wave"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import drf from '@/api/drf'
import RealDropCard from '@/components/RealDropCard.vue'
export default {
  name: 'DropListView',
  components: {
    RealDropCard,
  },
  data() {
    return {
      drops : []
    }
  },
  methods: {

  },
  created() {

    axios({
      url: drf.drops.drops(),
      method: 'get',
    })
    .then(response => {
      this.drops = response.data
      })
  }
}
</script>

<style scoped>
.mymargintop {
  margin-top: 10rem;
}
.my_bord_text {
  width: 481px;
  height: 63px;
  margin-left: 16rem;
  font-family: 'LeferiPoint-BlackA';
  font-style: normal;
  font-weight: 700;
  font-size: 55px;
  line-height: 63px;
  display: flex;
  align-items: center;
  text-align: center;

  color: #425E7A;
}


/* 긁긁 */
/* html, body { height: 100%; }
body {
  background:radial-gradient(ellipse at center, rgba(255,254,234,1) 0%, rgba(255,254,234,1) 35%, #B7E8EB 100%);
  overflow: hidden;
} */

.ocean { 
  height: 5%;
  width:100%;
  position:absolute;
  bottom:0;
  left:0;
  background: #015871;
}

.wave {
  background: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/85486/wave.svg) repeat-x; 
  position: absolute;
  top: -198px;
  width: 6400px;
  height: 198px;
  animation: wave 7s cubic-bezier( 0.36, 0.45, 0.63, 0.53) infinite;
  transform: translate3d(0, 0, 0);
}

.wave:nth-of-type(2) {
  top: -175px;
  animation: wave 7s cubic-bezier( 0.36, 0.45, 0.63, 0.53) -.125s infinite, swell 7s ease -1.25s infinite;
  opacity: 1;
}

@keyframes wave {
  0% {
    margin-left: 0;
  }
  100% {
    margin-left: -1600px;
  }
}

@keyframes swell {
  0%, 100% {
    transform: translate3d(0,-25px,0);
  }
  50% {
    transform: translate3d(0,5px,0);
  }
}
</style>