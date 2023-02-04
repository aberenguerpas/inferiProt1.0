<script setup >
import { ref, onMounted } from 'vue'
import {useLastKeyStore} from '../store/LastSearch.js'
import { storeToRefs } from 'pinia';
const useLastKey = useLastKeyStore()

const {keywords} = storeToRefs(useLastKey)

const emit = defineEmits(['response'])
/*keywords.value = ref(new URLSearchParams(window.location.search).get('keywords'))*/

onMounted(() => {
  if(keywords.value){
    document.getElementById('textInput').value = keywords.value
    onEnter()
  }


  if(new URLSearchParams(window.location.search).has('keywords'))
    onEnter()
    
})

async function onEnter(){
  
    keywords.value =  document.getElementById('textInput').value
    emit('response', 'loading')
    window.dataLayer = window.dataLayer || [];
 		window.dataLayer.push({'event': 'busqueda','searchtext': keywords.value});
    const response = await fetch("http://inferia.io/api/search?keywords="+keywords.value,{
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
  <input  placeholder="Buscar.." id="textInput">
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
        margin-top:1em;
        margin-bottom:1em;
    }

    .lupa{
        position: absolute;
        top: 35%;
        left: 1.5em;
        color: #5c7284;
        z-index: 2;
    }
</style>