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
  SERVER_ERROR(state) {
    state.alert = {
      success: false,
      message: 'A server error occurred'
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
  },
  FETCH_ERROR(state) {
    state.alert = {
      success: false,
      message: 'Error fetching jobs'
    }
  },
  SET_JOBS(state, jobs) {
    state.jobs = jobs
  }
}
