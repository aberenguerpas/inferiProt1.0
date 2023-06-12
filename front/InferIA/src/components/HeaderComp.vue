<script setup>
import { ref } from "vue";
import { RouterLink } from "vue-router";

const open = ref(true);

const toggle = () => {
  open.value ? (open.value = false) : (open.value = true);
};
</script>

<template>
  <nav
    class="fixed top-0 z-50 flex items-center md:px-[40px] px-[20px] py-[25px] flex-wrap justify-between w-full h-24"
  >
    <a class="" href="https://www.inferia.io/">
      <img src="../assets/img/Inferia_negativo.png" alt="Logo" />
    </a>

    <div class="block lg:hidden">
      <button
        @click="toggle"
        class="flex items-center px-3 py-2 border rounded text-[#47b5ff] border-[#47b5ff] hover:text-white hover:border-white"
      >
        <svg
          class="h-3 w-3"
          viewBox="0 0 20 20"
          fill="#47b5ff"
          xmlns="http://www.w3.org/2000/svg"
        >
          <title>Menu</title>
          <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
        </svg>
      </button>
    </div>
    <div
      class="w-full block flex-grow lg:flex lg:items-center lg:w-auto"
      :class="{ burger: open }"
    >
      <div class="text-sm lg:flex-grow lg:flex lg:justify-end">
        <a
          href="https://www.inferia.io/"
          class="block mt-4 lg:inline-block lg:mt-0 text-gray-600 hover:text-[#47b5ff] mr-5"
        >
          Home
        </a>
        <a
          href="https://www.inferia.io/sell-data/"
          class="block mt-4 lg:inline-block lg:mt-0 text-gray-600 hover:text-[#47b5ff] mr-5"
        >
          Sell Your Data
        </a>

        <RouterLink to="/useCases" @click="toggle" class="block mt-4 lg:inline-block lg:mt-0 text-gray-600 hover:text-[#47b5ff] mr-5">
          Use Cases
        </RouterLink>
       
        <RouterLink to="/providers" @click="toggle" class="block mt-4 lg:inline-block lg:mt-0 text-gray-600 hover:text-[#47b5ff] mr-5">
          Providers
        </RouterLink>

        <a
          href="https://www.inferia.io/our-history/"
          class="block mt-4 lg:inline-block lg:mt-0 hover:text-[#47b5ff] text-gray-600 mr-5"
        >
          Our History
        </a>
        <a
          href="https://www.inferia.io/blog/"
          class="block mt-4 lg:inline-block lg:mt-0 text-gray-600 hover:text-[#47b5ff] mr-5"
        >
          Blog
        </a>
        <a
          href="https://www.inferia.io/contact/"
          class="block mt-4 lg:inline-block lg:mt-0 text-gray-600 hover:text-[#47b5ff] mr-5"
        >
          Contact
        </a>
      </div>
      <div>
        <a
          href="https://www.inferia.io/request-data/"
          class="inline-block text-sm px-4 py-3 leading-none border rounded-full text-white border-white hover:border-transparent hover:text-teal-500 bg-[#06283d] mt-4 lg:mt-0"
          >Request Data</a
        >
      </div>
    </div>
  </nav>
</template>

<style scoped>

.active{
  color:#47b5ff;
}


nav {
  height: 90px !important;
  box-shadow: 0px 5px 15px -4px rgba(0, 0, 0, 0.1);
  font-family: "Ubuntu", sans-serif;
  background-color: #fff !important;
}

a {
  font-size: 15px;
}

img {
  width: 90px;
}

@media only screen and (max-width: 1027px) {
  #navbarNav {
    margin: 0;
    margin-top: 1em;
  }

  .burger {
    display: none;
  }

  nav {
    height: auto !important;
    padding-left: 20px !important;
    padding-right: 20px !important;
  }

  .navbar-collapse {
    background: #fafafa;
    margin: 0;
    padding: 0;
  }
}

@media only screen and (max-width: 600px) {
}
</style>
