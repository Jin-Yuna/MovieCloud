<template>
  <div>
    <img :src="'https://image.tmdb.org/t/p/w500'+img" alt="">
  </div>
</template>

<script>
export default {
  props: {
    img: String,
  }
}
</script>

<style>

</style>