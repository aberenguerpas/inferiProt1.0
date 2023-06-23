<script setup>
import { useRouter } from "vue-router";
const router = useRouter();

const props = defineProps([
  "title",
  "img_src",
  "bono",
  "pointer",
  "description",

]);

const show = () => {
  router.push(props.pointer);
};
</script>

<template>
  <div class="mx-auto border-2 border-gray-100 rounded-lg lg:flex cardx">
    <div class="hidden lg:grid lg:w-1/4 mr-3" v-if="props.bono">
      <img
        src="../assets/img/bonoimg.jpg"
        class="rounded-l-lg object-cover w-full h-full"
      />
    </div>

    <div class="hidden lg:grid lg:w-1/4 mr-3" v-else>
      <img :src="img_src" class="rounded-l-lg object-cover w-full h-full" />
    </div>
    <!--text part-->
    <div class="lg:w-3/4 w-full p-4">
      
      <div class="flex mb-3" v-if="props.title == 'Bonoconsumo'">
      <img
        src="../assets/img/bonoimg.jpg"
        class="rounded-lg object-cover w-3/12 m-2 visible lg:hidden"
      />

      <div class="flex flex-col">
        
        <h3 class="font-semibold text-base text-gray-700 lg:text-xl">{{ title }}</h3>
        <div class="flex flex-wrap text-xs lg:text-sm">
          <span
            class="m-0.5 rounded-full my-1 bg-gradient-to-r from-cyan-500 to-blue-500 px-4 py-0.5 text-white"
            >Compras</span
          >
          <span
            class="mr-0.5 rounded-full my-1 bg-gradient-to-r from-cyan-500 to-blue-500 px-4 py-0.5 text-white"
            >Economía</span
          >
          <span
            class="mr-0.5 rounded-full my-1 bg-gradient-to-r from-cyan-500 to-blue-500 px-4 py-0.5 text-white"
            >Comercio
          </span>
        </div>
        </div>
      </div>
      <div class="description-wrapper">
        <p class="lg:my-4 text-sm lg:text-base description">
          {{ description }}
          ...
        </p>
      </div>

      <button
        @click="show"
        class="rounded-full bg-[#06283D] px-6 py-2 mt-3 text-white hover-bg-white text-[#]"
      >
        Ver
      </button>
    </div>
  </div>
</template>

<style scoped>
.description {
  display: -webkit-box;
  -webkit-line-clamp: 5;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
