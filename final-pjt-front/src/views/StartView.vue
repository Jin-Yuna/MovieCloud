<template>
<div class="background-image">
  <div class="gradient">
    <h1 class="logo_titile">MOVIE CLOUD</h1>
    <router-link class="login-link" :to="{ name: 'login' }">
      <img class="logo" 
      src="../assets/logo.png" 
      alt="로고이미지">
    </router-link>
  </div>
</div>
</template>

<script>
export default {

}
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
  left: 0px;
  top: 40px;
}
.logo_titile {
  white-space: nowrap; 
  position: absolute;
  width: 464px;
  height: 92px;
  left: calc(50% - 500px/2);
  top: calc(50% - 200px/2);

  font-family: 'Arial';
  font-weight: 700;
  font-size: 80px;
  line-height: 92px;
  /* identical to box height */

  display: flex;
  align-items: center;
  text-align: center;

  color: #425E7A;
  text-shadow: 0px 1px 5px rgba(0, 0, 0, 0.25)
}
.logo {
  position: absolute;
  width: 204px;
  height: 183px;
  left: calc(50% - 200px/2);
  top: 26%;
}
</style>