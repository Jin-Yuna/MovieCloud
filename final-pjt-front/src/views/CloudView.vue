<template>
  <div>
    <h1 v-if="profile.username">
      {{ profile.username }} 프로필
      </h1>
    <h1 v-else>
      {{ profile.nickname }} 프로필
    </h1>

    <h2>작성한 글</h2>

    <h2>좋아요 한 글</h2>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    if (!this.profile) {
      const payload = { userPk: this.$route.params.pk }
      this.fetchProfile(payload)
    }

  },
}

</script>

<style></style>
