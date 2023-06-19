<script setup>
import BreadCrumbs from "../components/BreadCrumbs.vue";

import { useFakeProviders } from "../store/fakeProviders";
import CardVertical from "../components/CardVertical.vue";

const store = useFakeProviders();

const { providers } = store;
</script>

<template>
  <div
    class="container lg:my-5 mx-auto lg:px-12 lg:mt-32 my-24"
  >
    <div class="w-full lg:w-8/12 mx-auto">
      <BreadCrumbs :list="['Providers']" />
    </div>
    <div class="w-full lg:w-6/12 md:w-10/12 mx-auto md:flex md:flex-wrap mt-3" >
      <div v-for="item in providers" class=" mx-auto mb-6">
        <CardVertical
          :img_src="item.img"
          :title="item.name"
          :description="item.description"
          :topics="item.topics"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
