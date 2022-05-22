<template>
  <div>
    <h1>게시판</h1>
    <DropCard
      v-for="drop in drops"
      :key="drop.id"
      :drop="drop"
    />
  </div>
</template>

<script>
import axios from 'axios'
import DropCard from '@/components/DropCard.vue'

export default {
  name: 'DropList',
  components: {
    DropCard,
  },
  data() {
    return {
      drops : []
    }
  },
  created() {
    axios.get('http://127.0.0.1:8000/drops/cards/')
      .then(response => {
        this.drops = response.data
      })
  }
}
</script>

<style>

</style>