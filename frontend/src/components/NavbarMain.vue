<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark" class="navbarMain">
      <b-navbar-brand class="navbar-main-brand">TBOMap</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>

        <b-navbar-nav class="ml-auto">
          <b-nav-item :to="{path: '/'}">Карта</b-nav-item>
          <b-nav-item>Аналитика</b-nav-item>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>


export default {

  name: "NavbarMain",


}
</script>

<style scoped>
  .navbar-main-brand {
    padding-left: 1%;
  }

  .navbar.navbar-dark.bg-dark{
    background-color: #3b1b64! important;
  }

</style>