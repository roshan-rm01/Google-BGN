<template>
  <app-modal :value="show" max-width="600" v-on="$listeners">
    <v-form autocomplete="off" class="sign_in mt-14">
      <p class="sign_in__title">
        Enter Your Details
      </p>
      <app-text-field type="email" placeholder="Email"></app-text-field>
      <app-text-field type="password" placeholder="Password"></app-text-field>
      <v-row justify="center">
        <app-btn type="submit" color="secondary" height="51" width="278"> <p class="white--text">Login</p> </app-btn>
      </v-row>
    </v-form>
  </app-modal>
</template>

<script>
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
