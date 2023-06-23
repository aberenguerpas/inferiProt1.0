<script setup>
import { useRoute } from "vue-router";
import BreadCrumbs from "../components/BreadCrumbs.vue";
import CardBeautiful from "../components/CardBeautiful.vue";
import {useFakeProviders} from '../store/fakeProviders'

const store = useFakeProviders()
const { providers } = store
const route = useRoute();
const name = route.params.name;
</script>

<template>
  <div
    class="container lg:my-5 lg:mx-auto lg:px-12 lg:mt-32 mt-24"
  >
    <div class="w-full lg:w-8/12 mx-auto">
      <BreadCrumbs :list="['Providers', `${name}`]" />
    </div>
    <div class="w-full lg:w-8/12 mx-auto my-6">
    <div class="flex items-start">
      <img class="rounded-lg w-2/12" :src="providers[name].img">
      <div class="flex flex-col mb-3 ml-3">
      <h1 class="text-left font-semibold mb-1 underline underline-offset-8 decoration-pink-500">
        {{ name }}
      </h1>
      <a :href="providers[name].url">{{ providers[name].url }}</a>
      <div class="flex flex-wrap">
        <div v-for="topic in providers[name].topics">
          <span
            class="m-0.5  text-xs lg:text-sm lg:my-0 rounded-full bg-gradient-to-r from-cyan-500 to-blue-500 px-2 py-0.5 text-white">
            {{ topic }}
          </span>
        </div>
      </div>
    </div>
    </div>
      <p class="text-sm lg:text-base text-gray-500 my-6">
        {{  providers[name].description }}
      </p>
  <div class="mx-auto my-6 flex flex-wrap ">
    <div
      class="mx-auto flex flex-col justify-center items-center"
    >
    <font-awesome-icon v-if="providers[name].type == 'Open'"  class="text-xl opacity-25" :icon="['fas', 'lock-open']" />
    <font-awesome-icon v-else class="text-xl opacity-25" :icon="['fas', 'lock']" />

    <div class="flex justify-center items-center">
        <p class="m-3 text-center text-sm">{{providers[name].type}}</p>
      </div>
    </div>
    <div
      class="mx-auto flex flex-col justify-center items-center"
    >
    <font-awesome-icon class="text-xl opacity-25" :icon="['fas', 'earth-americas']" />
      <div class="flex justify-center items-center">
        <p class="m-3 text-center text-sm">{{providers[name].geo}}</p>
      </div>
    </div>
    <div
      class="mx-auto flex flex-col justify-center items-center"
    >
    <font-awesome-icon class="text-xl opacity-25" :icon="['fas', 'database']" />
      <div class="flex justify-center items-center">
        <p class="m-3 text-center text-sm">{{providers[name].n_data}}</p>
      </div>
    </div>
  </div>
  <div v-if="providers[name].type == 'Private'" class="min-w-[256px] max-w-[500px] w-full">
        <div class="card-body flex flex-col text-center px-8 py-8 border-2 border-gray-100 rounded-md items-center justify-center">
          <i class="bi bi-megaphone " style="font-size: 2rem; color:#66666E;"></i>
          <h5 class="font-bold text-base">Are you interested in the data of this provider or similar?</h5>
         <p class="text-justify text-sm text-gray-400 mt-2">We can get what you need, just tell us what is it, and you will have it very soon! <span class="fw-bold">It is free.</span></p>
          <a href="https://www.inferia.io/request-data/" class="rounded-full bg-[#06283D] text-white mt-4 py-2 px-4 btn-btn">Request</a>
        </div>
    </div>
    <div v-if="providers[name].useCase" class="w-full lg:my-20 my-14 mx-auto">
      <h1 class="text-left text-base font-semibold my-3 underline underline-offset-8 decoration-orange-500">
       Casos de uso
      </h1>
      <CardBeautiful
        title="Bonoconsumo"
        pointer="/useCases/bonoconsumo"
        img_src="/src/assets/img/bonoimg.jpg"
        description="Actualmente, el bonoconsumo se ha convertido en una estrategia eficaz para promover el crecimiento económico y mejorar la calidad de vida de los habitantes de las ciudades. Es necesario analizar este fenómeno para descubrir su verdadero impacto en la economía de las ciudades."
      />
    </div>
    </div>
  </div>

</template>

<style scoped>

.container {
  font-family: "Ubuntu", sans-serif !important;
}

.card-effect {

  background: rgb(26,71,252);
background: linear-gradient(299deg, rgba(26,71,252,0) 0%, rgba(29,111,233,0) 83%, rgba(32,159,211,1) 100%);

}
</style>
