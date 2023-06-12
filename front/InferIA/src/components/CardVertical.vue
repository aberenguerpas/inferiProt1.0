<script setup>
import { RouterLink} from "vue-router";
const props = defineProps(["img_src", 'description', 'title']);
</script>

<template>
   <router-link :to="`/providers/${title}/`" id="router-link">
    <div class="xl:w-[350px] lg:w-[290px]  md:w-[250px]  min-w-[250px] w-full mx-auto flex flex-col py-2 px-5 rounded-lg card ">
    <div class="py-2">
      <div class="flex items-center ">
        <img :src="img_src" class="w-2/12 mr-3 rounded-md" />
        <div class="wrapper-title">
          <h5 class="font-bold text-[#06283D] text-xl title ">{{ title }}</h5>
        </div>
       
      </div>
        
        <div class="description-wrapper py-4">
          <p class="description">{{ description }}</p>
        </div>
    </div>
   
    
  </div>
  </router-link>
 
</template>

<style scoped>
.description {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.description-wrapper{
  height: 4em;
}

.wrapper-title{
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.title{
  height: 1.5em;
}

.card{
  box-shadow: 0 5px 15px rgba(0, 0, 0, 15%);
}



</style>


