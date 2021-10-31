<template>
  <v-row justify="end">
    <v-col cols="4" md="6">
      <nuxt-link to="/">
        <div class="logo-container">
          <img src="~/assets/images/logo.jpeg" alt="logo" class="logo"/>
        </div>
      </nuxt-link>
    </v-col>
    <v-col cols="8" md="6">
      <ul v-if="!getUser">
        <li><nuxt-link href="#" to="">Find Jobs</nuxt-link></li>
        <li><a href="#" @click.prevent="showTalentSignIn = true"> Talent Sign In  </a></li>
        <li><a href="#" @click.prevent="showEmployerSignIn = true"> Employer Sign In  </a></li>
      </ul>
      <ul v-else>
        <li><a href="#" @click.prevent="logOut"> Logout</a></li>
      </ul>
    </v-col>
    <sign-in-modal :show="showTalentSignIn" @close="showTalentSignIn = false"></sign-in-modal>
    <employer-sign-in-modal :show="showEmployerSignIn" @close="showEmployerSignIn = false"></employer-sign-in-modal>
  </v-row>
</template>
<script>
import { mapGetters } from 'vuex';
import EmployerSignInModal from '~/components/EmployerSignInModal';
import SignInModal from '~/components/SignInModal';
export default {
  components: {
    EmployerSignInModal,
    SignInModal,
  },
  data() {
    return {
      showTalentSignIn: false,
      showEmployerSignIn: false,
    }
  },
  computed: {
    ...mapGetters(['getUser'])
  },
  methods: {
    logOut() {
      const isLoggedOut = this.$store.dispatch('logOut');
      if (isLoggedOut) {
        this.$router.push('/');
      }
    }
  }
}
</script>

<style lang="scss" scoped>
ul {
  display: table;
  margin: 10px auto;
  padding: 10px 20px;
}
ul li {
  list-style: none;
  display: inline-block;
  margin-left: 20px;
}
ul li a {
  text-decoration: none;
  position: relative;
  padding: 15px 10px;
  font-size: 18px;
  display: block;
}
ul li a + a {
  margin-left: 16px;
}
ul li a::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 4px;
  background-color: var(--v-primary-base);
  transform-origin: bottom right;
  transition: transform 0.5s ease;
  transform: scaleX(0);
}
ul a:hover::after {
  transform-origin: bottom left;
  transform: scaleX(1);
}
.logo-container {
  padding: 15px;
}

.logo-container > img {
  height: 45px;
  width: 45px;
}
</style>
