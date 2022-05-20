import axios from 'axios'
import VueCookies from 'vue-cookies'

const kakaoHeader = {
    'Authorization': '50634426dfc0150423190cbcb41d99e9',
    'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
};

const getKakaoToken = async (code) => {
    console.log('loginWithKakao');
    try {
        const data = {
            grant_type: 'authorization_code',
            client_id: '683d19aa3f66f6c7d4ca3b08f6f139ed',
            redirect_uri: 'http://localhost:8080/',
            code: code,
        };
        var esc = encodeURIComponent;
        var queryString = Object.keys(data).map(k => esc(k) + '=' + esc(data[k])).join('&')

        // console.log(queryString)
        // console.log(('https://kauth.kakao.com/oauth/token', queryString, { headers: kakaoHeader }))

        const result = await axios.post('https://kauth.kakao.com/oauth/token', queryString, { headers: kakaoHeader });
        // const result = await axios.post(`https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id=${data.client_id}&redirect_uri=${data.redirect_uri}&code=${data.code}`);
        // console.log('카카오 토큰', queryString);
        // console.log(result)

        const token_header = {
            'Token': result.data.access_token
        }
        const server_token = await axios.get(`http://localhost:8080/`, { headers: token_header });
        console.log(server_token)
        return result;

    } catch (e) {
        return e;
    }
};

const refreshToken = async () => {
    try {
        const { result } = (await axios.get('/refreshToken')).data;
        VueCookies.set('access-token', result.access_token);
        console.log('Refresh API 성공', result);
        return result;
    } catch (e) {
        console.log(e);
    }
}

export {
    getKakaoToken,
    refreshToken,
};