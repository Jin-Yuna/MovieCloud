<template>
<div class="weather_container">
  <v-container class="mt-16">
    <v-card
      shaped
      :loading="loading"
      class="mx-auto mt-16"
      max-width="1300"
    >
      <template slot="progress">
        <v-progress-linear
          color="deep-purple"
          height="10"
          indeterminate
        ></v-progress-linear>
      </template>
      <v-img
        height="400"
        :src="posterUrl"
      ></v-img>
      <v-flex>
        <v-card-text class="my_card_title ma-5">{{ drop.title }}</v-card-text>
        <div v-show="drop.user.pk===this.$store.state.accounts.currentUser.pk" class="ma-7">
          <router-link :to="{ name: 'DropEditView', params: { dropPk } }">
            <button class="mr-3">수정하기</button>
          </router-link>
          <button @click="deleteDrop(dropPk)">삭제하기</button>
        </div>
      </v-flex>
      <v-card-text>
        <v-row
          align="center"
          class="mx-0"
        >
          <v-rating
            :value="drop.user_vote"
            color="amber"
            dense
            half-increments
            readonly
            size="25"
            class="ml-6"
          ></v-rating>
  
          <div class="grey--text ms-4">
            {{ drop.user_vote }}
          </div>
        </v-row>
  
        <div class="mt-6 ml-6 my_card_datas">
          {{ drop.movie.tagline }}
        </div>
        <router-link :to="{ name: 'ProfileView', params: {userPk:userpk} }">
          <h3 class="ml-7">{{drop.user.username}}</h3>
        </router-link> 
        <p class="ml-7">{{drop.created_at}}</p>
        
      </v-card-text>
  
      <v-divider class="mx-4"></v-divider>
      <v-flex class="justify-space-between">
        <p class="my_card_datas ma-7">{{ drop.movie.title }}을 보고</p>
        <p class="ma-6">{{ drop.movie.genres_name }}</p>
      </v-flex>
    
      <v-card-text class="my_card_content ml-3">
         {{ drop.content }}
      </v-card-text>
      <v-row
        align="center"
        justify="space-around"
        class="mt-10"
      >
        <v-btn
          @click="likeDrop(dropPk)"
          tile
          color="pink"
        >
          <v-icon left>
            mdi-heart
          </v-icon>
          {{ likeCount }}
        </v-btn>
      </v-row>
      <v-divider class="mx-4"></v-divider>
      <div class="ml-4">
        <CommentList :comments="reversedComments" />
      </div>
    </v-card>
  </v-container>
</div>  
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/Comments/CommentList.vue'

  export default {
    name: 'DropDetailView',
    components: {
      CommentList,
    },
    data() {
      return {
        dropPk: this.$route.params.dropPk,
      }
    },
    computed: {
      ...mapGetters(['drop']),
      posterUrl() {
        return 'https://image.tmdb.org/t/p/w500' + this.drop.movie.poster_path
      },
      likeCount() {
        return this.drop.like_users?.length
      },
      reversedComments() {
        const reversedComments = [...this.drop.comments].reverse();
        return reversedComments
      },
    },
    methods: {
      ...mapActions(['getDrop', 'deleteDrop', 'likeDrop', ])
    },
    created() {
      this.getDrop(this.dropPk)
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
  font-size: 55px;
  line-height: 63px;
  color: #425E7A;
}
.my_card_datas {
  width: 391px;
  height: 26px;

  font-family: 'LeferiBaseType-RegularA';
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 129.49%;
  color: #425E7A;
}
.my_card_content {
  font-size: 20px;
  line-height: 129.49%;
}

</style>
