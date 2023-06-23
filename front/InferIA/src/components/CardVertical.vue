<script setup>
import { RouterLink} from "vue-router";
const props = defineProps(["img_src", 'description', 'title', 'topics']);
</script>

<template>
   <router-link :to="`/providers/${title}/`" id="router-link">
    <div class="xl:w-[350px] lg:w-[350px] md:w-[350px]  min-w-[300px] w-full mx-auto flex flex-col py-2 px-5 rounded-lg card ">
      <div class="py-2 mx-auto">
        <div class="flex flex-wrap items-center">
          <img :src="img_src" class="w-2/12 mr-4 rounded-md" />
          <div class="flex flex-col w-8/12">
            <h4 class="wrapper-title font-bold text-[#06283D] lg:text-base">{{ title }}</h4>
            <div class="flex flex-wrap py-1 text-xs" >
              <div class="m-0.5 rounded-full bg-gradient-to-r from-cyan-500 to-blue-500 px-2 py-0.5 text-white" v-for="t in topics">
                {{ t }}
              </div>
            </div>
          </div>
        </div>
          <div class="description-wrapper py-2 leading-6">
            <p class="description text-xs lg:text-base">{{ description }}</p>
          </div>
      </div>
  </div>
  </router-link>
 
</template>

<style scoped>
.description {
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.wrapper-title{
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
.card{
  box-shadow: 0 5px 15px rgba(0, 0, 0, 15%);
}
</style>
