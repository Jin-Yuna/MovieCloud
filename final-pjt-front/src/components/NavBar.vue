<template>
  <nav>
    <ul>
      <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'login' }">Login</router-link>
      </li>
      <li v-if="!isLoggedIn">
        <router-link :to="{ name: 'signup' }">Signup</router-link>
      </li>
      <li v-if="isLoggedIn">
        <router-link :to="{ name: 'ProfileView', params: { pk } }">
          <div>
            {{ currentUser.username }}'s page
          </div>
 
        </router-link>
      </li>
      <li v-if="isLoggedIn">
        <router-link :to="{ name: 'logout' }">Logout</router-link>
      </li>
      <li>
        <router-link :to="{ name: 'DropListView' }">글 목록</router-link>
      </li>
      <li>
        <router-link :to="{ name: 'DropCreateView' }">새글쓰기</router-link>
      </li>
      <SearchBar />
      <li>
        <router-link :to="{ name: 'MovieHome' }">HOME</router-link>
      </li>
    </ul>
  </nav>
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

<style></style>
