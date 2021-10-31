import Cookies from 'js-cookie'

export default {

  setCookie(data) {
    Cookies.set('org_session', data)
  }

}
