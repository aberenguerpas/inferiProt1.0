<script setup>
import SearchBarVue from '../components/SearchBar.vue';
import ResultCardVue from '../components/ResultCard.vue';
import DataFormVue from '../components/DataForm.vue';
import LoadCompVue from '../components/LoaderComp.vue';
import BreadCrumbs from '../components/BreadCrumbs.vue';
import { ref } from 'vue';

const results = ref([])
</script>

<template>
    <div class= "container mb-5">
      <div class="row">
        <div class="col-12">
          <BreadCrumbs :list="['Search']"/>
          <SearchBarVue @response="(msg) => results = msg" />
          <p>Results {{ results['total']}}</p>
          <hr>
        </div>
      </div>
      
      <div class="row">
        <div class="col-12 col-lg-8">
          <div v-if="results['results']==0" class="text-center m-5">
            <h5 class="fw-bold fs-4"> Ups! We haven't found anything!</h5>
            <p class="mt-3 text-center">Don't worry, we get can get it for you!<br> Let us know what you need clicking <a href="https://www.inferia.io/solicitar_datos">here.</a></p>
          </div>
          <div v-else-if="results=='loading'" class="text-center" >
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