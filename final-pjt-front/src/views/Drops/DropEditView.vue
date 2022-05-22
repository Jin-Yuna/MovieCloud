<template>
  <div>
    <h1>글 수정하기</h1>
    <DropForm v-if="drop" :drop="drop" :movies_title="movies_title" action="update" />
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
    created() {
      this.getDrop(this.$route.params.dropPk)
      axios.get('http://127.0.0.1:8000/movies/get_movie_title/')
      .then(response => {
        this.movies_title = response.data
    })
    },

  }
</script>

<style></style>
