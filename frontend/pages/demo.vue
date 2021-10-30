<template>
  <div class="demo-page pa-10 mb-15">
    <h1>Demo</h1>
    <div class="mt-10">
      <h2 class="heading-2 mb-2">Forms</h2>
      <p class="body mt-8 mb-4">Buttons</p>
      <v-row>
        <app-btn color="primary" height="64" width="261"> Login </app-btn>
        <app-btn color="secondary" class='ml-2' height="64" width="261"> Secondary </app-btn>
        <app-btn class='ml-2' color="secondary" height="64" width="120"
        >
          <v-icon>mdi-television</v-icon>
        </app-btn>
          <app-btn-border color="secondary" background="rgba(255, 194, 0, 0.18)" class='ml-2' height="64" width="261"> Lets go </app-btn-border>
      </v-row>

      <hr class='my-10'>
      <p class="body mt-8 mb-4">Text and select field</p>
      <v-row>
        <v-col cols='6'>
          <app-text-field></app-text-field>
        </v-col>
        <v-col cols='6'>
          <app-select :items='items'></app-select>
        </v-col>
      </v-row>

      <p class="body mt-8 mb-4">Textarea </p>
      <v-row>
        <v-col cols='6'>
          <app-text-area></app-text-area>
        </v-col>
        <v-col cols='6'>
          <p class="body mt-8 mb-4"> Code  Input </p>
          <app-code-input></app-code-input>
        </v-col>
      </v-row>

      <div class="mt-10">
        <h2 class="heading-2 mb-2">Modals</h2>
        <div class="modals d-flex">
          <div>
            <app-btn
              color="primary"
              height="60"
              width="190"
              @click.stop="modalOne = true"
            >
              Modal 1
            </app-btn>
            <app-modal v-model="modalOne" width="43%">
              <div class="mt-10 mb-13 pa-5">
                <h1 class="heading-1 mb-2">App Colors</h1>
                <div class="d-flex">
                  <div class="color-test primary"></div>
                  <div class="color-test secondary"></div>
                  <div class="color-test secondary lighten-2"></div>
                  <div class="color-test grey"></div>
                  <div class="color-test yellow"></div>
                  <div class="color-test success"></div>
                  <div class="color-test purple lighten-1"></div>
                </div>
                <h3 class="body mt-8 mb-2">Using CSS Variables</h3>
                <div class="d-flex">
                  <div class="color-test one"></div>
                  <div class="color-test two"></div>
                  <div class="color-test three"></div>
                  <div class="color-test four"></div>
                  <div class="color-test five"></div>
                  <div class="color-test six"></div>
                  <div class="color-test seven"></div>
                </div>
              </div>
            </app-modal>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AppBtn from '../components/Base/Forms/AppBtn'
import AppBtnBorder from '../components/Base/Forms/AppBtnBorder'
import AppTextField from '../components/Base/Forms/AppTextField'
import AppSelect from '../components/Base/Forms/AppSelect'
import AppTextArea from '../components/Base/Forms/AppTextArea'
import AppCodeInput from '../components/Base/Forms/AppCodeInput'
import AppModal from '../components/Base/Forms/AppModal'
export default {
  components: {
    AppCodeInput,
    AppSelect,
    AppBtn,
    AppBtnBorder,
    AppTextField,
    AppTextArea,
    AppModal,
  },
  data() {
    return {
      modalOne: false,
      modalTwo: false,
      items: [
        'Mini',
        'Mani',
        'Modupe',
      ]
    }
  }
}
</script>
<style lang='scss' scoped>
.color-test {
  width: 37px;
  height: 37px;
  border-radius: 50%;
  margin-right: 2px;
&.one {
   background-color: var(--v-primary-base);
 }
&.two {
   background-color: var(--v-secondary-base);
 }
&.three {
   background-color: var(--v-secondary-lighten2);
 }
&.four {
   background-color: var(--v-grey-base);
 }
&.five {
   background-color: var(--v-yellow-base);
 }
&.six {
   background-color: var(--v-success-base);
 }
&.seven {
   background-color: var(--v-purple-lighten1);
 }
}
</style>
