<template>
  <div class="applicants">
    <v-row>
      <v-col cols="12" md="6">
        <v-row justify="start">
          <div class="px-2 px-md-10">
            <h1 class="text__heading white--text">Access to Talents...</h1>
            <p class="text__Label mt-2  white--text">Get unlimited access to over thousands of talented Africans </p>
          </div>
        </v-row>
      </v-col>
      <v-col cols="12" md="6" >
        <v-form ref="form" v-model="valid" autocomplete="off" class="sign_in mt-14">
          <div class="applicants__form">
            <h1 class="applicants__form__title">Company Details</h1>
            <v-row class="mt-8" no-gutters>
              <v-col cols="12" md="6">
                <div>
                  <p class="text__label">Industry</p>
                  <app-select v-model="industry" :items="industries" :rules="[v => !!v || 'Please select one']"></app-select>
                </div>
              </v-col>
              <v-col cols="12" md="6" class-="ml-5">
                <div class="pl-md-5">
                  <p class="text__label">Country</p>
                  <app-select v-model="country" :items="countries" :rules="[v => !!v || 'Please select one']"></app-select>
                </div>
              </v-col>
            </v-row><br/>
            <v-row no-gutters>
              <v-col cols="12" md="6">
                <div>
                  <p class="text__label">Telephone</p>
                  <app-text-field v-model="telephone" :rules="[v => !!v || 'Telephone is required']"></app-text-field>
                </div>
              </v-col>
              <v-col cols="12" md="6">
                <div class="pl-md-5">
                  <p class="text__label">Company Size</p>
                  <app-select v-model="companySize" :items="companySizes" :rules="[v => !!v || 'Please select one']"></app-select>
                </div>
              </v-col>
            </v-row>
            <v-row no-gutters>
              <v-col cols="12" md="12">
                <div>
                  <p class="text__label">Company Bio</p>
                  <app-text-area v-model="companyBio" :rules="[v => !!v || 'Company bio is required']"></app-text-area>
                </div>
              </v-col>
            </v-row>
            <v-row justify="center">
              <app-btn
                type="button"
                color="secondary"
                height="51"
                width="278"
                :disabled="!valid || loading"
                :loading="loading"
                @click="onboardEmployer"
              >
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
import {mapState} from "vuex";
import AppTextField from '~/components/Base/Forms/AppTextField';
import AppSelect from '~/components/Base/Forms/AppSelect'
import AppBtn from '~/components/Base/Forms/AppBtn';
import AppTextArea from '~/components/Base/Forms/AppTextArea';
export default {
  components: {
    AppTextField,
    AppSelect,
    AppBtn,
    AppTextArea,
  },
  layout: 'authenticated',
  data() {
    return {
      countries: ['United States', 'United Kingdom', 'Switzerland', 'Germany', 'Other'],
      industries: ['Aviation', 'Telecommunication', 'Oil and Gas', 'Information Technology', 'Other'],
      companySizes: ['1-50 employees', '50-500 employees', '500 - 1000 employees', '>1000 employees'],
      companyBio: '',
      telephone: '',
      country: null,
      companySize: null,
      industry: null,
      valid: false,
    }
  },
  computed: {
    ...mapState(['loading'])
  },
  methods: {
    async onboardEmployer() {
      if (this.$refs.form.validate()) {
        const userData = {
          location: this.country,
          companySize: this.companySize,
          industry: this.industry,
          companyBio: this.companyBio,
          telephone: this.telephone
        }
        const onboardSuccess = await this.$store.dispatch('onboardEmployer', userData);
        if (onboardSuccess) {
          await this.$router.push('employer-dashboard');
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
