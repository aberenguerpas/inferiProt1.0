<script setup>
import BreadCrumbs from "../components/BreadCrumbs.vue";

import { useFakeProviders } from "../store/fakeProviders";
import CardVertical from "../components/CardVertical.vue";

const store = useFakeProviders();

const { providers } = store;
</script>

<template>
  <div
    class="container lg:my-5 mx-auto lg:px-12 lg:mt-32 my-24 min-h-screen"
  >
    <div class="w-full lg:w-8/12 mx-auto">
      <BreadCrumbs :list="['Providers']" />
    </div>

    <h1
      class="text-center lg:text-5xl text-4xl font-semibold lg:my-5 lg:py-6 my-3 py-3 underline underline-offset-8 decoration-pink-500"
    >
      Providers
    </h1>

    <div class="w-full lg:w-8/12 md:w-10/12 mx-auto md:flex md:flex-wrap mt-8 " >
      <div v-for="item in providers" class=" mx-auto mb-6">
        <CardVertical
          :img_src="item.img"
          :title="item.name"
          :description="item.description"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  font-family: "Ubuntu", sans-serif !important;
}
</style>
