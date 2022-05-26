<template>
  <div>
    <v-text-field 
      label=">>댓글쓰기" 
      v-model="content"
      @keyup.enter="onSubmit"
      placeholder="댓글쓰기"
      >
    </v-text-field>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['drop']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ dropPk: this.drop.id, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>

</style>