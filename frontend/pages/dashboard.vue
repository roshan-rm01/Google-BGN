<template>
  <div class="applicant">

    <v-row class="mb-40" no-gutters justify="center">
      <v-col cols="10" class="search" >
        <v-row no-gutters>
          <v-col cols="11">
            <v-row class="mt-4" justify="space-between">
              <app-text-field dense height="45" placeholder="Job title or position "></app-text-field>
              <app-text-field dense class="pl-4" placeholder="Location" rounded height="45"></app-text-field>
              <app-text-field dense class="pl-4" placeholder="Language" rounded height="45"></app-text-field>
            </v-row>
          </v-col>
          <v-col cols="1" class="mt-4 d-flex justify-end">
            <app-btn title="Search" color="secondary" height="64" width="80"
            >
              <v-icon>mdi-adjust</v-icon>
            </app-btn>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <v-row no-gutters justify="center">
      <h1 class="applicant__title">Jobs available for you</h1>
    </v-row>
    <v-row v-for="i in 5" :key="i" :class="{'mt-4' : i > 0 }" justify="center" no-gutters>
      <v-col cols="10" class="job" @click="$router.push('/job-details')">
        <div class="d-flex justify-space-between">
          <h2 class="job__title">Backend Developer</h2>
          <p class="job__description mt-2">24th July 2019</p>
        </div>
        <p class="job__description mt-4">
          Lorem ipsum dolor sit amet, consecrated adipisicing elit. Aspernatur assumenda ducimus eos facilis fugiat harum hic maiores maxime minima modi nam natus, nesciunt odio, odit officiis quidem sit temporibus velit.
        </p>
      </v-col>
    </v-row>
  </div>
</template>
<script>
import AppBtn from "@/components/Base/Forms/AppBtn";
import AppTextField from "~/components/Base/Forms/AppTextField";
export default {
  components: {
    // eslint-disable-next-line vue/no-unused-components
    AppBtn,
    AppTextField
  }
}
</script>
<style lang="scss" scoped>
.applicant {
  margin: 60px;
  background: #fff;
  border: 1px solid #F9FAFC;
  box-sizing: border-box;
  box-shadow: 0 4px 40px rgba(0, 0, 0, 0.05);
  border-radius: 40px;
  padding: 40px;
  @media screen and (max-width: 960px) {
    padding: 20px;
  }
  &__title {
    font-style: normal !important;
    font-weight: bold !important;
    font-size: 40px !important;
    line-height: 28px !important;
    letter-spacing: 0.35px !important;
    color: #000;
  }
}
.job {
  background: #fff;
  border: 1px solid #F9FAFC;
  box-sizing: border-box;
  border-radius: 14px;
  padding: 10px !important;
  cursor: pointer;
  box-shadow: 0 4px 40px rgba(0, 0, 0, 0.05);
  &__title {
    font-weight:  500;
  }
  &__description {
    font-size: 14px;
    padding: 0;
    margin: 0;
  }
}

.search {
  padding: 20px !important;
  box-sizing: border-box;
  border: 1px solid #F9FAFC;
  box-shadow: 0 4px 40px rgba(0, 0, 0, 0.05);
  border-radius: 8px;
}

.mb-40 {
  margin-bottom: 40px !important;
}
</style>
