const HOST = 'http://127.0.0.1:8000/'

const ACCOUNTS = 'accounts/'

const DROPS = 'drops/'
const COMMENTS = 'comments/'
const WEATHER = 'weathers/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',

    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: userPk => HOST + 'profile/' + `${userPk}/`,
    follow: userPk => HOST + 'follow/' + `${userPk}/`,
  },
  drops: {
    newDrop: () => HOST + DROPS + 'new/',
    drops: () => HOST + DROPS + 'list/',
    drop: dropPk => HOST + DROPS + `${dropPk}/`,
    likeDrop: dropPk => HOST + DROPS + `${dropPk}/` + 'like/',
    comments: dropPk => HOST + DROPS + `${dropPk}/` + COMMENTS,
    comment: (dropPk, commentPk) => HOST + DROPS + `${dropPk}/` + COMMENTS + `${commentPk}/`,
  },
  weathers: {
    weather: (weatherPk) => HOST + WEATHER + `${weatherPk}/`
  }

}
