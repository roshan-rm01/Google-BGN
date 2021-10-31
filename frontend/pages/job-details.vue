<template>
  <div class="job-details">
    <div class="pb-14 mt-14">
      <v-row no-gutters justify="center" >
        <v-col cols="12" md="6">
          <v-row no-gutters justify="space-between">
            <div class="job-details__title">
              <h2 style="font-weight: 400">Software Engineer</h2>
              <p>LONDON, UNITED KINGDOM /DEV /FULL-TIME</p>
            </div>
            <app-btn color="black" height="50" width="261" class="mt-4" @click="visitUrl('applicants')"> <p class="white--text">Apply</p> </app-btn>
            <app-btn color="black" height="50" width="261" class="mt-4" @click="$router.push('/employer-dashboard/applicants')"> <p class="white--text">View Applicants</p> </app-btn>
          </v-row>
        </v-col>
      </v-row>
    </div>
    <div class="job-details__description">
      <v-row no-gutters justify="center" >
        <v-col cols="12" md="6">
          <p class="description__heading">A World-Changing Company</p>
          <p class="description__subtext mt-2">
            At Palantir, we’re passionate about building software that solves problems. We partner with the most important institutions in the world to transform how they use data and technology. Our software has been used to stop terrorist attacks, discover new medicines, gain an edge in global financial markets, and more. If these types of projects excite you, we'd love for you to join us.
          </p>
          <div class="mt-4">
            <p class="description__heading">A World-Changing Company</p>
            <p class="description__subtext mt-2">
              At Palantir, we’re passionate about building software that solves problems. We partner with the most important institutions in the world to transform how they use data and technology. Our software has been used to stop terrorist attacks, discover new medicines, gain an edge in global financial markets, and more. If these types of projects excite you, we'd love for you to join us.
            </p>
          </div>

          <div class="mt-4">
            <p class="description__heading">A World-Changing Company</p>
            <p class="description__subtext mt-2">
              At Palantir, we’re passionate about building software that solves problems. We partner with the most important institutions in the world to transform how they use data and technology. Our software has been used to stop terrorist attacks, discover new medicines, gain an edge in global financial markets, and more. If these types of projects excite you, we'd love for you to join us.
            </p>
          </div>

          <div class="mt-4">
            <p class="description__heading">A World-Changing Company</p>
            <p class="description__subtext mt-2">
              At Palantir, we’re passionate about building software that solves problems. We partner with the most important institutions in the world to transform how they use data and technology. Our software has been used to stop terrorist attacks, discover new medicines, gain an edge in global financial markets, and more. If these types of projects excite you, we'd love for you to join us.
            </p>
          </div>
          <div class="mt-4">
            <p class="description__heading">A World-Changing Company</p>
            <p class="description__subtext mt-2">
              At Palantir, we’re passionate about building software that solves problems. We partner with the most important institutions in the world to transform how they use data and technology. Our software has been used to stop terrorist attacks, discover new medicines, gain an edge in global financial markets, and more. If these types of projects excite you, we'd love for you to join us.
            </p>
          </div>

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
.job-details {
  &__description {
    background: #f9f9f9;
    padding: 20px 0;
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

