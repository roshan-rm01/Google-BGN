<template>
  <v-snackbar
    v-model="getAlert"
    :timeout="2000"
    :value="true"
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
