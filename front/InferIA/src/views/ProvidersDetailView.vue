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
  INE: "https://www.ine.es/",
  "Dades Obertes": "https://governobert.gencat.cat/ca/dades_obertes/inici/",
  'APYMECO': 'https://www.apymeco.info/',
  'Open Street Maps' : 'https://www.openstreetmap.org/',
  AEMET: 'https://www.openstreetmap.org/'
};


</script>

<template>
  <div
    class="container lg:my-5 lg:mx-auto lg:px-12 lg:mt-32 my-24 min-h-screen"
  >
    <div class="w-full lg:w-8/12 mx-auto">
      <BreadCrumbs :list="['Providers', `${name}`]" />
    </div>

    <h1
      class="text-center lg:text-5xl text-4xl font-semibold lg:my-5 lg:py-6 my-3 py-3 underline underline-offset-8 decoration-pink-500"
    >
      {{ name }}
    </h1>

    <div class="w-full lg:w-8/12 mx-auto my-6">
      <p class="lg:px-3 text-gray-500">
        {{  providers[name].description }}
      </p>
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
