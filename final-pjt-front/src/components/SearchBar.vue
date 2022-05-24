<template>
<div>
  <transition>
  <search v-if="show"><input type="text" @set-input-value="setInputValue"></search>
   </transition>
  <button @click="toggleShow">검색 아이콘</button>
</div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'SearchBar',
  data() {
    return {
      show: false
    }
  },
  computed: {
    ...mapGetters('movieSearchList')
  },
  created() {
    this.$store.dispatch('get_movies_search')
  },
  methods: {
    toggleShow() {
      this.show = !this.show
    },
  }
}
</script>

<style>
.v-enter-active, .v-leave-active {
  transition: opacity 1s;
}
/* 더 이상 보이게 되지 않았을 때의 투명도 */
.v-enter, .v-leave-to {
  opacity: 0;
}
</style>