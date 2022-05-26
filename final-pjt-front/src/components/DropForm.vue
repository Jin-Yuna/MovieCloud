<template>
  <div>
    <h2>{{ this.newDrop.movie }}!!!</h2>
    <form @submit.prevent="onSubmit" class="form">
      <!-- 수정할 때는 영화목록 선택 안보이게 함 -->
      <div v-if="this.action==='create'"> 
        <label for="movie">영화</label>
        <input type="text" @click="toggleShow" :placeholder="this.result_movie">
        <!-- <select id="movie" v-model="newDrop.movie">
          <option v-for="movie_title in movies_title" :value="movie_title.pk" :key="movie_title.pk">
            <span>{{ movie_title.title }}</span>
          </option>
        </select> -->
      </div>
      <div>
        <label for="title">제목</label>
        <input type="text" id="title" v-model="newDrop.title">
      </div>
      <div>
        <label for="content">내용</label>
        <textarea id="content" cols="30" rows="10" v-model="newDrop.content"></textarea>
      </div>
      <div>
        <label for="user_vote">평점</label>
        <input type="number" id="user_vote" min="0" max="5" step="1" v-model="newDrop.user_vote">
      </div>
      <button>작성</button>
    </form>
    <!-- 모달  -->
    <div>
      <transition>
        <div id="search" class="modal" v-if="this.show">
          <div class="bg"></div>
            <div class="searchbar">
              <div class="flex explain">
                <p>영화를 검색해보아용</p>
                <button @click="toggleShow">닫기</button>
              </div>
              <input type="text" @keyup.enter="search">
              <div v-if="result_show">
                <li
                  v-for="result_movie in result"
                  :key="result_movie.pk"
                  @click="setMovieId(result_movie.pk, result_movie.title)">
                  {{ result_movie.title }}
              </li>
            </div>
          </div>
        </div>
      </transition>
    </div>  
  </div>

  


</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'DropCreate',
  props: {
    drop: Object,
    action: String,
    movies_title : Array,
  },
  data() {
    return {
      newDrop: {
        title: this.drop.title,
        content: this.drop.content,
        movie: this.drop.movie_id, // 영화 아이디(pk)
        user_vote: this.drop.user_vote,
        movies_title : this.$store.state.movies.movies_title
      },
      movietitle : null,
      show: false,
      inputValue: '',
      result: [],
      result_show: false,
      result_movie: ''
    }
  },

  methods: {
    ...mapActions(['createDrop', 'updateDrop']),
    onSubmit() {
      if (this.action === 'create') {
        this.createDrop(this.newDrop)
      } else if (this.action === 'update') {
        const payload = {
          dropPk: this.drop.id,
          ...this.newDrop,
        }
        this.updateDrop(payload)
      }
    },
    setMovieId(movieid, movietitle) {
      this.newDrop.movie = movieid
      this.result_movie = movietitle
    }, 
    toggleShow() {
      this.show = !this.show
      if (!this.show) {
        this.result = []
      }
    },
    search(event) {
      this.inputValue = event.target.value
      const movies = this.movies_title
      for (var movie of movies) {
        if (movie.title.includes(this.inputValue)) {
          this.result.push(movie)
        }
      }
      this.result_show = true
    },
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