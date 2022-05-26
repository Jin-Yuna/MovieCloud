<template>
  <div class="weather_container">
  <v-container class="mt-16">
    <div class="mt-16">
      <div v-if="profile.pk===currentUser.pk">
        <h1 class="my_card_title">Hi {{ profile.username }}!</h1>
      </div>
      <div v-else>
        <h1 class="my_card_title">{{ profile.username }}</h1>
        <v-row
          align="center"
          justify="end"
          class="mr-4"
          @click="follow({userPk : profile.pk}); buttonchange()"
        >
          <v-btn
            tile
            color="amber darken-1"
            v-if="followed"
          >
            <v-icon left>
              mdi-star
            </v-icon>
            팔로우중
          </v-btn>
          <v-btn
            tile
            color="grey lighten-1"
            v-else
          >
            <v-icon left>
              mdi-star
            </v-icon>
            팔로우
          </v-btn>
        </v-row>
        <span>팔로워 수 : {{ profile.followers.length }}</span>
      </div>
      <h2 v-if="profile.followings.length"> 팔로우 목록 : {{ profile.followings }}</h2>  
      <v-tab class="mt-16">
        <v-badge
          color="blue darken-1"
          :content="profile.drops.length"
        >
          <h2 class="my_card_datas">작성한 글</h2>
        </v-badge>
      </v-tab>
  
  <!--  -->
      <v-sheet
        class="mx-auto"
        elevation="8"
        max-width="120em"
        back
        color="transparent"
      >
        <v-slide-group
          v-model="model"
          class="pa-4"
          show-arrows
        >
          <v-slide-item
            v-for="drop in profile.drops "
            :key="drop.pk"
            v-slot="{ toggle }"
          >
            <v-card
              class="ma-4"
              height="290"
              width="200"
              @click="toggle"
            >
            <DropCard 
              :drop = drop
              :profilename="profile.username"
              :profilepk="profile.pk"
            />
            </v-card>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>


      <v-tab class="mt-16">
        <v-badge
          color="blue darken-1"
          :content="profile.like_drops.length"
        >
          <h2 class="my_card_datas">좋아요한 글</h2>
        </v-badge>
      </v-tab>
      <v-sheet
        class="mx-auto"
        elevation="8"
        max-width="120em"
        color="transparent"
      >
        <v-slide-group
          v-model="model"
          class="pa-4"
          active-class="success"
          show-arrows
        >
          <v-slide-item
            v-for="drop in profile.like_drops "
            :key="drop.pk"
            v-slot="{ toggle }"
          >
            <v-card
              class="ma-4"
              height="290"
              width="200"
              @click="toggle"
            >
            <DropCard 
              :drop = drop
              :profilename="profile.username"
              :profilepk="profile.pk"
            />
            </v-card>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>
    </div>
  </v-container>
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
      followed : false,
      model: null,
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
    created() {
      if (!this.profile) {
        const payload = { userPk: this.$route.params.userPk }
        this.fetchProfile(payload)
      } 
    },
    buttonchange() {
      this.followed = !this.followed
    }
  },
  created() {
    console.log(this.$route.params.pk )
    this.fetchProfile({userPk:this.$route.params.pk })
    if (!this.profile) {
      const payload = { userPk: this.$route.params.pk }
      this.fetchProfile(payload)
    }
  },
  mounted() {
    this.isFollowed()
  },
}





</script>

<style scoped>
.weather_container {
  background: linear-gradient(to top, #BBDEFB, #ffffff);
  height: 100vh;
  background-size: cover;
}
.my_card_title {
  /* left: calc(50% - 481px/2 - 298.5px);
  top: calc(50% - 63px/2 - 1298px); */
  font-family: 'LeferiPoint-BlackA';
  font-style: normal;
  font-weight: 700;
  font-size: 80px;
  line-height: 63px;
  color: #425E7A;
}
.my_card_datas {
  font-family: 'LeferiPoint-BlackA';
  font-style: normal;
  font-weight: 700;
  font-size: 40px;
  line-height: 63px;
  color: #425E7A;
}

</style>
