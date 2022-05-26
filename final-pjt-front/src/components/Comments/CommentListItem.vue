<template>
  <div class="comment-list-item">
    <span v-if="!isEditing">{{ payload.content }} | {{ comment.user.username }}</span>
    <span v-if="isEditing">
    <v-flex>
      <v-text-field @keyup.enter="onUpdate" type="text" v-model="payload.content"></v-text-field>
      <button @click="onUpdate">수정 |</button>
      <button @click="switchIsEditing">&nbsp;취소</button>
    </v-flex>
    </span>
    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <v-btn
        @click="switchIsEditing"
        class="mx-2"
        fab
        dark
        x-small
        color="cyan"
      >
        <v-icon dark>
          mdi-pencil
        </v-icon>
      </v-btn>
      <v-btn
        @click="deleteComment(payload)"
        class="mx-2"
        fab
        dark
        x-small
        color="cyan"
      >
        <v-icon dark>
          mdi-minus
        </v-icon>
      </v-btn>
    </span>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        dropPk: this.comment.drop,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.$store.dispatch('updateComment', this.payload )
      this.isEditing = false
    }
  },
  created() {

  }

}
</script>

<style scoped>

</style>