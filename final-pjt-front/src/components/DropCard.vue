<template>
  <div class="video-list-item">
    <img :src="posterUrl" alt="포스터">
    <h3>{{ drop.title }}</h3>
    <p>{{ drop.content }}</p>
    <p>{{ drop.user.username }}</p>
    <p>총 drop 데이터 : {{ drop }}</p>
  </div>
</template>

<script>

export default {
  props: {
    drop: {
      type: Object,
      required: true,
    }
  },
  methods: {
  },
  computed: {
    posterUrl() {
      return 'https://image.tmdb.org/t/p/w500' + this.drop.movie.poster_path
    }
  }
}
</script>

<style scoped>
.video-list-item {
  margin: 1rem 0;
}

.video-list-item:hover {
  cursor: pointer;
  background-color: grey;
  color: white;
}
</style>