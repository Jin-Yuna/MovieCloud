<template>
  <div>
    <h2>새글쓰기</h2>
    <DropCreate />
  </div>
</template>

<script>

import DropCreate from '@/components/DropCreate.vue'
export default {
  name: 'DropCreateView',
  components: {
    DropCreate,
  },
  data() {
    return {
    }
  },

}
</script>

<style>

</style>