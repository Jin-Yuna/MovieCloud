<template>
  <div>
    <DropCreate />
    <h1>게시판</h1>
    <div v-for="drop in drops" :key="drop.id">
      {{ drop }} -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import DropCreate from '@/components/DropCreate.vue'

export default {
  name: 'DropList',
  components: {
    DropCreate,
  },
  data() {
    return {
      drops : []
    }
  },
  created() {
    const config = {
      headers: {
        Authorization: `Token ${this.$store.state.token}`
      }
    }
    axios.get('http://127.0.0.1:8000/drops/', config)
      .then(response => {
        this.drops = response.data
      })
  }
}
</script>

<style>

</style>