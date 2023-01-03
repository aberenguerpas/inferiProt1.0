<script setup>
import SearchBarVue from './components/SearchBar.vue';
import ResultCardVue from './components/ResultCard.vue';
import DataFormVue from './components/DataForm.vue';
import HeaderCompVue from './components/HeaderComp.vue';
import LoadCompVue from './components/LoaderComp.vue';

import { ref } from 'vue'

const results = ref([])

</script>

<template>
  <headerCompVue/>
  <main>
    <SearchBarVue @response="(msg) => results = msg" />
    <hr>
   <p> <strong>Resultados:</strong> {{ results['total']}}</p>
    <div class="container text-center">
      <div class="row">
        <div class="col-8">
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
        <div class="col-4">
          <DataFormVue/>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

*{
  font-family: 'Poppins', sans-serif;
  margin-top:0;
  padding-top:0;
}
</style>
