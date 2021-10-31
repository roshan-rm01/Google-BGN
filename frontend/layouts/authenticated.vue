<template>
  <v-app>
    <v-main dark>
      <navbar/>
      <nuxt />
      <snackbar />
    </v-main>
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar.vue'
import Snackbar from '@/components/Snackbar.vue'
export default {
  components: {
    Navbar,
    Snackbar
  },
  created() {
    const user = this.$store.getters.getUser;
    if (!user) {
      this.$router.push('/');
    }
  }
}
</script>
