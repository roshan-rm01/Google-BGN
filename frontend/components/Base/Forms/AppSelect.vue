<template>
  <v-select
    outlined
    v-bind="{ ...$props, ...$attrs }"
    hide-details="auto"
    v-on="$listeners"
    height='65'
  >
    <template v-for="(index, name) in $slots" #[name]>
      <slot :name="name" />
    </template>
    <template v-for="(index, name) in $scopedSlots" #[name]="data">
      <slot :name="name" v-bind="data"></slot>
    </template>
    <template #append>
      <template
        v-if="
          $attrs.error ||
          ($attrs['error-messages'] && $attrs['error-messages'].length)
        "
      >
        <v-icon small color="error">fa-info-circle</v-icon>
      </template>
      <template v-else>
        <svg width="16" height="13" viewBox="0 0 16 13" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M7.99996 13C7.32546 13 6.68029 12.6634 6.23241 12.0727L0.6165 4.70889C-0.0553295 3.82633 -0.189962 2.574 0.271254 1.51522C0.677818 0.580667 1.48695 0 2.38405 0H13.6159C14.513 0 15.3221 0.580667 15.7287 1.51522C16.1899 2.574 16.0552 3.82633 15.3848 4.70744L9.76751 12.0727C9.31962 12.6634 8.67445 13 7.99996 13Z" fill="#231F20"/>
        </svg>
      </template>
    </template>
  </v-select>
</template>
<style lang="scss" scoped>
@import 'text_field.scss';
::v-deep {
  &.v-list {
    padding: 0 0 !important;
  }
  svg {
    margin: 0;
    position: absolute;
    top: 50%;
    -ms-transform: translateY(-50%);
    transform: translateY(-50%);
    right: 4%;

  }
}
</style>
