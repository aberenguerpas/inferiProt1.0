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
  <div>
  <main>
    <headerCompVue/>
    <SearchBarVue @response="(msg) => results = msg" />
    <p> <strong>Resultados:</strong> {{ results['total']}}</p>
    <hr>
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
        <div class="col-4 dataform">
          <DataFormVue/>
        </div>
        <div class="dataformMob">
          <DataFormVue/>
        </div>
      </div>
    </div>
  </main>
</div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

*{
  font-family: 'Poppins', sans-serif;
}

.container{
  margin-left: 0;
  margin-right: 0;
  padding: 0;
}

@media only screen and (max-width: 992px) {

  .dataform{
        display: none!important;
  }
  .col-8{
    width: 100%;
  }
  .dataformMob > img{
    width: 30%!important;
  }
  body { padding-top: 100px; } 
}

@media only screen and (min-width: 992px) {
  .dataformMob{
    display: none;
  }
}
</style>
