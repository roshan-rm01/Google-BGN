
const SERVER_ERRORS = [500, 502, 503, 504];

export default function ({ $axios, store, redirect}) {
  $axios.onError(error => {
    const { response } = error;
    switch (response.status) {
      case 500:
      case 502:
        store.dispatch('handleServerError');
        break;
    }
    return response
  })
}
