<template>
  <div class="weather_container">
    <v-container>
    <div class="content">
      <h2>Edit Drop</h2>
      <h2>Edit Drop</h2>
    </div>
    <br><br><br><br><br><br><br>
    <DropForm v-if="drop" :drop="drop" :movies_title="movies_title" action="update" />
    </v-container>
  </div>

</template>

<script>
import axios from 'axios'
import DropForm from '@/components/DropForm.vue'
import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'DropEditView',
    components: {
       DropForm 
    },
    data() {
      return {
        movies_title: []
      }
    },
    computed: {
      ...mapGetters(['drop'])
    },
    methods: {
      ...mapActions(['getDrop'])
    },
    mounted() {
      this.getDrop(this.$route.params.dropPk)
      axios.get('http://127.0.0.1:8000/movies/get_movie_title/')
      .then(response => {
        this.movies_title = response.data
    })
    },

  }
</script>

<style scoped>

.weather_container {
  background: linear-gradient(to top, #BBDEFB, #ffffff);
  height: 100vh;
  background-size: cover; 
}

.bold_text {
  margin-top: 10rem;
  margin-bottom: 5rem;
  position: relative;
  font-family: 'LeferiPoint-BlackA';
  font-style: normal;
  font-weight: 700;
  font-size: 55px;
  line-height: 63px;
  color: #425E7A;
  left: calc(50% - 290px/2 - 0px);
  top: calc(50% - 26px/2 + 318.5px);
}

/* 텍스트 효과 */
.content {
  margin-top: 13rem;
  font-family: 'LeferiPoint-BlackA';
  position: relative;
  left: calc(50% - 290px/2 + 100px);
  top: calc(50% - 26px/2 + 100.5px);
}

.content h2 {
  color: #fff;
  font-size: 4em;
  position: absolute;
  transform: translate(-50%, -50%);
}

.content h2:nth-child(1) {
  color: transparent;
  -webkit-text-stroke: 1px #425E7A;
}

.content h2:nth-child(2) {
  color: #425E7A;
  animation: animate 4s ease-in-out infinite;
}

@keyframes animate {
  0%,
  100% {
    clip-path: polygon(
      0% 45%,
      16% 44%,
      33% 50%,
      54% 60%,
      70% 61%,
      84% 59%,
      100% 52%,
      100% 100%,
      0% 100%
    );
  }
  50% {
    clip-path: polygon(
      0% 60%,
      15% 65%,
      34% 66%,
      51% 62%,
      67% 50%,
      84% 45%,
      100% 46%,
      100% 100%,
      0% 100%
    );
  }
}

</style>
