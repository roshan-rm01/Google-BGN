<template>
  <v-snackbar
    class="snack"
    :timeout="2000"
    :value="getAlert"
    :color="getAlertType"
    absolute
    right
    top
  >
    {{ getAlertMessage }}
  </v-snackbar>
</template>
<script>
import {mapGetters} from "vuex";

export default {
  data() {
    return {

    }
  },
  computed: {
    ...mapGetters([
      'getAlert'
    ]),
    getAlertMessage() {
      if (this.$store.getters.getAlert) {
        const {message} = this.$store.getters.getAlert;
        return message;
      }
      return '';
    },
    getAlertType() {
      if (this.$store.getters.getAlert) {
        const {success} = this.$store.getters.getAlert;
        return success ? 'green' : 'red';
      }
      return '';
    }
  }
}
</script>
<style>
  .snack {
    z-index: 999 !important;
  }
</style>
