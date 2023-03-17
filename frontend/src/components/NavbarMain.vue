<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark" class="navbarMain">
      <b-navbar-brand class="navbar-main-brand">TBOMap</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>

        <b-navbar-nav>
          <b-nav-item :to="{path: '/'}">Карта</b-nav-item>
          <b-nav-item :to="{path: '/analytics'}">Аналитика</b-nav-item>

        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <b-nav-item @click="showHelpModal">
            <b-icon icon="question-circle-fill" aria-label="Help"></b-icon>
          </b-nav-item>
        </b-navbar-nav>

        <b-modal ref="helpModal" scrollable hide-footer no-body>
          <HelpComponent></HelpComponent>
        </b-modal>

      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import HelpComponent from "@/components/HelpComponent.vue";

export default {

  name: "NavbarMain",
  components: {
    HelpComponent
  },
  methods: {
    showHelpModal() {
      this.$refs['helpModal'].show();
    }
  }


}
</script>

<style >

  .navbar.navbar-dark.bg-dark{
    background-color: #3b1b64! important;
  }

  .modal-body {
    padding: 0 !important;
  }

  .modal-dialog {
    max-width: 1024px !important;
    max-height: 543px !important;
  }

</style>