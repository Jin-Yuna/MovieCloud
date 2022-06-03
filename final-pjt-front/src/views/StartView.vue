<template>
<div class="background-image">
  <div class="gradient">
    <router-link class="login-link" :to="{ name: 'login' }">
      <img class="logo"
      src="../assets/logo.png" 
      alt="로고이미지">
    </router-link>
    <h1 class="logo_title">MOVIE CLOUD</h1>
  </div>
</div>
</template>

<script>

</script>

<style scoped>
.background-image {
  height: 100vh;
  background-image: url('../assets/background.png');
  background-repeat: no-repeat;
  background-size: cover; 
}
.gradient {
  background: linear-gradient(90.04deg, rgba(219, 202, 255, 0.5) 0.05%, rgba(250, 246, 254, 0.5) 99.97%);
  width: 100%;
  height: 100%;
}
.logo_title {
  position: absolute;
  left: calc(50% - 500px/2);
  top: 42%;

  font-family: 'Arial';
  font-weight: 700;
  font-size: 80px;
  line-height: 92px;

  color: #425E7A;
  text-shadow: 0px 1px 5px rgba(0, 0, 0, 0.25)
}
.logo {
  position: relative;
  width: 204px;
  height: 183px;
  left: calc(50% - 200px/2);
  top: 30%;
}
</style>