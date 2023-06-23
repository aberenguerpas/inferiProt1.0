<script setup>

import { computed, ref } from 'vue';
const props = defineProps(['data'])


const isFree = ref(true) 
const isButtonMore = ref(false)
const btnTitle = ref('ver más')
const geoContent = ref('')
const all = ref(false)
const notArray = ref(false)

const lastModified = computed( ()=> {
    let lastModi = props.data.modified
    const x = lastModi?.slice(0,16);
    return x
})


const issued = computed( () =>{
    return props.data.issued?.slice(0,16)

})


const time = computed( ()=>{
    if(props.data.temporal?.startDate && props.temporal?.endDate){{
        const f_date = props.data.temporal.startDate?.slice(0,16)
        const s_date = props.data.temporal.endDate?.slice(0,16)
        return f_date + ' - ' + s_date
    }}
   
})

const geo = ()=> {
    if(props.data.geo){
        if(props.data.geo.length > 1 && Array.isArray(props.data.geo)){
            isButtonMore.value = true
            geoContent.value = props.data.geo
        }else if(!Array.isArray(props.data.geo)){
            geoContent.value = props.data.geo
            isButtonMore.value = false
            notArray.value = true
        }
    }else{
        geoContent.value = '---'
    }
}

const showMoreOrLess = () =>{
    if(btnTitle.value === 'ver más'){
        geoContent.value = props.data.geo
        btnTitle.value = 'ver menos';
        all.value = true
    }else if(btnTitle.value === 'ver menos'){
        geo.value = props.data.geo[0];
        btnTitle.value = 'ver más';
        all.value = false
    }
}

geo()
</script>


<template>
   <div class="min-w-[300px] max-w-[500px] cardx p-4 border-2 border-gray-100 rounded-md truncate w-full">
        <h6 class="font-bold mt-3 text-sm"> Precio</h6>
        <h6 class="font-semibold green mt-1 text-xs pl-2" :class="{ free: isFree, pay: !isFree}" >Gratis</h6>
        <h6 class="font-bold mt-3 text-sm">Licencia</h6>
        <a :href="data.license" class="text-xs pl-2">  {{  data.license }}</a>
        <h6 class="font-bold mt-3 text-sm">Fuente</h6>
        <a :href="`https://${data.provider}`" class="text-xs pl-2"> {{ data.provider }}</a>
        <h6 class="font-bold mt-3 text-sm">Creado</h6>
        <p class="px-2 text-xs pl-2">{{ issued || "---"}} </p>
        <h6 class="font-bold mt-3 text-sm">Última modificación</h6>
        <p class="px-2 text-xs pl-2"> {{  lastModified || "---" }}</p>
        <h6 class=" font-bold mt-3 text-sm">Cobertura temporal</h6>
        <p class="px-2 text-xs pl-2">{{ time || '---'}}</p>
        <h6 class="font-bold mt-3 text-sm">Cobertura geográfica</h6>
        <ul class="px-2 text-xs pl-2" v-if="all">
            <li v-for="place in geoContent"> {{ place}} </li>
        </ul>
        <ul v-else-if="!all && !notArray">
            <li class="px-2"> {{ geoContent[0] }}</li>
        </ul>
        <p v-else-if="notArray"> {{ geoContent }}</p>
        <div v-if="isButtonMore" class="mt-3"> 
            <p @click="showMoreOrLess" class="text-muted text-end"> <u class="cursor-pointer">{{ btnTitle }}</u> </p>
        </div>
    </div>
</template>


<style scoped>
.cardx{
    box-shadow: 0px 5px 15px -4px rgba(0, 0, 0, 0.1);
    
}

ul {
  list-style-type: none;
  margin: 0 ;
  padding: 0;
}

h6 {
    color: #06283D;
}

a, h5{
    color: #47B5FF;
}

.free{
    color: #38b000;
}
</style>