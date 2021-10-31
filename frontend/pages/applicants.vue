<template>
  <div class="applicants">
    <v-row>
      <v-col cols="12" md="6">
        <v-row justify="start">
          <div class="px-2 px-md-10">
            <h1 class="text__heading white--text">Land your dream job...</h1>
            <p class="text__Label mt-2  white--text">Join over 2000 african youths in getting life changing <br> opportunities</p>
          </div>
        </v-row>
      </v-col>
      <v-col cols="12" md="6" >
        <v-form ref="form" v-model="valid" autocomplete="off" class="sign_in mt-14">
          <div class="applicants__form">
          <h1 class="applicants__form__title">Personal info</h1>
          <v-row class="mt-8" no-gutters>
            <v-col cols="12" md="6">
              <div>
                <p class="text__label">Firstname</p>
                <app-text-field v-model="firstName" :rules="[v => !!v || 'First name is required']"></app-text-field>
              </div>
            </v-col>
            <v-col cols="12" md="6" class-="ml-5">
              <div class="pl-md-5">
                <p class="text__label">Lastname</p>
                <app-text-field v-model="lastName" :rules="[v => !!v || 'Last name is required']"></app-text-field>
              </div>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col cols="12" md="6">
              <div>
                <p class="text__label">Email</p>
                <app-text-field v-model="email" type="email" :rules="[v => !!v || 'Email is required']"></app-text-field>
              </div>
            </v-col>
            <v-col cols="12" md="6">
              <div class="pl-md-5">
                <p class="text__label">Password</p>
                <app-text-field v-model="password" type="password" :rules="[v => !!v || 'Password is required']"></app-text-field>
              </div>
            </v-col>
          </v-row>
          <v-row no-gutters>
            <v-col cols="12" md="6" class-="ml-5">
              <div class="pl-md-5">
                <p class="text__label">Country</p>
                <app-select v-model="country" :items="countries"></app-select>
              </div>
            </v-col>
          </v-row>
          <v-row justify="center">
            <app-btn type="button" color="secondary" height="51" width="278" :disabled="!valid" @click="regApplicant">
              <p class="white--text">Submit</p>
            </app-btn>
          </v-row>
        </div>
        </v-form>
      </v-col>
    </v-row>
  </div>
</template>
<script>
import AppTextField from "@/components/Base/Forms/AppTextField";
import AppSelect from '@/components/Base/Forms/AppSelect'
import AppBtn from '@/components/Base/Forms/AppBtn';
export default {
  components: {
    AppTextField,
    AppSelect,
    AppBtn
  },
  data() {
    return {
      countries: ['Nigeria', 'Ghana', 'Senegal'],
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      country: null,
      valid: false,
    }
  },
  methods: {
    async regApplicant() {
      if (this.$refs.form.validate()) {
        const userData = {
          email: this.email,
          password: this.password,
          firstName: this.firstName,
          lastName: this.lastName,
          country: this.country
        }
        const regSuccess = await this.$store.dispatch('regApplicant', userData);
        if (regSuccess) {
            this.$router.push('dashboard');
        }
      }
    }
  }
}
</script>
<style lang="scss" scoped>
.applicants {
  background: linear-gradient(0deg, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('../assets/images/applicant.png');
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  padding: 60px;
  @media screen and (max-width: 960px) {
    padding: 30px;
  }
  &__form {
    background: #fff;
    border: 1px solid #F9FAFC;
    box-sizing: border-box;
    box-shadow: 0 4px 40px rgba(0, 0, 0, 0.05);
    border-radius: 30px;
    padding: 45px;
    @media screen and (max-width: 960px) {
      padding: 20px;
    }
    &__title {
      font-style: normal;
      font-weight: bold;
      font-size: 20px;
      line-height: 28px;
      letter-spacing: 0.35px;
      color: #000;
    }
   }
}

.text__label {
  font-size: 14px;
  line-height: 24px;
  color: #575A65;
  margin-bottom: 4px !important;
}
p {
  margin: 0;
  padding: 0;
}
.text__heading {
  font-weight: 700;
  font-size: 48px !important;
  line-height: 58px !important;
  @media (min-width: 1024px) {
    margin-top: 200px !important;
  }
}
</style>
