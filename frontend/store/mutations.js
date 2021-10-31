export default {
  SET_USER(state, user) {
    state.user = user
  },
  AUTH_SUCCESS(state, message) {
    state.alert = {
      success: true,
      message,
    }
  },
  AUTH_ERROR(state) {
    state.alert = {
      success: false,
      message: 'Error authenticating you'
    }
  },
  REG_ERROR(state) {
    state.alert = {
      success: false,
      message: 'Error with registration'
    }
  },
  SET_LOADING(state) {
    state.loading = true
  },
  STOP_LOADING(state) {
    state.loading = false
  }
}
