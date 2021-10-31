export default {
  async authApplicant({ commit }, reqData) {
    commit('SET_LOADING');
    // const res = await this.$axios.$post('/applicant/sign-in', reqData)
    // const { success, data } = this.parseResponse({ commit }, res);
    const { success, data } = { success: true, data: { email: 'a@b.com', token: 'jwwt', 'type': 'applicant' }}
    if (success) {
      commit('AUTH_SUCCESS', 'Login successful');
      commit('SET_USER', data);
    } else {
      commit('AUTH_ERROR');
    }
    commit('STOP_LOADING');
    return success;
  },

  async authEmployer({ commit }, reqData) {
    commit('SET_LOADING');
    // const res = await this.$axios.$post('/applicant/sign-in', reqData)
    // const { success, data } = this.parseResponse({ commit }, res);
    const { success, data } = { success: true, data: { email: 'a@b.com', token: 'jwwt', 'type': 'employer' }}
    if (success) {
      commit('AUTH_SUCCESS', 'Login successful');
      commit('SET_USER', data);
    } else {
      commit('AUTH_ERROR');
    }
    commit('STOP_LOADING');
    return success;
  },

  async regApplicant({ commit }, reqData) {
    commit('SET_LOADING');
    // const res = await this.$axios.$post('', reqData)
    // const { success, data } = this.parseResponse({ commit }, res);
    const { success, data } = { success: true, data: { email: 'a@b.com', token: 'jwwt', 'type': 'applicant' }}
    if (success) {
      commit('AUTH_SUCCESS', 'Registration successful');
      commit('SET_USER', data);
    } else {
      commit('REG_ERROR');
    }
    commit('STOP_LOADING');
    return success;
  },

  async regEmployer({ commit }, reqData) {
    commit('SET_LOADING');
    // const res = await this.$axios.$post('', reqData)
    // const { success, data } = this.parseResponse({ commit }, res);
    const { success, data } = { success: true, data: { email: 'a@c.com', token: 'jwwt', 'type': 'employer' }}
    if (success) {
      commit('AUTH_SUCCESS', 'Registration successful');
      commit('SET_USER', data);
    } else {
      commit('REG_ERROR');
    }
    commit('STOP_LOADING');
    return success;
  },

  parseResponse({ commit }, axiosResponse) {
    let response = { success: true }
    switch (axiosResponse.status){
      case 401:
      case 403:
        response = { success: false }
        break;
      case 500:
        commit('SERVER_ERROR');
        response = { success: false }
        break;
    }
    return { ...response, data: axiosResponse.data };
  }
}
