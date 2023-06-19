<script setup>
import {ref, onMounted } from 'vue'

const props = defineProps(["data"]);
const mediaTypes = [];

const addMediaType = () => {
  for (let i = 0; i < props.data.length; i++) {
    let type = props.data[i].mediaType;
    if (!mediaTypes.includes(type)) {
      mediaTypes.push(type);
    }
  }
};

addMediaType();

const isSizeNull = () => {
  for (let i = 0; i < props.data.length; i++) {
    let ourSize = props.data[i].size.slice(0, 4);
    if (ourSize.toLowerCase() === "null") {
      props.data[i].size = "---";
    }
  }
};

isSizeNull();

const toggleContent = (index) => {
    //itemRefs.value[index].children.style.display = 'none'
    console.log(itemRefs.value[index].children.length)
    for(let i = 1; i < itemRefs.value[index].children.length; i++){
        if(itemRefs.value[index].children[i].style.display === 'none'){
            itemRefs.value[index].children[i].style.display = 'block'
        }else{
            itemRefs.value[index].children[i].style.display = 'none'
        }
        
    }
};

const itemRefs = ref([])

</script>

<template>
  <div class="my-3 lg:w-5/6 w-full">
    <div class="accordion-item" v-for="(item, index) in mediaTypes" ref="itemRefs">
      <div class="bg-[#06283D] p-3 rounded-lg text-white flex justify-between text-sm" >
        <h2 class="uppercase">
          {{ item }}
        </h2>
        <button class=" rounded-md" @click="toggleContent(index)">
          <font-awesome-icon :icon="['fas', 'caret-down']" />
        </button>
      </div>

      <div v-for="(res, index) in data" class="border-2 border-gray-100 rounded-lg">
        <div class=" p-3" v-if="res.mediaType === item">
          <h6 class="accordion text-sm">{{ res.name }}</h6>
          <h6 class="mb-2 mt-1 text-sm">Size: {{ res.size }}</h6>
          <button class="mt-2 bg-[#06283D] rounded-full p-2">
            <a :href="res.downloadUrl" class="text-white text-sm">Download</a>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.accordion {
  transition: all 0ms;
}

.rounded-full:hover{
  background-color: white;
  color: #47B5FF;
}
.rounded-full a:hover{
  background-color: transparent;
}
</style>
