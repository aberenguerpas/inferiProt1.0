<script setup >
import { onMounted } from 'vue'
import { useLastKeyStore } from '../store/LastSearch.js'
import { storeToRefs } from 'pinia';

const useLastKey = useLastKeyStore()
const { keywords } = storeToRefs(useLastKey)
const emit = defineEmits(['response'])


onMounted(() => {
  if(keywords.value){
    document.getElementById('textInput').value = keywords.value
    onEnter()
  }

  const searchParams = new URLSearchParams(window.location.search)
  if(searchParams.has('keywords')){
    document.getElementById('textInput').value = searchParams.get('keywords')
    onEnter()  
  }
})

//This function makes the search
async function onEnter(){
    keywords.value =  document.getElementById('textInput').value
    emit('response', 'loading')

    //It's for Google Analytics
    window.dataLayer = window.dataLayer || [];
 		window.dataLayer.push({'event': 'busqueda','searchtext': keywords.value});

    const response = await fetch("http://inferia.io/api/search-test?keywords="+keywords.value,{
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
  <input placeholder="Search" id="textInput" autocomplete="off" class="searchBar">
</form>
</template>

<style>
    .searchBar{
        padding: 1em;
        border-radius: 2em;
        width: 100%;
        border: none;
        padding-left: 3.5em;
        margin-top:1em;
        margin-bottom:1em;
        box-shadow: 0 2px 5px 1px rgb(64 60 67 / 16%)
    }

    .lupa{
        position: absolute;
        top: 35%;
        left: 1.5em;
        color: #5c7284;
        z-index: 2;
    }
</style>