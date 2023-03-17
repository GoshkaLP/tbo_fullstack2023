<template>
  <div id="app">
    <NavbarMain />
    <router-view />
  </div>
</template>

<script>
  import NavbarMain from "@/components/NavbarMain.vue";

  export default {
    name: 'App',
    components: {
      NavbarMain
    }
  }

</script>

<style>

</style>