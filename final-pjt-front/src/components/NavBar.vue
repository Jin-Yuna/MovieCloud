<template>
  <v-app-bar fixed color="#F6FAFE" >
    <v-app-bar-title>
      <router-link class="logo-title" :to="{ name: 'MovieHome' }">MOVIE CLOUD</router-link>
    </v-app-bar-title>
    <v-app-bar-nav-icon>
        <router-link :to="{ name: 'MovieHome' }">
          <img class="logo-image" 
          src="../assets/logo.png" 
          alt="로고이미지">
      </router-link>
    </v-app-bar-nav-icon>
    <v-spacer></v-spacer>
    <ul>
      <li>
        <router-link :to="{ name: 'MovieHome' }" class="link-to">MOVIE</router-link>
      </li>
      <li>
        <router-link :to="{ name: 'DropListView' }" class="link-to">CLOUD</router-link>
      </li>
      <li>
        <router-link :to="{ name: 'ProfileView', params: { pk } }" 
        v-if="isLoggedIn" classs="link-to">{{ currentUser.username }}'S CLOUD</router-link>
      </li>
    </ul>
    <SearchBar />
    <div class="btn-group">
      <router-link :to="{ name: 'login' }" v-if="!isLoggedIn">
        <v-btn color="#F6FAFE">Login</v-btn>
      </router-link>
      <router-link :to="{ name: 'logout' }" v-if="isLoggedIn" class="logout-link"><v-btn dark color="#1A2940">Logout</v-btn></router-link>
    </div>
  </v-app-bar>
</template>

<script>
  import { mapGetters } from 'vuex'
  import SearchBar from '@/components/SearchBar'
  
  export default {
    name: 'NavBar',
    components: {
      SearchBar,
    },
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      
      pk() {
        return this.currentUser.pk ? this.currentUser.pk : 'guest'
      },
    },
  }
</script>

<style scoped>
.logo-title {
  margin-left: 450px;
  font-family: 'Arial';
  font-weight: 700;
  font-size: 30px;
  text-decoration: none;
  color: #1A2940;
  line-height: 34px;
  margin-right: 10px;
} 
.logo-image{
  width: 55px;
 }
 ul {
   list-style: none;
   display: flex;
 }
 li {
   margin: 10px;
 }
a {
  font-family: 'LeferiBaseType-RegularA';
  color: #1A2940;
  text-decoration: none;
}
a:visited {
  color: #1A2940;
  text-decoration: none;
}
 .link-to {
  font-family: 'LeferiBaseType-RegularA';
  color: #1A2940;
  font-weight: 700;
  font-size: 20px;
 }
 .btn-group {
   margin-right: 450px;
 }
 .logout-link {
    font-family: 'LeferiBaseType-RegularA';
    color: #F6FAFE;
    text-decoration-line: none;
 }
</style>
