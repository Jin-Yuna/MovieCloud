import axios from 'axios'

const kakaoHeader = {
    'Authorization': process.env.VUE_APP_KAKAO_ADMIN_API_KEY,
    'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
};

// 토큰 받아오기
const getKakaoToken = async (code) => {
    try {
        const data = {
            grant_type: 'authorization_code',
            client_id: process.env.VUE_APP_KAKAO_REST_API_KEY,
            redirect_uri: 'http://localhost:8080/kakaoLogin',
            code: code,
        };
        var esc = encodeURIComponent;
        var queryString = Object.keys(data).map(k => esc(k) + '=' + esc(data[k])).join('&')

        const result = await axios.post('https://kauth.kakao.com/oauth/token', queryString, { headers: kakaoHeader })
        return result;

    } catch (e) {
        return e;
    }
}

export {
    getKakaoToken,
}