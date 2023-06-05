<script setup>
import Chart from "../components/Chart.vue";
import BreadCrumbs from "../components/BreadCrumbs.vue";
import ModalForm from "../components/ModalForm.vue";
import InfoUseCases from "../components/InfoUseCases.vue";
import Chart2 from "../components/Chart2.vue";
import ShareButtons from "../components/ShareButtons.vue";
import CardVertical from '../components/CardVertical.vue'
import { useFakeProviders } from "../store/fakeProviders";


const store = useFakeProviders();

const { providers } = store;
</script>

<template>
  <div
    class="container lg:my-5 my-3 lg:mx-auto lg:px-12 lg:mt-32 mt-24 mx-auto min-h-screen"
  >
    <BreadCrumbs :list="['Use Cases', 'Bonoconsumo']" />
    <h1
      class="text-center lg:text-5xl text-4xl font-semibold lg:my-5 lg:py-6 my-3 py-3 underline underline-offset-8 decoration-pink-500"
    >
      Bonoconsumo
    </h1>

    <div class="w-full lg:w-8/12 mx-auto lg:my-14 my-12 lg:flex-col">
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras et eros et
        tortor bibendum efficitur. Mauris mattis euismod diam, eu sollicitudin
        ipsum. Vestibulum id feugiat nunc, sit amet venenatis turpis. Sed
        ultrices molestie metus, euismod auctor metus laoreet pretium. Sed
        scelerisque leo interdum est malesuada, at porttitor nisi rutrum.
        Vestibulum imperdiet tellus faucibus laoreet aliquet. Morbi finibus,
        magna rutrum placerat ultrices, mi est laoreet nulla, at hendrerit ipsum
        mauris congue erat. Vivamus sodales rhoncus consequat. Nam a odio
        tortor.
      </p>

      <ShareButtons />
    </div>

    <div class="w-full lg:w-8/12 mx-auto lg:my-28 my-12 lg:flex">
      <div class="lg:w-6/12 mx-auto">
        <img src="../assets/img/torrevieja_test.jpg" class="object-cover" />
      </div>
      <div
        class="lg:p-6 mt-4 lg:mt-0 lg:w-6/12 w-full flex flex-col justify-center"
      >
        <h4 class="text-3xl font-semibold">Analisis de los datos</h4>
        <p class="mt-2">
          En la actualidad, el bonoconsumo se ha convertido en una estrategia
          efectiva para fomentar el crecimiento económico y mejorar la calidad
          vida.
        </p>
      </div>
    </div>

    <InfoUseCases class="lg:my-24 my-20" />

    <div class="w-full lg:w-8/12 mx-auto lg:mt-20 lg:mb-24 mt-12 mb-12 lg:flex">
      <div
        class="lg:p-6 my-5 lg:my-0 lg:w-5/12 w-full flex flex-col justify-center"
      >
        <h1 class="text-3xl font-semibold">Analisis de los datos</h1>
        <p class="mt-2">
          En la actualidad, el bonoconsumo se ha convertido en una estrategia
          efectiva para fomentar el crecimiento económico y mejorar la calidad
          vida.
        </p>
      </div>
      <div class="lg:w-7/12 mx-auto border-gray-100 rounded-lg mr-4">
        <Chart2 />
      </div>
    </div>

    <div class="w-full lg:w-8/12 mx-auto rounded-lg my-12">
      <Chart />
    </div>

    <ModalForm />

    <div class="w-full lg:w-8/12 mx-auto rounded-lg my-12">
      <h5
        class="text-center lg:text-4xl text-3xl font-semibold lg:my-5 lg:py-6 my-3 py-3 underline underline-offset-8 decoration-pink-500"
      >
        Providers
      </h5>
    </div>

    <div class="w-full lg:w-8/12 mx-auto px-2 my-12 flex flex-container ">
      <template v-for="item in providers" >
        <div v-if="item.useCase" class="cards mx-auto my-3">
          <CardVertical :img_src="item.img" :description="item.description" :title="item.name"  />
        </div>
      </template>
    </div>
  </div>
</template>

<style scoped>
.container {
  font-family: "Ubuntu", sans-serif !important;
}



.flex-container{
  overflow-x: scroll;
  scroll-snap-type: x mandatory;
  overflow-y: hidden;
}

.flex-container::-webkit-scrollbar{
    display: none;
  }

.cards:not(:last-child) {
  margin-right: 14px;
}
</style>
