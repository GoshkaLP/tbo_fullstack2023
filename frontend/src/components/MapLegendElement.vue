<template>
  <div>
    <div :style="style"></div>
    <p style="display: inline-block; margin-left: 10px;">
      <slot/>
    </p>
  </div>
</template>

<script>
export default {
  name: "MapLegendElement",
  props: ['color'],
  computed: {
    style() {
      return "display: inline-block; background-color: " + this.color + "; width: 15px; height: 15px;"
    }
  }
}
</script>

<style scoped>

</style>