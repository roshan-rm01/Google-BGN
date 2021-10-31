<template>
  <app-modal :value="show" max-width="600" v-on="$listeners">
    <v-form ref="form" v-model="valid" autocomplete="off" class="sign_in mt-14">
      <p class="sign_in__title">
        New Posting
      </p>
      <app-text-field
        v-model="title"
        :rules="[v => !!v || 'Title is required']"
        type="text"
        placeholder="Job Title">
      </app-text-field>
      <app-text-field
        v-model="role"
        :rules="[v => !!v || 'Role is required']"
        type="text"
        placeholder="Role (e.g) Software Engineer">
      </app-text-field>
      <v-row>
        <v-col>
          <app-text-field
            v-model="experience"
            :rules="[v => !!v || 'Experience is required']"
            type="text"
            placeholder="Years of experience">
          </app-text-field>
        </v-col>
        <v-col>
          <app-text-field
            v-model="salary"
            :rules="[v => !!v || 'Salary is required', v => /^([1-9]\d*)$/.test(v) || 'Salary must be in number']"
            type="text"
            placeholder="Salary in USD">
          </app-text-field>
        </v-col>
      </v-row>
      <app-text-area
        v-model="description"
        :rules="[v => !!v || 'Description is required']"
        placeholder="Description of role">
      </app-text-area><br/><br/>
      <v-row justify="center">
        <app-btn
          type="button"
          color="secondary"
          height="51"
          width="278"
          :disabled="!valid || loading"
          :loading="loading"
          @click="postJob"
        >
          <p class="white--text">Submit</p>
        </app-btn>
      </v-row>
    </v-form>
  </app-modal>
</template>

<script>
import { mapState } from 'vuex';
import AppModal from '@/components/Base/Forms/AppModal'
import AppTextField from "~/components/Base/Forms/AppTextField";
import AppTextArea from '~/components/Base/Forms/AppTextArea';
import AppBtn from "~/components/Base/Forms/AppBtn";
import AppSelect from '~/components/Base/Forms/AppSelect';
export default {
  components: {
    AppBtn,
    AppTextField,
    AppTextArea,
    AppModal,
    AppSelect
  },
  props: {
    show: {
      type: Boolean,
      default: false,
    },
  },
  data: () => ({
    valid: false,
    title: '',
    role: '',
    description: '',
    experience: '',
    salary: null,
  }),
  computed: {
    ...mapState(['loading'])
  },
  methods: {
    async postJob() {
      if (this.$refs.form.validate()) {
        const data = {}
        const postSuccess = await this.$store.dispatch('postJob', data);
        if (postSuccess) {
          this.$emit('close');
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.sign_in  {
  padding: 40px;
  &__title {
    font-weight: 500;
    font-size: 20px;
    line-height: 28px;
    letter-spacing: 0.35px;
    color: #000;
    margin-bottom: 10px;
  }
}
p {
  margin: 0;
  padding: 0;
}
</style>
