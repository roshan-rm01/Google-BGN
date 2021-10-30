<template>
  <v-row justify="end">
    <v-col cols="12" md="6">
      <ul>
        <li><nuxt-link href="#" to="">Find Jobs</nuxt-link></li>
        <li><nuxt-link href="#" to="">Post Jobs</nuxt-link></li>
        <li><a href="#" @click.prevent="showSignIn = true"> Sign In  </a></li>
      </ul>
    </v-col>
    <sign-in-modal :show="showSignIn" @close="showSignIn = false"></sign-in-modal>
  </v-row>
</template>
<script>
import SignInModal from "~/components/SignInModal";
export default {
  components: {
    SignInModal,
  },
  data() {
    return {
      showSignIn: false
    }
  },
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
</style>
