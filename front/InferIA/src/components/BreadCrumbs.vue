<script setup>
import { useRouter } from "vue-router";
import IconHome from "./icons/IconHome.vue";
import IconArrow from "./icons/IconArrow.vue";
const props = defineProps(["list"]);
const router = useRouter();

const routes = ['/', '/useCases','/providers']

const back = (item) => {
  if(item.toLowerCase() === 'search'){
    router.push(routes[0])
  }else if(item.toLowerCase() === 'use cases'){
    router.push(routes[1])
  }else if(item.toLowerCase() === 'providers'){
    router.push(routes[2])
  }
};
</script>

<template>
  <div class="flex items-center py-4 overflow-x-auto whitespace-nowrap justify-normal">
    <a href="https://www.inferia.io/">
      <IconHome />
    </a>

    <span v-for="item in props.list" :key="item"  @click="back(item)" class="flex">
        <IconArrow />
    <a class="text-gray-600">
     {{ item }}
    </a>
    </span>
 
  </div>
</template>

<style scoped>

    a{
        /*color: rgb(75 85 99)!important;*/
        cursor: pointer !important;
      
    }
</style>