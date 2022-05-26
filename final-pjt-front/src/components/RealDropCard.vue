<template>
  <div class="video-list-item">
    <router-link :to="{ name: 'DropDetailView', params: {dropPk: droppk} }">
      <img :src="posterUrl" alt="포스터" class="drop">  
      <h3 class="overflow-x-hidden">{{ drop.title }}</h3>
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
    },
  }
}
</script>

<style scoped>
/* .img_size {
  width: 200px;
  height: 300px;
  filter: blur(1px);
} */
.drop {
  width: 120px;
  height: 120px;
  border-radius: 80% 0 55% 50% / 55% 0 80% 50%;
  border: 60px solid #BBDEFB;
  transform: rotate(-45deg);
  margin-top: 20px;
  overflow: hidden;
}

.drop:hover {
  border: 1px solid black;
  filter: blur(0px);
}
h3 {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 100px;
  height: 23px;
}

</style>