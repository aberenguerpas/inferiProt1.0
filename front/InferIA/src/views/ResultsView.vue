<script setup>
import SearchBarVue from "../components/SearchBar.vue";
import ResultCardVue from "../components/ResultCard.vue";
import SearchFilters from "../components/SearchFilters.vue";
import DataFormVue from "../components/DataForm.vue";
import LoadCompVue from "../components/LoaderComp.vue";
import BreadCrumbs from "../components/BreadCrumbs.vue";
import IconFaceVue from "../components/icons/IconFace.vue";
import AdvanceSearchModel from "../components/AdvanceSearchModel.vue"

//STORES from pinia
import { storeToRefs } from "pinia";
import { useAdvanceSearchStore } from "../store/AdvanceSearch";

//pinia
const store = useAdvanceSearchStore();
const { results } = storeToRefs(store);

const tags = {
  //data of the three promoted buttons
  energy: {
    tags: "energía,energética,contaminantes",
    title: "Energy & Environment",
  },
  economy: {
    tags: "empleo,trabajo,empresas,ayudas,locales",
    title: "Business",
  },

  development: {
    tags: "producción,consumo,reciclaje,basura,residuos,tráfico,materiales,material",
    title: "Circular Economy",
  },
};
</script>

<template>
  <div class="container lg:my-5 my-3 mx-auto lg:px-12 lg:mt-28 mt-24">
  
      <div class="bg-white w-full lg:w-10/12 mx-auto">
        <BreadCrumbs :list="['Results']" />
      </div>

      <div class="bg-white w-full lg:w-10/12 mx-auto">
        <SearchBarVue />
        <SearchFilters/>
      </div>
      <!--Results-->
      <div class="my-3 mx-auto w-full lg:w-10/12 ">
          <p class="text-gray-400">
            Resultados
            <span v-if="results && results['results']">{{
              results["results"].length
            }}</span>
          </p>
        
          <div class="w-full mt-3">
            <hr class="w-full">
          </div>
        
      </div>
   

    <!--Results pintados-->
    <div class="lg:flex  min-w-0 lg:w-10/12 w-full mx-auto">
    
      <div class="w-full lg:w-9/12 mx-auto">
        <div
          v-if="
            results && results['results'] && results['results'].length === 0
          "
          class="m-5 flex items-center justify-center flex-col my-10"
        >
          <div class="py-3">
            <IconFaceVue />
          </div>
          <h5 class="font-bold text-base text-center">
            Ups! No hemos encontrado nada.
          </h5>

          <p class="mt-3 text-center text-xs lg:text-sm">
            No te preocupes, te lo podemos conseguir.<br />
            Háznos saber lo qué necesitas haciendo click
            <a href="https://www.inferia.io/request-data/">aquí</a>
          </p>
        </div>
        <div v-else-if="results === 'loading'" class="text-center">
          <LoadCompVue />
        </div>
        <div v-else class="">
          <div class="lg:w-11/12 w-full min-w-0" v-for="todo in results['results']" :key="todo.title">
            <ResultCardVue :data="todo" />
          </div>
        </div>
      </div>

      <div class="w-full lg:w-3/12 bg-white my-4 lg:my-0 mx-auto flex flex-col items-center justify-center lg:block">
        <DataFormVue/>
        <AdvanceSearchModel/>
      </div>
    </div>
  </div>
</template>

<style scoped>
</style>
