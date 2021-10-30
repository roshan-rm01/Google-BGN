<template>
  <v-container fluid fill-height class="main">
    <v-row class="content">
      <v-col cols="5" class="content__image">
      </v-col>
      <v-col col="12" class="content__text">
        <h1>Talent Africa</h1>
        <p>Connecting African youths to jobs all over the world.</p>
        <div class="reg-container">
          <NuxtLink to="/register">
            <span class="reg-link">
              Job Seekers Sign Up
            </span>
          </NuxtLink>
          <NuxtLink to="/employer/register">
            <span class="reg-link">
              Employer Sign Up
            </span>
          </NuxtLink>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
  export default {
    layout: 'home'
  }
</script>
<style scoped lang="scss">
h1 {
  font-weight: 500;
  font-size: 3rem;
}
.content__text > p {
  font-size: 2rem;
}
.content__image {
  background-image: url('../assets/images/lady.jpeg');
}
.main {
  align-items: start;
  padding: 5rem 3rem;
  background: var(--bg-color);
}
.content {
  height: 100%;
  color: #FFF;
}
.reg-container {
  margin-top: 3rem;
}
.reg-container > a {
  text-decoration: none;
}
.reg-link {
  display: flex;
  height: 50px;
  margin: 20px 0;
  background: #1762A7;
  color: #FFF;
  max-width: 30%;
  justify-content: center;
  align-items: center;
}

</style>
