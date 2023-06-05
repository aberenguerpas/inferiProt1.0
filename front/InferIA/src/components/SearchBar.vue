<script setup>
import { onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useAdvanceSearchStore } from "../store/AdvanceSearch";
import IconLupaVue from "./icons/IconLupa.vue";

//pinia
const store = useAdvanceSearchStore();
const { results } = storeToRefs(store);
const { keywords } = storeToRefs(store);

onMounted(() => {
  if (keywords.value) {
    onEnter();
  }

  const searchParams = new URLSearchParams(window.location.search);
  if (searchParams.has("keywords")) {
    keywords.value = searchParams.get("keywords");
    onEnter();
  }
});

//This function makes the search
async function onEnter() {
  results.value = "loading";

  //It's for Google Analytics
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({ event: "busqueda", searchtext: keywords.value });

  try {
    const response = await fetch(
      "http://inferia.io/api/search/?keywords=" + keywords.value,
      {
        headers: new Headers({ "Content-type": "application/json" }),
      }
    );
    if (response.ok) {
      const res = await response.json();
      results.value = res;
      console.log("ok", results.value);
    }
  } catch (error) {
    console.log(error);
  }
}
</script>

<template>
  
    <form
      id="searchBox"
      @submit.prevent="onEnter"
      class="flex rounded-full justify-right items-center w-full py-1 px-2 hover:shadow-lg"
      
    >
      <IconLupaVue class="px-1"/>

      <input
        placeholder="Search"
        id="textInput"
        autocomplete="off" 
        class="p-1 border-0 my-1 pl-2 w-5/6"
        v-model="keywords"
      />
    </form>
  
</template>

<style scoped>
#searchBox{
  box-shadow: 0 2px 5px 1px rgb(64 60 67 / 16%);
}
</style>
