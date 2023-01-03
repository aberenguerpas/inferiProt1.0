<script setup >
import {ref} from 'vue'

const emit = defineEmits(['response'])
const keywords = ref('')

async function onEnter(){
    emit('response', 'loading')
    const response = await fetch("http://localhost:8000/search?keywords="+keywords.value,{
    headers: new Headers({ 'Content-type': 'application/json'}),
    })

    if(response.ok){
      const res = await response.json()
      emit('response', res)
    }
   
}
</script>

<template>
<form id="searchBox" @submit.prevent="onEnter">
  <i class="bi bi-search lupa"></i>
  <input v-model="keywords" placeholder="Buscar...">
</form>
</template>

<style>
    input{
        background-color: #f7f8f9;
        padding: 1em;
        border-radius: 2em;
        width: 100%;
        border: none;
        padding-left: 3.5em;
        margin-bottom:1em;
    }

    .lupa{
        position: absolute;
        top: 22%;
        left: 1.5em;
        color: #5c7284;
        z-index: 2;
    }
</style>