<template>
  <div class="text-center">
  </div>
</template>

<script>
export default {
  name: 'ModalCreated',
  props: {
    showModal: Boolean,
  },
  data() {
    return {
      localShowModal: this.showModal
    }
  },
  watch: {
    localShowModal(newValue) {
      this.$emit('update:showModal', newValue)
    },
  },
}
</script>
