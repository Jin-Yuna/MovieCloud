<template>
  <div>
    <h2>{{ drop.title }}</h2>
    <img :src="posterUrl" alt="포스터">
    <p>{{ drop.user }}</p>
    <div v-if="drop.user.pk=this.$store.state.accounts.currentUser.pk">
      <router-link :to="{ name: 'DropEditView', params: { dropPk } }">
        <button>Edit</button>
      </router-link>
      <!-- <button @click="deleteArticle(articlePk)">Delete</button> -->
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'DropDetailView',
    components: {

    },
    data() {
      return {
        dropPk: this.$route.params.dropPk,
      }
    },
    computed: {
      ...mapGetters(['drop']),
      posterUrl() {
        return 'https://image.tmdb.org/t/p/w500' + this.drop.movie.poster_path
      },
    },
    methods: {
      ...mapActions([
        'getDrop',
      ])
    },
    created() {
      this.getDrop(this.dropPk)
    },
  }
</script>

<style></style>
