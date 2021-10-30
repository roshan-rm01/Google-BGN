<template>
  <v-dialog
    v-bind="{ ...$props, ...$attrs }"
    :content-class="
      mobileDenseMargin ? 'dense-margin base-modal-inner' : 'base-modal-inner'
    "
    v-on="$listeners"
    @input="handleClose"
  >
    <template v-for="(slot, name, index) in $slots" #[name]>
      <div v-if="name === 'default'" :key="index">
        <div
          v-if="showCloseBtn"
          class="base-modal__close-icon"
          @click="closeModal()"
        >
          <modal-close-icon />
        </div>
      </div>
      <div :key="name">
        <slot :name="name" />
      </div>
    </template>
  </v-dialog>
</template>

<script>
import ModalCloseIcon from '~/assets/icons/modal-close.svg?inline'
export default {
  name: 'BaseModal',
  components: {
    ModalCloseIcon,
  },
  props: {
    mobileDenseMargin: {
      type: Boolean,
      default: false,
    },
    headerTitle: {
      type: String,
      default: '',
    },
    showCloseBtn: {
      type: Boolean,
      default: true,
    },
  },
  methods: {
    closeModal() {
      this.$emit('input', false)
      this.$emit('close')
    },
    handleClose(value) {
      if (!value) {
        this.$emit('close')
      }
    },
  },
}
</script>

<style lang="scss">
.base-modal-inner {
  background-color: #fff;
  box-shadow: 0 5px 10px rgba(1, 8, 89, 0.1) !important;
  border-radius: 24px !important;
  position: relative;
  &.dense-margin {
    @media screen and (max-width: 400px) {
      margin: 12px !important;
    }
  }
}

.v-overlay {
  .v-overlay__scrim {
    display: none;
    opacity: 1 !important;
    background: rgba(0, 15, 53, 0.1) !important;
    mix-blend-mode: normal;
    border-color: rgba(0, 15, 53, 0.1) !important;
  }
  &.v-overlay--active .v-overlay__scrim {
    display: block;
    backdrop-filter: blur(5px);
  }
}
.base-modal__close-icon {
  position: absolute;
  top: 30px;
  right: 30px;
  cursor: pointer;
  opacity: 1;
  :hover {
    opacity: 0.9;
  }
  //@include breakpoint('xs') {
  //  top: 20px;
  //  right: 20px;
  //  svg {
  //    width: 24px;
  //    height: 24px;
  //  }
  //}
}
</style>
