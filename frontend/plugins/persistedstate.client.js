import createPersistedState from 'vuex-persistedstate'

export default ({store}) => {
  createPersistedState({
    key: 'user_state',
    paths: ['user'],
  })(store)
}
