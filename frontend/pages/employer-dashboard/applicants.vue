<template>
  <div class="job-applicants">
    <div class="pb-14 mt-14">
      <v-row no-gutters justify="center" >
        <v-col cols="12" md="6">
          <v-row no-gutters justify="space-between">
            <div class="job-applicants__title">
              <h2 style="font-weight: 400">Software Engineer</h2>
              <p>LONDON, UNITED KINGDOM /DEV /FULL-TIME</p>
            </div>
            <span> <h1>78</h1> <p>applicants</p></span>
          </v-row>
        </v-col>
      </v-row>
    </div>
    <div class="job-applicants__description">
      <v-row no-gutters justify="center" >
        <v-col cols="12" md="6">
          <v-row no-gutters>
              <v-col v-for="i in 6"  :key="i" cols="12" md="6" class="job-applicants__card">
              </v-col>
          </v-row>
        </v-col>
      </v-row>
    </div>
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
.job-applicants {
  &__description {
    background: #f9f9f9;
    padding: 20px 0;
  }
  &__card {
    background: #fff;
    border: 1px solid #F9FAFC;
    box-sizing: border-box;
    box-shadow: 0 4px 40px rgba(0, 0, 0, 0.05);
    border-radius: 20px;
    padding: 100px !important;
  }
}

.description__heading {
  font-size: 18px;
  font-weight: 600;
  -webkit-font-smoothing: antialiased;
}
.description__subtext {
  font-size: 16px;
}
p{
  margin: 0;
  padding: 0;
}
h2, p {
  color: #515357;
}
</style>

