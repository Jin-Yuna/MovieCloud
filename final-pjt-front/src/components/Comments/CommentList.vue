<template>
  <div class="comment-list">
    <CommentListItem
      v-for="comment in comments"
      :comment="comment"
      :key="comment.pk"
    />
    <CommentFrom />
  </div>
</template>

<script>
import CommentFrom from '@/components/Comments/CommentForm.vue'
import CommentListItem from '@/components/Comments/CommentListItem.vue'

export default {
  name: 'CommentList',
  components: {
    CommentFrom,
    CommentListItem,
  },
  props: { comments: Array },
}
</script>

<style>
.comment-list {
  border: 1px solid blue;
}
</style>