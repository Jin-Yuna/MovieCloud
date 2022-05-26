<template>
  <div class="comment-list">
    <CommentListItem
      v-for="comment in calData"
      :comment="comment"
      :key="comment.pk"
    />
    <div class="text-center">
    <CommentFrom />
    <v-pagination
      v-model="curPageNum"
      :length="numOfPages"
      circle
    ></v-pagination>
  </div>
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
  data() {
      return {
        listData: [],
        dataPerPage: 10,
        curPageNum: 1,
      }
    },
  computed: {
    startOffset() {
      return ((this.curPageNum - 1) * this.dataPerPage);
    },
    endOffset() {
      return (this.startOffset + this.dataPerPage);
    },
    numOfPages() {
      return Math.ceil(this.comments.length / this.dataPerPage);
    },
    calData() {
      return this.comments.slice(this.startOffset, this.endOffset)
    }
  }
}
</script>

<style>
.comment-list {
  border: 1px solid blue;
}
</style>