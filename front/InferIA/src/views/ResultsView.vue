<script setup>
import SearchBarVue from '../components/SearchBar.vue';
import ResultCardVue from '../components/ResultCard.vue';
import DataFormVue from '../components/DataForm.vue';
import LoadCompVue from '../components/LoaderComp.vue';
import BreadCrumbs from '../components/BreadCrumbs.vue';

import {ref } from 'vue';
const results = ref([])
</script>


<template>
    <div class= "container mb-5">
      <div class="row">
        <div class="col-12">
          <BreadCrumbs :list="['Búsqueda']"/>
          <SearchBarVue @response="(msg) => results = msg" />
          <p> <strong>Resultados:</strong> {{ results['total']}}</p>
          <hr>
        </div>
      </div>
      
      <div class="row ">
        <div class="col-12 col-lg-8">
          <div v-if="results['results']==0">
            <p class="mt-5">No hemos encontrado ningún resultado para tu búsqueda :(</p>
          </div>
          <div v-else-if="results=='loading'">
            <LoadCompVue/>
          </div>
        <div v-else> 
            <div v-for="todo in results['results']" :key="todo.title">
                <ResultCardVue :data="todo" />
            </div>
        </div>
        </div>
        <div class="col-lg-4 col-12">
          <DataFormVue/>
        </div>
        
      </div>
    
    
    </div>

</template>

<style scoped>

@media only screen and (min-width: 1000px) {
  .data {
    width: 350px;
  }
}

</style>