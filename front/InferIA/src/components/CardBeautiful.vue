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
    <div class="lg:w-3/4 w-full p-5">
      <h3 class="font-semibold text-xl text-gray-700">{{ title }}</h3>
      <div class="flex mt-3 flex-wrap">
        <span
          class="mr-2 lg:my-0 my-2 rounded-full bg-gradient-to-r from-cyan-500 to-blue-500 px-4 py-0.5 text-white"
          >Shopping</span
        >
        <span
          class="mr-2 rounded-full my-2 lg:my-0 bg-gradient-to-r from-cyan-500 to-blue-500 px-4 py-0.5 text-white"
          >Economy</span
        >
        <span
          class="mr-2 rounded-full my-2 lg:my-0 bg-gradient-to-r from-cyan-500 to-blue-500 px-4 py-0.5 text-white"
          >Local Trade
        </span>
      </div>
      <div class="description-wrapper">
        <p class="my-5 lg:my-4 text-base description">
          {{ description }}
          ...
        </p>
      </div>

      <button
        @click="show"
        class="rounded-full bg-[#06283D] px-6 py-2 mt-4 text-white hover-bg-white text-[#]"
      >
        Preview
      </button>
    </div>
  </div>
</template>

<style scoped>
.description {
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.description-wrapper {
  height: 6em;
}
</style>
