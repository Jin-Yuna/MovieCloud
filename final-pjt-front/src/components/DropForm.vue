<template>
  <form @submit.prevent="onSubmit">
    <!-- 수정할 때는 영화목록 선택 안보이게 함 -->
  
    <div v-if="isCreate"> 
      <label for="movie">영화</label>
      <select id="movie" v-model="newDrop.movie">
        <option v-for="movie_title in movies_title" :value="movie_title.pk" :key="movie_title.pk">
          <span>{{ movie_title.title }}</span>
        </option>
      </select>
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
        movies_title : this.drop.movies_title,
      },
      movietitle : null,
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
    getmovieid(movietitle) {
  // { "pk": 953233, "title": "말괄량이 길들이기" }
      if (this.action === 'create') {
        for (const movie in this.movies_title ) {
          if (movie.title === movietitle) {
            this.newDrop.movie = movie.pk
            console.log(movie.pk)
        }
      }    
      }
    },
  },
  computed : {
    isCreate() {
      return (this.action === 'create')
    },
  },
}
</script>

<style>
.display-none {
  display: none;
}
</style>