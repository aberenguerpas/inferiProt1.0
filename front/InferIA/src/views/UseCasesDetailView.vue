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
  
    <div class="w-full lg:w-8/12 mx-auto lg:my-14 my-4 lg:flex-col text-sm lg:text-base">
      <BreadCrumbs :list="['Use Cases', 'Bonoconsumo']" />
      <h1 class="text-3xl text-center underline decoration-sky-500 m-12">Bonoconsumo</h1>
      <p class="my-4">
        Actualmente, el bonoconsumo se ha convertido en una estrategia eficaz para promover el crecimiento económico y mejorar la calidad de vida de los habitantes de las ciudades. Es necesario analizar este fenómeno para descubrir su verdadero impacto en la economía de las ciudades.
        En InferIA hemos llevado a cabo un análisis de los datos generados en la ciudad de <strong>Torrevieja, Alicante.</strong>
      </p>
      <ShareButtons />
    </div>
    <InfoUseCases class="lg:my-24 my-20"/>
    <div class="w-full lg:w-8/12 mx-auto lg:my-28 my-12 lg:flex">
      <div class="lg:w-6/12 mx-auto">
        <img src="../assets/img/torrevieja_test.jpg" class="object-cover" />
      </div>
      <div
        class="lg:p-6 mt-4 lg:mt-0 lg:w-6/12 w-full flex flex-col justify-center"
      >
        <h4 class="text-xl font-semibold">Potencia la economía</h4>
        <p class="mt-2 text-sm lg:text-base">
          Los emprendedores locales son grandes beneficiarios del bono de consumo, ya que reciben más clientes con recursos adicionales, lo que aumenta sus ventas y estabilidad financiera.
        </p>
      </div>
    </div>

    <div class="w-full lg:w-8/12 mx-auto lg:mt-20 lg:mb-24 mt-12 mb-12 lg:flex">
      <div
        class="lg:p-6 my-5 lg:my-0 lg:w-5/12 w-full flex flex-col justify-center"
      >
        <h1 class="text-xl font-semibold">Dias más activos</h1>
        <p class="mt-2 text-sm lg:text-base">
          En el sector comercio se observa un consumo relativamente estable de lunes a sábado, con un ligero incremento los viernes. Por otro lado, en el sector de la hostelería se aprecia un crecimiento progresivo de lunes a viernes, alcanzando su punto más alto los fines de semana, especialmente los sábados y domingos.
        </p>
      </div>
      <div class="lg:w-7/12 mx-auto border-gray-100 rounded-lg mr-4">
        <Chart2 />
      </div>
    </div>
    <div class="w-full lg:w-8/12 mx-auto lg:mt-20 lg:mb-5 mt-12">
    <h1 class="text-xl font-semibold">Horas de actividad</h1>
        <p class="mt-2 text-sm lg:text-base">
          En cuanto a la distribución por sectores, se observa que a las 11:00 y 19:00 predomina el uso del bono de consumo en el sector comercial. Los residentes aprovechan este horario para comprar en establecimientos minoristas y adquirir una variedad de productos y servicios. Por otro lado, a las 15:00 y a las 22:00 horas, la actividad se reparte entre el sector comercial y el sector hostelero. Los ciudadanos optan por disfrutar de experiencias gastronómicas en restaurantes y cafeterías durante este horario.
        </p>
        </div>
    <div class="w-full lg:w-8/12 mx-auto rounded-lg">
      <Chart />
    </div>

    <ModalForm />

    <div class="w-full lg:w-8/12 mx-auto rounded-lg">
      <h5
        class="text-left lg:text-2xl text-xl font-semibold lg:my-5 lg:py-6  py-3 underline underline-offset-8 decoration-orange-500"
      >
        Proveedores
      </h5>
    </div>
    
    <div class="w-full lg:w-8/12 mx-auto px-2 flex flex-container ">
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
