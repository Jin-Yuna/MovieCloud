<template>
  <div>
    <div class="container">
      <h2>새글쓰기</h2>
      <DropForm :drop="drop" :movies_title="movies_title" action="create"/>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
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
      movies_title: this.$store.state.movies.movies_title,
    }
  },
  methods: {
    ...mapActions(['setMoviesTitle']),
  },
  created() {
    if (!this.movies_title.length) {
      this.setMoviesTitle()
    }
    
  },
}
</script>

<style>

</style>