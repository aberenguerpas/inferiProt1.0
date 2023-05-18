<script setup>
import SearchBarVue from "../components/SearchBar.vue";
import ResultCardVue from "../components/ResultCard.vue";
import DataFormVue from "../components/DataForm.vue";
import LoadCompVue from "../components/LoaderComp.vue";
import BreadCrumbs from "../components/BreadCrumbs.vue";
import AdvanceSearchModel from "../components/AdvanceSearchModel.vue";
import PromotedBtn from "../components/PromotedBtn.vue";
//STORES from pinia
import { storeToRefs } from "pinia";
import { useAdvanceSearchStore } from "../store/AdvanceSearch";


//pinia
const store = useAdvanceSearchStore();
const { results } = storeToRefs(store);

const tags = {  //data of the three promoted buttons
  energy: {
    tags: 'energía,energética,contaminantes',
    title: 'Energy & Environment'
  },
  economy: {
    tags: 'empleo,trabajo,empresas,ayudas,locales',
    title: "Business"
  },

  development: {
    tags: 'producción,consumo,reciclaje,basura,residuos,tráfico,materiales,material',
    title: 'Circular Economy'
  }
}
</script>

<template>
  <div class="container mb-5">
    <div class="row">
      <div class="col-12">
        <BreadCrumbs :list="['Search']" />
        <SearchBarVue/>
      </div>
    </div>

    <!--Promoted buttons-->
    <div class="row">
      <div class="col-12 col-lg-4">
        <PromotedBtn :title="tags.energy.title" :tag="tags.energy.tags"/>
      </div>
      <div class="col-12 col-lg-4">
        <PromotedBtn :title="tags.economy.title" :tag="tags.economy.tags"/>
      </div>
      <div class="col-12 col-lg-4">
        <PromotedBtn :title="tags.development.title" :tag="tags.development.tags"/>
      </div>
    </div>

    <!--Results-->
    <div class="row">
      <div class="col-12 py-1"> 
        <p> Results <span v-if="results && results['results']">{{ results['results'].length }}</span> </p>
      </div>
    </div>
    <!--Results pintados-->
    <div class="row">
      <div class="col-12 col-lg-8">
        <div
          v-if="results && results['results'] && results['results'].length === 0"
          class="text-center m-5"
        >
          <h5 class="fw-bold fs-4">Ups! We haven't found anything!</h5>
          <p class="mt-3 text-center">
            Don't worry, we get can get it for you!<br />
            Let us know what you need clicking
            <a href="https://www.inferia.io/request-data/">here.</a>
          </p>
        </div>
        <div v-else-if="results === 'loading'" class="text-center">
          <LoadCompVue />
        </div>
        <div v-else>
          <div v-for="todo in results['results']" :key="todo.title">
            <ResultCardVue :data="todo" />
          </div>
        </div>
      </div>
  
      <div class="col-12 col-lg-4">
        <DataFormVue />
        <AdvanceSearchModel />
      </div>
    </div>
  </div>
  
</template>

