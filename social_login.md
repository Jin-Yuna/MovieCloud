**카카오**

https://developers.kakao.com/docs/latest/ko/kakaologin/common

REST API 키 : 683d19aa3f66f6c7d4ca3b08f6f139ed

Javascript 키 : fcf79d7950891e2a0bcbec183a0187dd

Admin 키 : 50634426dfc0150423190cbcb41d99e9



- flow

  1. 인증 코드 요청 (javascript SDK)

  2. 받은 인증 코드를 통해 토큰 요청 (REST API)

     ![캡처](social_login.assets/캡처.PNG)

     

- 구현 방법

  - **index.html에 javascript SDK 코드 삽입**

    ```html
    <script src="https://developers.kakao.com/sdk/js/kakao.js"></script>
    ```

    SDK?

    SDK란 Software Development Kit의 약자로, 소프트웨어 개발 도구 모음

    SDK는 API, IDE, 문서, 라이브러리, 코드 샘플 및 기타 유틸리티가 포함될 수 있음

    SDK는 프로그램 및 응용 프로그램 개발의 복잡성을 줄이는 강력한 기능 집합

  - **kakao javascript 키 설정 - main.js**

    ```JS
    window.Kakao.init('Javascript 키);
    ```

  - **카카오 인증 코드 요청 - views/KakaoLoginView.vue**

    ```JS
    loginWithKakao() {
                const params = {
                    redirectUri: "http://localhost:8080/auth",
                };
                window.Kakao.Auth.authorize(params);
            },
    ```

    => **인증코드에 받는 데 성공하면 redirectUri에 설정한 페이지로 이동하며, 쿼리에 인증 코드 정보가 담겨있음**

    여기서, 내가 지정해놓은 redirect uri를 잘못 작성해 토큰을 받는 uri로 redirect 되지 못해서 토큰을 받지 못함. 

    => 지정한 uri에 따라 views/KakaoLoginTokenView.vue로 redirect됨

  - **해당 인증코드를 들고 토큰 요청-  services/login.js**

    ```js
    const kakaoHeader = {
        'Authorization': '50634426dfc0150423190cbcb41d99e9',
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    };
    
    const getKakaoToken = async (code) => {
        try {
            const data = {
                grant_type: 'authorization_code',
                client_id: '683d19aa3f66f6c7d4ca3b08f6f139ed',
                redirect_uri: 'http://localhost:8080/',
                code: code,
            };
            var esc = encodeURIComponent;
            var queryString = Object.keys(data).map(k => esc(k) + '=' + esc(data[k])).join('&')
    
            const result = await axios.post('https://kauth.kakao.com/oauth/token', queryString, { headers: kakaoHeader });
            const token_header = {
                'Token': result.data.access_token
            }
    
            const server_token = await axios.get(`http://localhost:8080/`, { headers: token_header });
            return result;
        } catch (e) {
            return e;
        }
    };
    ```

    => 토큰 받아옴

    => 실수

    1. 인가 코드를 Query String으로 전달받지 않아 몇 번이고 오류 발생 ⇒ 문서 잘보기
    2. uri를 통해 요청 보내는 데는 성공하지만 400 에러 발생 ⇒ 재로그인으로 해결 ( 새로운 인가코드 반영 x )
