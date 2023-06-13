<script setup>
import { useRoute } from "vue-router";
import BreadCrumbs from "../components/BreadCrumbs.vue";
import CardBeautiful from "../components/CardBeautiful.vue";
import {useFakeProviders} from '../store/fakeProviders'

const store = useFakeProviders()
const { providers } = store
const route = useRoute();

const name = route.params.name;

const dataProviders = {
  "Datos.gob": "https://datos.gob.es/es/",
  "INE": "https://www.ine.es/",
  "Dades Obertes": "https://governobert.gencat.cat/ca/dades_obertes/inici/",
  'APYMECO': 'https://www.apymeco.info/',
  'Open Street Maps' : 'https://www.openstreetmap.org/',
  "AEMET": 'https://www.openstreetmap.org/'
};
</script>

<template>
  <div
    class="container lg:my-5 lg:mx-auto lg:px-12 lg:mt-32 my-24 min-h-screen"
  >
    <div class="w-full lg:w-8/12 mx-auto">
      <BreadCrumbs :list="['Providers', `${name}`]" />
    </div>
    <div class="w-full lg:w-8/12 mx-auto my-6">
    <h1
      class="text-left lg:text-5xl text-4xl font-semibold lg:py-6 my-3 py-3 underline underline-offset-8 decoration-pink-500"
    >
      {{ name }}
    </h1>

    <div class="w-full lg:w-8/12 mx-auto my-6">
      <p class="lg:px-3 text-gray-500">
        {{  providers[name].description }}
      </p>
      <div class="w-full lg:w-9/12 mx-auto rounded-lg my-5 lg:flex py-5">
    <div
      class="rounded-lg border-2 border-gray-100 lg:w-4/12 w-full mx-auto flex flex-col justify-center items-center  mr-3"
    >
    <p  class="text-3xl">Type</p>
    <svg xmlns="http://www.w3.org/2000/svg" height="6em" viewBox="0 0 576 512"><!--! Font Awesome Free 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M352 144c0-44.2 35.8-80 80-80s80 35.8 80 80v48c0 17.7 14.3 32 32 32s32-14.3 32-32V144C576 64.5 511.5 0 432 0S288 64.5 288 144v48H64c-35.3 0-64 28.7-64 64V448c0 35.3 28.7 64 64 64H384c35.3 0 64-28.7 64-64V256c0-35.3-28.7-64-64-64H352V144z"/></svg>
      <div class="flex justify-center items-center">
        <p class="text-center text-xl">Private data</p>
      </div>
    </div>
    <div
      class="rounded-lg border-2 border-gray-100 rounded-lg lg:w-4/12 w-full mx-auto flex flex-col justify-center items-center  mr-3"
    >
    <p  class="text-3xl">Geo-coverage</p>
    <svg xmlns="http://www.w3.org/2000/svg" height="6em" viewBox="0 0 512 512"><!--! Font Awesome Free 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M57.7 193l9.4 16.4c8.3 14.5 21.9 25.2 38 29.8L163 255.7c17.2 4.9 29 20.6 29 38.5v39.9c0 11 6.2 21 16 25.9s16 14.9 16 25.9v39c0 15.6 14.9 26.9 29.9 22.6c16.1-4.6 28.6-17.5 32.7-33.8l2.8-11.2c4.2-16.9 15.2-31.4 30.3-40l8.1-4.6c15-8.5 24.2-24.5 24.2-41.7v-8.3c0-12.7-5.1-24.9-14.1-33.9l-3.9-3.9c-9-9-21.2-14.1-33.9-14.1H257c-11.1 0-22.1-2.9-31.8-8.4l-34.5-19.7c-4.3-2.5-7.6-6.5-9.2-11.2c-3.2-9.6 1.1-20 10.2-24.5l5.9-3c6.6-3.3 14.3-3.9 21.3-1.5l23.2 7.7c8.2 2.7 17.2-.4 21.9-7.5c4.7-7 4.2-16.3-1.2-22.8l-13.6-16.3c-10-12-9.9-29.5 .3-41.3l15.7-18.3c8.8-10.3 10.2-25 3.5-36.7l-2.4-4.2c-3.5-.2-6.9-.3-10.4-.3C163.1 48 84.4 108.9 57.7 193zM464 256c0-36.8-9.6-71.4-26.4-101.5L412 164.8c-15.7 6.3-23.8 23.8-18.5 39.8l16.9 50.7c3.5 10.4 12 18.3 22.6 20.9l29.1 7.3c1.2-9 1.8-18.2 1.8-27.5zM0 256a256 256 0 1 1 512 0A256 256 0 1 1 0 256z"/></svg>
      <div class="flex justify-center items-center">
        <p class="text-center text-xl">Spain 🇪🇸</p>
      </div>
    </div>
    <div
      class="rounded-lg border-2 border-gray-100 rounded-lg lg:w-4/12 w-full mx-auto flex flex-col justify-center items-center  mr-3"
    >
    <p>Nº Datasets</p>
    <svg xmlns="http://www.w3.org/2000/svg" height="6em" viewBox="0 0 448 512"><!--! Font Awesome Free 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M448 80v48c0 44.2-100.3 80-224 80S0 172.2 0 128V80C0 35.8 100.3 0 224 0S448 35.8 448 80zM393.2 214.7c20.8-7.4 39.9-16.9 54.8-28.6V288c0 44.2-100.3 80-224 80S0 332.2 0 288V186.1c14.9 11.8 34 21.2 54.8 28.6C99.7 230.7 159.5 240 224 240s124.3-9.3 169.2-25.3zM0 346.1c14.9 11.8 34 21.2 54.8 28.6C99.7 390.7 159.5 400 224 400s124.3-9.3 169.2-25.3c20.8-7.4 39.9-16.9 54.8-28.6V432c0 44.2-100.3 80-224 80S0 476.2 0 432V346.1z"/></svg>
      <div class="flex justify-center items-center">
        <p class="text-center">30K</p>
      </div>
    </div>
  </div>

    </div>

    <div class="w-full lg:w-8/12 mx-auto my-12 lg:my-16">
      <h3 class="text-center font-semibold text-[#06283D] text-3xl">
        Contacto
      </h3>
      <div class="mt-6 mx-auto">
        <a :href="dataProviders[name]">{{ dataProviders[name] }}</a>
      </div>
    </div>

    <div v-if="providers.useCase" class="w-full lg:w-8/12 lg:my-20 my-14 mx-auto">
      <CardBeautiful
        title="Bonoconsumo"
        pointer="/useCases/bonoconsumo"
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sit amet quam enim. Fusce sodales tincidunt lacinia. Donec nec dapibus libero. Quisque accumsan odio vitae metus aliquet aliquam. Curabitur quis tincidunt ex"
      />
    </div>
  </div>
</template>

<style scoped>
.container {
  font-family: "Ubuntu", sans-serif !important;
}

.container a {
  font-size: 20px;
}



.mt-6.mx-auto {
    text-align: center;
}
</style>
