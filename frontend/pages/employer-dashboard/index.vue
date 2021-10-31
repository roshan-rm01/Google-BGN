<template>
  <div class="employer">
    <v-row class="mb-40" no-gutters>
        <v-col cols="12" md="8">
          <h1>Job Listings</h1>
          <p>Your previously added jobs</p>
        </v-col>
      <v-col cols="12" md="4">
        <v-row justify="end">
          <app-btn class='ml-2' title="Add Job" color="secondary" height="64" width="120"
          >
            <v-icon>mdi-plus</v-icon>
          </app-btn>
        </v-row>
      </v-col>
    </v-row>
    <v-row v-for="i in 5" :key="i" :class="{'mt-4' : i > 0 }" no-gutters>
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
export default {
  components: {
    AppBtn
  }
}
</script>
<style lang="scss" scoped>
.employer {
  margin: 60px;
  background: #fff;
  border: 1px solid #F9FAFC;
  box-sizing: border-box;
  box-shadow: 0 4px 40px rgba(0, 0, 0, 0.05);
  border-radius: 40px;
  padding: 40px;
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

.mb-40 {
  margin-bottom: 40px !important;
}
</style>
