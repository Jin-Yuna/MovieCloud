<template>
  <div class="video-list-item">
    <router-link :to="{ name: 'DropDetailView', params: {dropPk: droppk} }">
      <img :src="posterUrl" alt="포스터" class="img_size">  
      <h3>{{ drop.title }}</h3>
    </router-link>
    <router-link :to="{ name: 'ProfileView', params: {userPk:userpk} }">
      {{ username }}
    </router-link> 
  </div>
</template>

<script>

export default {
  props: {
    drop: {
      type: Object,
      required: true,
    },
    profilename: String,
    profilepk: Number,
  },
  methods: {
  },
  computed: {
    posterUrl() {
      return 'https://image.tmdb.org/t/p/w500' + this.drop.movie.poster_path
    },
    droppk() {
      let droppk = 0
      if (this.drop.pk) {droppk=this.drop.pk} else {droppk=this.drop.id}
      return droppk
    },
    userpk() {
      let userpk = 0
      if (this.drop.user) {userpk = this.drop.user.pk } else {userpk=this.profilepk}
      return userpk
    },
    username() {
      let username = ''
      if (this.drop.user) {username= this.drop.user.username} else {username=this.profilename}
      return username
    }
  }
}
</script>

<style scoped>
.img_size {
  width: 200px;
  height: 300px;
}
</style>