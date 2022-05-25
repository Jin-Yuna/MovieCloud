<template>
  <div class="login">
    <div class="page-container">
      <div class="login-form-container shadow">
        <div class="login-form-real-jjin">
            <img class="logo" 
              src="../assets/logo.png" 
              alt="로고이미지">
            <h1>로그인</h1>
            <p>WELCOME!</p>
            <form class="login-input-container" @submit.prevent="login(credentials)">
              <div class="login-input-wrap input-id">
                <img class="usericon" src="../assets/loginusericon.svg" alt="로그인 유저 아이콘">
                <input v-model="credentials.username" placeholder="아이디"  type="text" id="username" required />         
              </div>
              <div class="login-input-wrap input-password">
                <img class="password" src="../assets/passwordicon.svg" alt="패스워드 아이콘">
                <input v-model="credentials.password" placeholder="비밀번호" type="password" id="password" required />
              </div>
              <!-- <div class="wrong-alert">
                <account-error-list v-if="authError"></account-error-list>
              </div> -->
              <div class="login-btn-wrap"><button class="login-button">Login</button></div>
            </form>
            <button class="kakaologin" @click="kakaoLogin"><img class="kakaologin-img" src="../assets/kakao_login.png"></button>
            <div class="go-to-signup"><a href="/signup">처음 오셨나요?</a></div>
          </div>
        </div>
    </div>
  </div>
</template>

<script>
  import { mapActions } from 'vuex'
  // import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      // AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        },
        data: null,
      }
    },
  computed: {
      // ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login']),
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
.login {
  background-color: #425E7A;
  height: 100vh;
}
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}
.login-form-container{
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
.login-form-real-jjin{
    width: 50%; 
    height: 70%;
    border-radius: 28px;
    padding:75px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color:#425E7A;
    background: linear-gradient(176.69deg, #BBDEFB 1.71%, #D4EAFC 36.3%, #F6FAFE 98.2%);
}
.login-form-real-jjin .logo {
  width: 117px;
  height: 105px;
  top: 26%;
}
.login-form-real-jjin h1{
    font-family: 'LeferiPoint-BlackA';
    font-style: normal;
    font-weight: 700;
    font-size: 40px;
    line-height: 46px;
    color: #425E7A;;
    width:100%;
    text-align: center;
}
.login-form-real-jjin p{
    font-family: 'LeferiBaseType-RegularA';
    font-weight: 400;
    font-size: 15px;
    line-height: 129.49%;
    color: #425E7A;
    padding-top: 10px;
}
.login-input-container{
    width: 310.5px;
}
.login-input-container .login-input-wrap{
    width: 310.5px;
    height: 45px;
    margin-top: 20px;
    border-radius: 2px;
    border-bottom: 3px solid #425E7A;
    /* box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25); */
}
.password {
  margin-left: 0.2em;
  margin-bottom: 0.2em;
}
.login-input-container .login-input-wrap input{
    background: none;
    border: none;
    line-height: 45px;
    padding-left:10px;
}
.login-input-container .login-input-wrap input:focus{
    outline: none;
}
.login-btn-wrap{
    margin-top: 18px;
    align-items: center;
}
.login-button {
  margin-left: 53px;
  margin-bottom: 3px;
  width: 202px;
  height: 52px;
  color:white;
  font-family: 'LeferiBaseType-RegularA';
  font-size: 18px;
  border: 0;
  border-radius: 7px;
  background: #425E7A;;
  background: linear-gradient(162deg, #425E7A 0%, rgb(56, 77, 110) 50%, #425E7A 100%);
}
.kakaologin {
  margin-top: 0;
  height: 100%;
  width: 100%;
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
  border: none;
  background: none;
  outline: none;
}
.kakaologin-img {
  width: 202px;
  height: 52px;
}
.go-to-signup{
  margin-top: 40px;
  font-family: 'LeferiPoint-WhiteA';
  font-weight: 400;
  font-size: 14px;
  line-height: 129.49%;
  display: flex;
  align-items: center;
  text-align: center;
  text-decoration: none;
  text-decoration-line: underline;
  color: #425E7A;
}

</style>
