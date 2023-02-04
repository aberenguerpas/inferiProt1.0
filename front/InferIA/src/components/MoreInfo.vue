<script setup>

import { computed } from 'vue';
const props = defineProps(['data'])



const lastModified = computed( ()=> {
        let lastModi = props.data.modified
        const x = lastModi?.slice(0,16);
        return x
        
    })

</script>


<template>

   <div class="border border-primary-subtle plus_info">
        <h5 class="fw-bold mt-3">  Licencia </h5>
        <a :href="data.license">  {{  data.license }}</a>
        <h5 class="fw-bold mt-3">Fuente</h5>
        <a :href="`https://${data.provider}`"> {{ data.provider }}</a>
        <h5 class="fw-bold mt-3">Última modificación</h5>
        <p class="mb-3"> {{  lastModified || "---" }}</p>
        
       
        <!--<h5 class=" fw-bold mt-3">Cobertura temporal</h5>
        <p> {{  datex }}</p>
        <h5 class="fw-bold mt-3"> Nº de filas </h5>
        <p> {{ info.n_rows }}</p>
        <h5 class="fw-bold mt-3"> Cobertura geografica </h5> -->
    </div>
</template>