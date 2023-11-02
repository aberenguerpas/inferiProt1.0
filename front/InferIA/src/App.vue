<script setup>
import headerCompVue from "./components/HeaderComp.vue";
import { RouterView } from "vue-router";
import FooterComp from "./components/FooterComp.vue";
import Chatbox from "./components/Chatbox.vue";
</script>

<template>

  <headerCompVue />

  <RouterView />
  <Chatbox />
  <FooterComp />
 
</template>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins&display=swap");

* {
  font-family: "Poppins", sans-serif;
}

@media only screen and (max-width: 992px) {
  .dataform {
    display: none !important;
  }

  .col-8 {
    width: 100%;
  }

  .dataformMob>img {
    width: 30% !important;
  }

  body {
    padding-top: 100px;
  }
}

@media only screen and (min-width: 992px) {
  .dataformMob {
    display: none;
  }
}
</style>
