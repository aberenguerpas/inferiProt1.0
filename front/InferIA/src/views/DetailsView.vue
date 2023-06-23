<script setup>
import { ref, onMounted } from "vue";
import MoreInfo from "../components/MoreInfo.vue";
import { useRoute } from "vue-router";
import BreadCrumbs from "../components/BreadCrumbs.vue";
import LoaderComp from "../components/LoaderComp.vue";
import Acordeon from "../components/Acordeon.vue";
import TableSample from "../components/TableSample.vue";
import DataForm from "../components/DataForm.vue";

const route = useRoute();
const info = ref({});
const sampleTable = ref("");
//for the cutted Description
const isButtonMore = ref(false);
const btnTitle = ref("ver más");
const cuttedDescription = ref("");
const isFree = ref(true);

onMounted(() => {
  getData();
});

const getData = async () => {
  try {
    const res = await fetch(
      `http://inferia.io/api/details/?id=${route.params.id}`,
      {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
      }
    );
    const jsonResponse = await res.json();
    info.value = jsonResponse;
    addSizeFormat();
    themesFormated();
    cutDescription();
    getSample();
  } catch (error) {
    console.log(error);
  }
};

const themesFormated = () => {
  const newTheme = [];
  if (!Array.isArray(info.value.results.theme)) {
    newTheme.push(info.value.results.theme);
    info.value.results.theme = newTheme;
  }
};

const addSizeFormat = () => {
  const data = ref(info.value.results.resources);
  const units = [" bytes", " KB", " MB", " GB"];
  for (let i = 0; i < data.value.length; i++) {
    let count = 0;
    let result = data.value[i].size;
    while (result > 1024) {
      let x = Math.floor(result / 1024);
      x = x.toString();
      count++;
      result = x;
    }
    result = result + units[count];
    data.value[i].size = result;
  }
  info.value.resources = data.value;
};

//dESCRIPTION Btns

const cutDescription = () => {
  if (info.value.results.description.length >= 250) {
    isButtonMore.value = true;
    cuttedDescription.value =
      info.value.results.description.slice(0, 250) + "...";
  } else {
    cuttedDescription.value = info.value.results.description;
  }
};

const showMoreOrLess = () => {
  if (btnTitle.value === "ver más") {
    cuttedDescription.value = info.value.results.description;
    btnTitle.value = "ver menos";
  } else {
    cuttedDescription.value =
      info.value.results.description.slice(0, 250) + "...";
    btnTitle.value = "ver más";
  }
};

const getSample = () => {
  if (info.value.results.sample) {
    let sample = info.value.results.sample;
    sample = JSON.parse(sample);
    if (sample.columns.length >= 2) {
      sampleTable.value = sample;
    } else {
      sampleTable.value = null;
    }
  } else {
    sampleTable.value = null;
  }
};

const goToTheme = () => {
  console.log("Yes viettt"); //quitar cuando don alberto me diga que hacer al fer click en el btn de theme
};
</script>

<template>
  <div v-if="info.results" class="container lg:my-5  mx-auto lg:px-12 lg:mt-28 mt-24  min-h-screen">

    <div class="bg-white w-full lg:w-10/12 mx-auto">
      <BreadCrumbs :list="['Search', `${info.results.title.slice(0, 15) + '...'}`]"/>
    </div>
  
    <!--first-->
      <div class="flex title-img w-full lg:w-10/12 mx-auto">
        <img :src="info.results.img_portal" width="50" class="object-contain rounded-md"/>
        <div class="ml-4 w-3/5 lg:w-11/12">
          <h1 class="my-1 break-all truncate font-bold text-base underline decoration-sky-500 underline-offset-4">
            {{ info.results.title }}
          </h1>
          <span
            @click="goToTheme"
            class="mr-2 text-sm rounded-full bg-gradient-to-r from-cyan-500 to-blue-500 px-4 text-white"
            v-for="theme in info.results.theme"
            >{{ theme }}</span
          >
        </div>
      </div>
    

    <!--Second row-->
    <div class="w-full my-5 lg:w-10/12 mx-auto rounded max-h-[500px] table-div text-xs">
      <TableSample :sample="sampleTable" />
    </div>
   
    <!--third-->
    <div class="w-full my-5 lg:w-10/12 mx-auto lg:flex">
        <!--left-->
        <div class="w-full lg:3/4 lg:mix-w-[40%] lg:mx-3">
            <h5 class="mx-auto font-bold text-base text-[#06283D] ">Descripción</h5>
            <div class="mt-2 leading-6 text-justify">
              <p class="break-all text-sm">{{ cuttedDescription }}</p>
            </div>
            <div v-if="isButtonMore">
              <p
                @click="showMoreOrLess"
                class="text-muted text-end cursor-pointer"
              >
                <u>{{ btnTitle }}</u>
              </p>
            </div>
            <div class="lg:my-5 mt-6">
                <h5 class="mx-auto font-bold text-base text-[#06283D]">Recursos</h5>
                <Acordeon :data="info.resources" />
            </div>
        </div>
      <!--RIGHT COL-->
        <div class="w-full mx-auto">
            <div class="my-6 mx-auto w-full flex lg:block items-center justify-center">
                <MoreInfo :data="info.results" />
            </div>
            <div class="my-6 mx-auto w-full flex lg:block items-center justify-center">
                <DataForm />
            </div>
            
        </div>
        </div>
  </div>

  <div class="container lg:my-5 my-3 mx-auto lg:px-12 lg:mt-28 mt-28 flex items-center justify-center w-full  min-h-screen" v-else>
      <LoaderComp />
  </div>
</template>

<style scoped>

.container{
  font-family: 'Ubuntu', sans-serif !important;;
}
.combinable-descr {
  height: 100px;
}

.table-div {
  display: flex;
  overflow: auto;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
  box-shadow: rgb(99 99 99 / 20%) 0px 2px 8px 0px;
}

.table-div::-webkit-scrollbar {
  display: none;
}

.combinable-container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
}


.pay {
  color: #2c3e50;
  opacity: 0.9;
}
@media only screen and (min-width: 900) {
  .combinable-container.px-2 {
    margin-bottom: 39px;
  }
  .col.more-info {
    margin-top: 100px;
  }
}

@media only screen and (max-width: 700px) {
  .description {
    font-size: 17px;
    text-align: left;
  }
  .right-col {
    margin-bottom: 40px;
  }
}
</style>
