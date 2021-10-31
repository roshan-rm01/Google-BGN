<template>
  <app-modal :value="show" max-width="600" v-on="$listeners">
    <v-form ref="form" v-model="valid" autocomplete="off" class="sign_in mt-14">
      <p class="sign_in__title">
        Employer Sign In
      </p>
      <app-text-field
        v-model="email"
        :rules="emailRules"
        type="email"
        placeholder="Email">
      </app-text-field>
      <app-text-field
        v-model="password"
        :rules="passwordRules"
        type="password"
        placeholder="Password">
      </app-text-field>
      <v-row justify="center">
        <app-btn
          type="button"
          color="secondary"
          height="51"
          width="278"
          :disabled="!valid || loading"
          :loading="loading"
          @click="authEmployer"
        >
          <p class="white--text">Login</p>
        </app-btn>
      </v-row>
    </v-form>
  </app-modal>
</template>

<script>
import {mapState} from "vuex";
import AppModal from '@/components/Base/Forms/AppModal'
import AppTextField from "~/components/Base/Forms/AppTextField";
import AppBtn from "~/components/Base/Forms/AppBtn";
export default {
  components: {
    AppBtn,
    AppTextField,
    AppModal
  },
  props: {
    show: {
      type: Boolean,
      default: false,
    },
  },
  data: () => ({
    valid: false,
    email: '',
    password: '',
    emailRules: [
      v => !!v || 'E-mail is required',
      v => /.+@.+\..+/.test(v) || 'Invalid email address',
    ],
    passwordRules: [
      v => !!v || 'Password is required',
    ],
  }),
  computed: {
    ...mapState(['loading'])
  },
  methods: {
    async authEmployer() {
      if (this.$refs.form.validate()) {
        const authSuccess = await this.$store.dispatch('authEmployer', {email: this.email, password: this.password});
        if (authSuccess) {
          this.$emit('close');
          this.$router.push('employer-dashboard');
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.sign_in  {
  padding: 40px;
  &__title {
    font-weight: 500;
    font-size: 20px;
    line-height: 28px;
    letter-spacing: 0.35px;
    color: #000;
    margin-bottom: 10px;
  }
}
p {
  margin: 0;
  padding: 0;
}
</style>
