<template>
  <form @submit.prevent="onSubmit">
    <div>
      <label for="movie">영화</label>
      <select id="movie" v-model="newDrop.movie">
        <option v-for="movie_title in movies_title" :key="movie_title.pk">
          <p>{{ movie_title.pk }}</p>
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
      <input type="number" id="user_vote" min="0" max="5" step="0.5" v-model="newDrop.user_vote">
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
        movie: this.drop.movie_pk,
        user_vote: this.drop.user_vote,
        // movies_title : drop.movies_title,
      }
    }
  },

  methods: {
    ...mapActions(['createDrop', 'updateDrop']),
    onSubmit() {
      if (this.action === 'create') {
        this.createDrop(this.newDrop)
        // this.$store.actions.drops.createDrop(this.newDrop)
      } else if (this.action === 'update') {
        const payload = {
          dropPk: this.drop.id,
          ...this.newDrop,
        }
        this.updateDrop(payload)
      }
    },
  },
  created() {
  }
}
</script>

<style></style>