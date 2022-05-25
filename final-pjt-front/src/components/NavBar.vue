<template>
  <div>
    <!--  -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
      <div class="container-fluid">
        <router-link class="navbar-brand" :to="{ name: 'MovieHome' }">HOME</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'DropCreateView' }">새글쓰기</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'DropListView' }">글 목록</router-link>
            </li>
            <!-- 로그인, 프로필 -->
            <li class="nav-item" v-if="isLoggedIn">
              <router-link class="nav-link" :to="{ name: 'ProfileView', params: { pk } }">
                <div>
                  {{ currentUser.username }}'s page
                </div>
              </router-link>
            </li>
            <li class="nav-item" v-if="isLoggedIn">
              <router-link class="nav-link" :to="{ name: 'logout' }">Logout</router-link>
            </li>
            <li class="nav-item" v-if="!isLoggedIn">
              <router-link class="nav-link" :to="{ name: 'login' }">Login</router-link>
            </li>
            <li class="nav-item" v-if="!isLoggedIn">
              <router-link class="nav-link" :to="{ name: 'signup' }">Signup</router-link>
            </li>
            <!--  -->
            <li class="nav-item">
              <SearchBar />
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
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

<style>
body {
  padding-top: 20px;
}
</style>
