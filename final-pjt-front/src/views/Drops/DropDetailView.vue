<template>
  <div>
    <h2>{{ drop.title }}</h2>
    <img :src="posterUrl" alt="포스터">
    <p>{{ drop.user }}</p>
    <div v-if="drop.user.pk===this.$store.state.accounts.currentUser.pk">
      <router-link :to="{ name: 'DropEditView', params: { dropPk } }">
        <button>Edit</button>
      </router-link>
      <button @click="deleteDrop(dropPk)">Delete</button>
    </div>
    <div>
      좋아요:
      <button
        @click="likeDrop(dropPk)"
      >{{ likeCount }}</button>
    </div>
    <CommentList :comments="drop.comments" />
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/Comments/CommentList.vue'

  export default {
    name: 'DropDetailView',
    components: {
      CommentList,
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
      likeCount() {
        return this.drop.like_users?.length
      }
    },
    methods: {
      ...mapActions(['getDrop', 'deleteDrop', 'likeDrop', ])
    },
    created() {
      this.getDrop(this.dropPk)
    },
  }
</script>

<style></style>
