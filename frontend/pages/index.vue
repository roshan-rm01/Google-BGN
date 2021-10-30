<template>
    <v-row class="px-14">
      <v-col cols="12" md="6">
       <v-row justify="center">
         <img class="image" src="@/assets/images/lady.png" alt="African Lady"/>
       </v-row>
      </v-col>
      <v-col col="12" md="6">
        <h1 class="mt-10 mt-md-14 title">Talent Africa</h1>
        <p>Connecting African youths to jobs all over the world.</p>
        <div class="mt-10 mt-md-14 d-md-flex">
            <app-btn color="primary" height="64" width="261" @click="visitUrl('applicants')">Job Seekers</app-btn>
            <app-btn class="mt-4 mt-sm-0 ml-md-4"  color="secondary" height="64" width="261" @click="visitUrl('employers')">Employers</app-btn>
        </div>
      </v-col>
    </v-row>
</template>
<script>
import AppBtn from "~/components/Base/Forms/AppBtn";
  export default {
    components: {
      AppBtn,
    },
    methods: {
      visitUrl(path) {
        this.$router.push(path)
      }
    }
  }
</script>
<style scoped lang="scss">
.image {
  max-width: 557px;
  @media (max-width: 480px) {
    width: 50%;
  }
}

.title{
  font-weight: 900;
  font-size: 68px !important;
  line-height: 78px !important;
  @media (min-width: 1024px) {
  margin-top: 200px !important;
}
}
</style>
