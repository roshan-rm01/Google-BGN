import CookieService from '~/services/cookies';

export default {
  async authApplicant({ commit }, reqData) {
    commit('SET_LOADING');
    const res = await this.$axios.$post('/applicant/sign-in', reqData)
    commit('STOP_LOADING');
    if (!res.token) {
      commit('AUTH_ERROR');
      return false;
    }
    CookieService.setCookie(res.token);
    commit('AUTH_SUCCESS', 'Login successful');
    commit('SET_USER', { email: reqData.email, token: res.token, type: 'applicant'});
    return true;
  },

  async authEmployer({ commit }, reqData) {
      commit('SET_LOADING');
      const res = await this.$axios.$post('/org/sign-in', reqData);
      commit('STOP_LOADING');
      if (!res.token) {
        commit('AUTH_ERROR');
        return false;
      }
      commit('AUTH_SUCCESS', 'Login successful');
      commit('SET_USER', { email: reqData.email, token: res.token, type: 'employer'});
      return true;
  },

  async regApplicant({ commit }, reqData) {
    commit('SET_LOADING');
    const res = await this.$axios.$post('/applicant/sign-up', reqData);
    commit('STOP_LOADING');
    if (!res.token) {
      commit('REG_ERROR');
      return false;
    }
    commit('AUTH_SUCCESS', 'Registration successful');
    commit('SET_USER', { email: reqData.email, token: res.token, type: 'applicant'});
    return true;
  },

  async regEmployer({ commit }, reqData) {
    commit('SET_LOADING');
    const res = await this.$axios.$post('/org/sign-up', reqData);
    commit('STOP_LOADING');
    if (!res.token) {
      commit('REG_ERROR');
      return false;
    }
    commit('AUTH_SUCCESS', 'Registration successful');
    commit('SET_USER', { email: reqData.email, token: res.token, type: 'employer'});
    return true;
  },

  async fetchJobs({ commit }) {
    commit('SET_LOADING');
    const res = await this.$axios.$get('/job/all');
    commit('STOP_LOADING');
    if (!res) {
      commit('FETCH_ERROR', 'Error fetching jobs');
    } else {
      commit('SET_JOBS', res);
    }
  },

  async onboardEmployer({ dispatch, commit }, data) {
    commit('SET_LOADING');
    const res = await this.$axios.$post('/org/org-details', data);
    commit('STOP_LOADING');
    if (!res.token) {
      commit('SET_ERROR', 'An error occurred');
      return false;
    }
    await dispatch('fetchOrgDetails');
    return true;
  },

  async fetchOrgDetails({ commit }) {
    commit('SET_LOADING');
    const res = await this.$axios.$get('/details', data);
    commit('STOP_LOADING');
    if (!res) {
      commit('SET_ERROR', 'Error fetching details');
    } else {
      commit('SET_USER', { ...res, type: 'employer'});
    }
  },

  logOut({ commit }) {
    localStorage.clear();
    commit('SET_USER', null)
  },

  handleServerError({ commit }) {
    commit('SERVER_ERROR');
  },
}
