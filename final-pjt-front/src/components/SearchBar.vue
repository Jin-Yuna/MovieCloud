<template>
<div>
  <transition>
  <div id="search" class="modal" v-if="show">
    <div class="bg"></div>
    <div class="searchbar">
      <div class="flex explain">
        <p>영화를 검색해보아용</p>
        <button @click="toggleShow">닫기</button>
      </div>
      <input type="text" @keyup.enter="search">
      <div v-if="result_show">
        <div 
          v-for="result_movie in result"
          :key="result_movie.id"
          @click="getMovieDetailAxios(result_movie.id)">
            {{ result_movie.title }}
        </div>
      </div>
    </div>
    </div>
   </transition>
  <button @click="toggleShow">검색 아이콘</button>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'SearchBar',
  data() {
    return {
      show: false,
      inputValue: '',
      result: [],
      result_show: false,
    }
  },
  computed: {
    ...mapGetters(['movieSearchList', 'movieTitiles'])
  },
  created() {
    this.$store.dispatch('get_movies_search')
  },
  methods: {
    toggleShow() {
      this.show = !this.show
      if (!this.show) {
        this.result = []
      }
    },
    search(event) {
      this.inputValue = event.target.value
      const movies = this.movieSearchList
      for (var movie of movies) {
        if (movie.title.includes(this.inputValue)) {
          this.result.push(movie)
        }
      }
      this.result_show = true
    },
    ...mapActions(['getMovieDetailAxios']),
  }
}
</script>

<style>
.v-enter-active, .v-leave-active {
  transition: opacity 1s;
}
/* 더 이상 보이게 되지 않았을 때의 투명도 */
.v-enter, .v-leave-to {
  opacity: 0;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal .bg {
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
        }
.searchbar {
  position: absolute;
  background-color: #fff;
  width: 400px;
  height: 300px;
  padding: 15px;
        }
.explain {
  align-items: center;
  justify-content: space-between;
}
</style>