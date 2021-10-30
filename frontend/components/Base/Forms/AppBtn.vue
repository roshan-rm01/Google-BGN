<template>
  <v-btn
    rounded
    v-bind="{ ...$props, ...$attrs }"
    depressed
    v-on="$listeners"
  >
    <template v-for="(index, name) in $slots" #[name]>
      <slot :name="name" />
    </template>
  </v-btn>
</template>

<script>
export default {
  name: 'AppBtn',
  props: {
  hasShadow: {
    default: false,
    type: Boolean,
  }
  }
}
</script>

<style lang="scss" scoped>
::v-deep.v-btn {
  &.v-btn--rounded {
    border-radius: 40px !important;
  }
  .v-btn__content {
    font-style: normal;
    font-weight: 600;
    font-size: 16px;
    line-height: 28px;
    display: flex;
    align-items: center;
    text-align: center;
    letter-spacing: 0.75px;
  }
}
</style>
