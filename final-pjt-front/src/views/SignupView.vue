<template>
  <div class="signup">
    <div class="page-container">
      <div class="signup-form-container shadow">
        <div class="signup-form-real-jjin">
          <img class="logo" 
              src="../assets/logo.png" 
              alt="로고이미지">
            <h1>회원가입</h1>
            <p>회원가입시 서비스 이용이 가능합니다</p>
 
            <form class="signup-input-container" @submit.prevent="signup(credentials)">
              <v-text-field
                label="아이디"
                prepend-inner-icon="mdi-account"
                color="#1A2940" v-model="credentials.username" type="text" id="username" required />
              <v-text-field
                  prepend-inner-icon="mdi-lock"
                  type="password1"
                  label="비밀번호" 
                  color="#1A2940" v-model="credentials.password1" id="password1" required />
              <v-text-field
                  prepend-inner-icon="mdi-lock"
                  type="password2"
                  label="비밀번호 확인" 
                  color="#1A2940" v-model="credentials.password2" id="password2" required  />
              <div class="wrong-alert">
                <account-error-list v-if="authError"></account-error-list>
              </div>
              <v-btn class="signup-button" type="submit" large
                    block
                    dark>회원가입</v-btn>
              </form>
            <button class="kakaologin" @click="kakaoLogin"><img class="kakaologin-img" src="../assets/kakao_login_medium_wide.png"></button>
            <transition name="fade" mode="out-in"> 
              <div class="go-to-signup">
              <router-link class="login-link" :to="{ name: 'login' }">이미 회원이신가요?</router-link>
              </div>
            </transition>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup']),
      kakaoLogin() {
        const params = {
          redirectUri:'http://localhost:8080/kakaoLogin',
        }
        window.Kakao.Auth.authorize(params)
      }
    },
  }
</script>

<style scoped>
.signup {
  background-color: #1A2940;
  height: 100vh;
}
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
.signup-form-container{
    /* background:linear-gradient(90.04deg, #BBDEFB 0.05%, #F6FAFE 99.97%); */   
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0px 4px 5px rgba(0, 0, 0, 0.5) ;
    border-radius: 28px;
}
.shadow{
    -webkit-box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
    -moz-box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
    box-shadow: 27px 43px 43px -26px rgba(89,89,89,0.39);
}
.signup-form-real-jjin{
    width: 50%; 
    height: 70%;
    border-radius: 28px;
    padding:75px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color:#1A2940;
    background: linear-gradient(176.69deg, #BBDEFB 1.71%, #D4EAFC 36.3%, #F6FAFE 98.2%);
}
.signup-form-real-jjin .logo {
  width: 117px;
  height: 105px;
  top: 26%;
}
.signup-form-real-jjin h1{
    font-family: 'LeferiPoint-BlackA';
    font-style: normal;
    font-weight: 700;
    font-size: 40px;
    line-height: 46px;
    color: #1A2940;
    width:100%;
    text-align: center;
}
.signup-form-real-jjin p{
    font-family: 'LeferiBaseType-RegularA';
    font-weight: 400;
    font-size: 15px;
    line-height: 129.49%;
    color: #1A2940;
    padding-top: 10px;
}
.signup-input-container{
    width: 310.5px;
}
.signup-input-container .login-input-wrap{
    width: 310.5px;
    height: 45px;
    margin-top: 20px;
    border-radius: 2px;
    border-bottom: 3px solid #1A2940;
    /* box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25); */
}
.password {
  margin-left: 0.2em;
  margin-bottom: 0.2em;
}
.signup-input-container .login-input-wrap input{
    background: none;
    border: none;
    line-height: 45px;
    padding-left:10px;
}
.signup-input-container .login-input-wrap input:focus{
    outline: none;
}
.signup-btn-wrap{
    margin-top: 18px;
    align-items: center;
}
.signup-button {
  margin-top: 10px;
  margin-bottom: 0;
  color:white;
  font-family: 'LeferiBaseType-RegularA';
  font-size: 16px;
  border: 0;
  border-radius: 7px;
  background: #1A2940;;
  background: linear-gradient(162deg, #1A2940 0%, rgb(56, 77, 110) 50%, #1A2940 100%);
}
.kakaologin {
  margin-top: 15px;

  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
  border: none;
  background: none;
  outline: none;
}
.kakaologin-img {
  width: 310px;
  height: 45px;
}
.go-to-signup{
  margin-top: 70px;
  font-family: 'LeferiPoint-WhiteA';
  font-weight: 400;
  font-size: 14px;
  line-height: 129.49%;
  display: flex;
  align-items: center;
  text-align: center;
  text-decoration: none;
  text-decoration-line: underline;
  color: #1A2940;
}
a:visited {
  color: #1A2940;
}
.fade-enter {
  opacity: 0;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease-out;
}
.fade-leave-to {
  opacity: 0;
}
</style>
