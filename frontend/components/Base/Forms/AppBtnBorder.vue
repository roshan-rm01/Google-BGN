<template>
  <div class='button__border' :style="{backgroundColor: background}">
    <v-row justify='center'>
      <app-btn v-bind="{ ...$props, ...$attrs }" height="64" width="261">
        <template v-for="(index, name) in $slots" #[name]>
          <slot :name="name" />
        </template>
      </app-btn>
    </v-row>
  </div>
</template>
<script>
import AppBtn from './AppBtn'
export default {
  components: {
    AppBtn,
  },
  props: {
    background: {
      type: String,
      required: true
    },
  },
}
</script>
<style>
.button__border {
  padding: 20px;
  border-radius: 40px;
}
</style>
