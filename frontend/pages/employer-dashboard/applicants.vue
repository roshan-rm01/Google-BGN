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
            <div class="d-flex">
              <span> <h1>78</h1> <p>applicants</p></span>
              <app-btn class='ml-2' title="Download" color="secondary" height="64" width="80"
              >
                <v-icon>mdi-download</v-icon>
              </app-btn>
            </div>
          </v-row>
        </v-col>
      </v-row>
    </div>
    <div class="job-applicants__description">
      <v-row no-gutters justify="center" >
        <v-col cols="12" md="6">
          <v-row no-gutters>
              <v-col v-for="i in 6" :key="i"  cols="12" md="6" :class="{'mt-10': i > 2}">
                <div class="job-applicants__card">
                    <v-row no-gutters justify="space-between">
                        <v-col cols="9">
                          <h1 class="job-applicants__card__name">Sandra Ali</h1>
                          <p class="job-applicants__card__des"> Product Manager at Wazobia FM </p>
                          <div class="mt-8">
                            <p>Specifications</p>
                            <ul>
                              <li>Experience with placeholder  </li>
                              <li>Previous experience as placeholder</li>
                              <li>Demonstrable knowledge of XYZ</li>
                            </ul>
                          </div>
                        </v-col>
                        <v-col cols="3">
                          <v-img  :src="require('assets/images/applicant-avatar.png')" alt=""/>
                        </v-col>
                    </v-row>
                    <v-row no-gutters justify="end">
                      <app-btn color="secondary" class="mt-4" height="30" width="120">
                        <p class="white--text button_view">View More</p>
                      </app-btn>
                    </v-row>
                </div>
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
    // eslint-disable-next-line vue/no-unused-components
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
    border-radius: 26px;
    padding: 20px !important;
    width: 95% !important;
    &__name {
      font-weight: 400 !important;
      font-size: 24px !important;
      line-height: 30px !important;
      color: #000;
    }
    &__des {
      font-weight: normal;
      font-size: 12px;
      line-height: 18px;
      color: #000;
    }
    &__avatar {
      width: 153px;
      height: 157px;
    }
  }
}
.description__subtext {
  font-size: 16px;
}

.button_view {
  font-size: 10px;
  text-decoration: none;
}
p{
  margin: 0;
  padding: 0;
}
h2, p, li {
  color: #515357;
  margin: 0;
  padding: 0;
}


li {
  font-size: 12px;
}


</style>

