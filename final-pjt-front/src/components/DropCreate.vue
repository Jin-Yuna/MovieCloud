<template>
  <form @submit="createArticle">
    <h2>새글쓰기</h2>
    <div>
      <label for="movie">영화</label>
      <select id="movie" v-model="movie_pk">
        <option v-for="movie_title in movies_title" :key="movie_title.pk">
          <p>{{ movie_title.pk }}</p>
        </option>
      </select>
    </div>
    <div>
      <label for="title">제목</label>
      <input type="text" id="title" v-model="title">
    </div>
    <div>
      <label for="content">내용</label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea>
    </div>
    <div>
      <label for="user_vote">평점</label>
      <input type="number" id="user_vote" min="0" max="5" step="0.5" v-model="user_vote">
    </div>
    <button>새글쓰기</button>
  </form>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      title: '',
      content: '',
      movie: null,
      user_vote: '',
      movie_pk: null,
      movies_title: [],
    }
  },
  created() {
    axios.get('http://127.0.0.1:8000/movies/get_movie_title/')
      .then(response => {
        this.movies_title = response.data
      // movie_id와 title 가져옴
      })
  },
  methods: {
    createArticle(event) {
      event.preventDefault()
      const data = {
        title: this.title,
        content: this.content,
        movie: this.movie_pk,
        user_vote: this.user_vote,
      }
      const config = {
        headers: {
          Authorization: `Token ${this.$store.state.accounts.token}`
        }
      }
      axios.post('http://127.0.0.1:8000/drops/new/', data, config)
        .then(response => {
          console.log(response.data)
          // 글 작성 완료하면 게시판으로 이동
          this.$router.push({ name: 'DropListView' })
        })
    }
  }

}
</script>

<style>
.hide {
  display: none !important;	/* 사용자가 아무것도 입력하지 않았을 때 검색창을 숨기는 용도*/
}

.rel_search {
  display:flex;
  flex-direction:column;
  justify-content : space-around;
  border: 1px solid red;
  border-radius: 12px;
 
}

.pop_rel_keywords {
  list-style: none;
  margin-right: 30%;

}

.pop_rel_keywords > li {	/* JS에서 동적으로 li를 생성할 때 적용될 스타일*/
  line-height : 250%
}
</style>