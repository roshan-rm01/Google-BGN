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
            <div class="applicants__form">
              <h1 class="applicants__form__title">Personal info</h1>
              <v-row class="mt-8" no-gutters>
                <v-col cols="12" md="6">
                  <div>
                    <p class="text__label">Firstname</p>
                    <app-text-field></app-text-field>
                  </div>
                </v-col>
                <v-col cols="12" md="6" class-="ml-5">
                  <div class="pl-md-5">
                    <p class="text__label">Lastname</p>
                    <app-text-field></app-text-field>
                  </div>
                </v-col>
              </v-row>
              <v-row no-gutters>
                <v-col cols="12" md="6">
                  <div>
                    <p class="text__label">Email</p>
                    <app-text-field></app-text-field>
                  </div>
                </v-col>
                <v-col cols="12" md="6" class-="ml-5">
                  <div class="pl-md-5">
                    <p class="text__label">Country</p>
                    <app-select :items="countries"></app-select>
                  </div>
                </v-col>
              </v-row>
              <v-row class="mt-4" no-gutters>
                <v-col cols="12" md="6">
                  <div>
                    <p class="text__label">CV Upload</p>
                    <app-text-field type="file"></app-text-field>
                  </div>
                </v-col>
                <v-col cols="12" md="6">
                  <div class="pl-md-5">
                    <p class="text__label">Password</p>
                    <app-text-field type="password"></app-text-field>
                  </div>
                </v-col>
              </v-row>
              <v-row justify="center">
                <app-btn-border background="rgba(255, 194, 0, 0.18)" color="secondary" height="51" width="278"> <p class="primary--text">Submit</p> </app-btn-border>
              </v-row>
            </div>
        </v-col>
    </v-row>
  </div>
</template>
<script>
import AppTextField from "~/components/Base/Forms/AppTextField";
import AppSelect from '~/components/Base/Forms/AppSelect'
import AppBtnBorder from "~/components/Base/Forms/AppBtnBorder";
export default {
  components: {
    AppTextField,
    AppSelect,
    AppBtnBorder
  },
  data() {
    return {
      countries: ['Nigeria', 'Ghana', 'Senegal']
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
