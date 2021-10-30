<template>
    <v-text-field
      outlined
      v-bind="{ ...$props, ...$attrs }"
      v-on="$listeners"
      height='65'
    >
      <template v-for="(index, name) in $slots" #[name]>
        <slot :name="name" />
      </template>
    </v-text-field>
</template>

<script>
export default {
  name: 'AppTextField',
}
</script>
<style lang='scss' scoped>
@import 'text_field.scss';
</style>
