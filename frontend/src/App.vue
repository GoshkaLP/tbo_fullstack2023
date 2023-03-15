<template>
  <div id="app">
    <NavbarMain/>
    <router-view ></router-view>
  </div>
</template>

<script>
  import NavbarMain from "@/components/NavbarMain.vue";
  export default {
    name: 'App',
    components: {
      NavbarMain
    },
    data() {
      return {
      }
    },
    // methods: {
    //   updateMapHeight(height) {
    //     this.navbarHeight = height;
    //     console.log(this.navbarHeight)
    //   }
    // }
  }

</script>

<style>

</style>