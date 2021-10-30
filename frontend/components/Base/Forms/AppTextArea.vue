<template>
  <v-textarea
    outlined
    v-bind="{ ...$props, ...$attrs }"
    hide-details="auto"
    :ripple="false"
    dense
    v-on="$listeners"
  >
    <template v-for="(index, name) in $slots" #[name]>
      <slot :name="name" />
    </template>
    <template v-for="(index, name) in $scopedSlots" #[name]="data">
      <slot :name="name" v-bind="data"></slot>
    </template>
  </v-textarea>
</template>
<style lang="scss" scoped>
@import 'text_field.scss';
::v-deep {
  &.v-input--selection-controls {
    margin-top: 0 !important;
    padding-top: 0 !important;
  }
}
</style>
