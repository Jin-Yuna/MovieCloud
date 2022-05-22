<template>
  <div>
    <h2>새글쓰기</h2>
    <DropForm :drop="drop" :movies_title="movies_title" action="create"/>
  </div>
</template>

<script>
import axios from 'axios'
import DropForm from '@/components/DropForm.vue'
export default {
  name: 'DropCreateView',
  components: {
    DropForm,
  },
  data() {
    return {
      drop: {
        title: '',
        content: '',
        movie: null,
        user_vote: 0,
        // movie_pk: null,
      },
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
}
</script>

<style>

</style>