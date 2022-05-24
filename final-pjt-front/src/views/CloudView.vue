<template>
  <div>
    <div v-if="profile.pk===currentUser.pk">
      <h1> 나의 프로필</h1>
    </div>
    <div v-else>
      <h1 v-if="profile.username">
        {{ profile.username }} 프로필
      </h1>
      <h1 v-else>
        {{ profile.nickname }} 프로필
      </h1>
      <button @click="follow({userPk : profile.pk}); buttonchange()">
        <span v-if="followed">팔로우취소</span>
        <span v-else>팔로우</span>
      </button>
      <span>팔로워 수 : {{ profile.followers.length }}</span>
    </div>
    <h2 v-if="profile.followings.length"> 팔로우 목록 : {{ profile.followings }}</h2>
    
    <h2>작성한 글</h2>

    <div class="flex">
      <DropCard
        v-for="drop in profile.drops"
        :key="drop.pk"
        :drop="drop"
        :profilename="profile.username"
        :profilepk="profile.pk"
      />
    </div>
    <h2>좋아요한 글</h2>
    <div class="flex">
      <DropCard
        v-for="like_drop in profile.like_drops"
        :key="like_drop.pk"
        :drop="like_drop"
        :profilename="profile.username"
        :profilepk="profile.pk"
      />
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import DropCard from '@/components/DropCard.vue'
export default {
  name: 'ProfileView',
  components: {
    DropCard,
  },
  data() {
    return{
      currentUser: this.$store.state.accounts.currentUser,
      followed : false
    }
  },
  computed: {
    ...mapGetters(['profile']),
    
  },
  methods: {
    ...mapActions(['fetchProfile', 'follow']),
    // 팔로우 확인이 가능하긴 한데 새로고침 두번 해야함....
    isFollowed() {
      this.followed = this.profile.followers.includes(this.currentUser.pk)
    },
    buttonchange() {
      this.followed = !this.followed
    }
  },
  created() {

    this.fetchProfile({userPk:this.$route.params.pk })
    if (!this.profile) {
      const payload = { userPk: this.$route.params.userPk }
      this.fetchProfile(payload)
    }
  },
  mounted() {
    this.isFollowed()
  },
}

</script>

<style>
.flex {
  display: flex;
}
</style>
