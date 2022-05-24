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
import drf from '@/api/drf'
import DropCard from '@/components/DropCard.vue'

export default {
  name: 'DropListView',
  components: {
    DropCard,
  },
  data() {
    return {
      drops : []
    }
  },
  methods: {

  },
  created() {

    axios({
      url: drf.drops.drops(),
      method: 'get',
    })
    .then(response => {
      this.drops = response.data
      })
  }
}
</script>

<style>

</style>