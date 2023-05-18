<script setup>
import { onMounted } from 'vue'
import { storeToRefs } from 'pinia';
import { useAdvanceSearchStore } from '../store/AdvanceSearch'

//pinia
const store = useAdvanceSearchStore()
const { results } = storeToRefs(store)
const { keywords  } = storeToRefs(store)

onMounted(() => {
  if(keywords.value){
    onEnter()
  }

  const searchParams = new URLSearchParams(window.location.search)
  if(searchParams.has('keywords')){
    keywords.value = searchParams.get('keywords')
    onEnter()
  }
})

//This function makes the search
async function onEnter(){

    results.value = 'loading'

    //It's for Google Analytics
    window.dataLayer = window.dataLayer || [];
 		window.dataLayer.push({'event': 'busqueda','searchtext': keywords.value});

    try{
      const response = await fetch("http://inferia.io/api/search/?keywords="+ keywords.value,{
                                  headers: new Headers({ 'Content-type': 'application/json'}),
      })
      if(response.ok){
        const res = await response.json()
        results.value = res
        console.log('ok', results.value)
      }
    }catch(error){
      console.log(error)
    }

}
</script>

<template>
  <form id="searchBox" @submit.prevent="onEnter">
    <i class="bi bi-search lupa"></i>
    <input
      placeholder="Search"
      id="textInput"
      autocomplete="off"
      class="searchBar"
      v-model="keywords"
    />
  </form>
</template>

<style scoped>
.searchBar {
  padding: 1em;
  border-radius: 2em;
  width: 100%;
  border: none;
  padding-left: 3.5em;
  margin-top: 1em;
  margin-bottom: 1em;
  box-shadow: 0 2px 5px 1px rgb(64 60 67 / 16%);
}

.lupa {
  position: absolute;
  top: 35%;
  left: 1.5em;
  color: #5c7284;
  z-index: 2;
}
</style>
