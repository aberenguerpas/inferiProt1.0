<script setup>
import { RouterLink } from "vue-router";

const props = defineProps(["data"]);
console.log("here", props.data);
</script>

<template>
  <router-link :to="`details/${data.id}`">
    <div
      class="lg:flex-col lg:mt-0 my-5 rounded-lg border-2 border-gray-100 cardx min-w-0"
    >
      <div class="flex items-start p-4">
        <img :src="data.img_portal" class="w-1/12 mr-6 rounded-md" />
        <div>
          <div class="wrapper-title"> 
            <h5 class="font-bold text-[#06283D] text-xl title ">
            {{ data.title }}
          </h5>
          </div>
          

          <div class="flex py-1 mb-3 pills text-sm">
            <div
              class="mr-2 rounded-full bg-gradient-to-r from-cyan-500 to-blue-500 px-4 text-white flex items-center justify-center"
            >
              <i
                class="fa-regular fa-file fa-xs mr-1"
                style="color: #ffffff"
              ></i>
              CSV
            </div>
            <div
              class="mr-2 rounded-full bg-gradient-to-r from-cyan-500 to-blue-500 px-4 text-white flex items-center justify-center"
            >
              <i
                class="fa-regular fa-circle-check fa-xs mr-1"
                style="color: #ffffff"
              ></i>
              <a
                :href="data['license']"
                class="hover:bg-gradient-to-r from-cyan-500 to-blue-500 text-sm"
                >License</a
              >
            </div>
            <div
              class="mr-2 rounded-full bg-gradient-to-r from-lime-500 to-green-500 px-4 text-white flex items-center justify-center"
            >
              <i
                class="fa-regular fa-money-bill-1 fa-xs mr-1"
                style="color: #ffffff"
              ></i>
              Free
            </div>
          </div>
          <div class="description-wrapper">
            <p class="card-text text-base description">{{ data.description }}</p>
          </div>
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
  height: 3em;
}

.wrapper-title{
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.title{
  height: 2em;
}

.cardx {
  box-shadow: 0px 5px 15px -4px rgba(0, 0, 0, 0.1);
}

.pills a {
  color: white !important;
}

@media (hover: hover) {
  a:hover {
    background-color: transparent !important;
  }
}

@media only screen and (max-width: 992px) {
  li,
  a {
    font-size: 0.9em !important;
  }
}

h5 {
  font-size: 1em;
}

@media only screen and (max-width: 600px) {
  img {
    display: none;
  }

  h5 {
    font-size: 17px;
  }
}
</style>
