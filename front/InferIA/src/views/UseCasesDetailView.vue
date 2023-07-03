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

function move(x){

  let container = document.getElementById('provs');

  container.scrollTo({ left: x, behavior: 'smooth' });
}
</script>

<template>
  <div
    class="container lg:my-5 my-3 lg:mx-auto lg:px-12 lg:mt-32 mt-24 mx-auto min-h-screen"
  >
  
    <div class="w-full lg:w-8/12 mx-auto lg:my-14 my-4 lg:flex-col text-sm lg:text-base">
      <BreadCrumbs :list="['Use Cases', 'Bonoconsumo']" />
      <h1 class="text-base lg:text-2xl text-center underline decoration-sky-500 m-12">La iniciativa <strong>Bono Consumo</strong>: Estrategia efectiva para el crecimiento económico y calidad de vida</h1>
      <h4 class="text-base lg:text-xl font-semibold">Análisis del impacto económico</h4>
      <p class="my-4 text-sm lg:text-base">Para comprender el impacto real de estas herramientas, es crucial realizar un análisis exhaustivo de este fenómeno en la economía de las ciudades. En <strong>InferIA</strong>, hemos llevado a cabo un análisis detallado de los datos generados en la ciudad de <strong>Torrevieja</strong>. Nuestro equipo de expertos ha examinado minuciosamente los datos obtenidos a través del programa <strong>Bono Consumo</strong>, analizando los cambios en los patrones de consumo, identificando los sectores económicos más beneficiados y evaluando el impacto a largo plazo en la economía local.
      </p>
      <h4 class="text-base lg:text-xl font-semibold">Resultados y aplicabilidad</h4>
      <p class="my-4 text-sm lg:text-base">Los resultados obtenidos nos proporcionan una comprensión más clara de cómo el <strong>Bono Consumo</strong> ha contribuido al crecimiento económico de <strong>Torrevieja</strong>, y cómo estas conclusiones pueden aplicarse en otras ciudades. Nuestro objetivo principal es proporcionar una base sólida de información que ayude a las autoridades y a los responsables de la toma de decisiones a diseñar estrategias efectivas de estímulo económico, con el propósito de mejorar la calidad de vida de los vecinos y vecinas de estas ciudades.
      </p>
      <h4 class="text-base lg:text-xl font-semibold">Compromiso de <strong>InferIA</strong></h4>
      <p class="my-4 text-sm lg:text-base">En <strong>InferIA</strong>, estamos comprometidos con la investigación y el análisis de estas iniciativas innovadoras que impulsan el desarrollo económico sostenible. Continuaremos trabajando para proporcionar información valiosa que respalde la toma de decisiones informadas y promueva el bienestar de las comunidades locales.
      </p>
      <h4 class="text-base lg:text-xl font-semibold">Explora nuestra investigación completa</h4>
      <p class="my-4 text-sm lg:text-base">Si estás interesado en conocer más detalles sobre el caso de uso del <strong>Bono Consumo</strong> en <strong>Torrevieja</strong> y cómo puede aplicarse en otras ciudades, te invitamos a explorar nuestra investigación completa en <strong>InferIA</strong>. Obtén una visión detallada de los resultados y descubre cómo esta estrategia puede ayudar a impulsar el crecimiento económico y mejorar la calidad de vida en tu comunidad.
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
        <h4 class="text-base lg:text-xl font-semibold">Potencia la economía</h4>
        <p class="mt-2 text-sm lg:text-base">
          Los emprendedores locales son grandes beneficiarios del bono de consumo, ya que reciben más clientes con recursos adicionales, lo que aumenta sus ventas y estabilidad financiera.
        </p>
      </div>
    </div>

    <div class="w-full lg:w-8/12 mx-auto lg:mt-20 lg:mb-24 mt-12 mb-12 lg:flex">
      <div
        class="lg:p-6 my-5 lg:my-0 lg:w-5/12 w-full flex flex-col justify-center"
      >
        <h1 class="text-base lg:text-xl font-semibold">Dias más activos</h1>
        <p class="mt-2 text-sm lg:text-base">
          En el sector comercio se observa un consumo relativamente estable de lunes a sábado, con un ligero incremento los viernes. Por otro lado, en el sector de la hostelería se aprecia un crecimiento progresivo de lunes a viernes, alcanzando su punto más alto los fines de semana, especialmente los sábados y domingos.
        </p>
      </div>
      <div class="lg:w-7/12 mx-auto border-gray-100 rounded-lg mr-4">
        <Chart2 />
      </div>
    </div>
    <div class="w-full lg:w-8/12 mx-auto lg:mt-20 lg:mb-5 mt-12">
    <h1 class="text-base lg:text-xl font-semibold">Horas de actividad</h1>
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
    <div class="lg:w-8/12 w-full mx-auto">
    <button style="left:-50px" class="w-8 bg-cyan-500 text-white p-2 rounded-full rounded-xl border-2 border-cyan-500 absolute left-0 top-1/2 z-10" @click='move(0)'><font-awesome-icon icon="fa-solid fa-chevron-left"/></button>
      <div id="provs" class="px-2 flex flex-container">
        <scroll-container  v-for="item in providers">
          <scroll-page v-if="item.useCase" class="cards mx-auto m-3">
            <CardVertical :id="item.name" :img_src="item.img" :description="item.description" :title="item.name"  />
          </scroll-page>
        
        </scroll-container>
      </div>
    <button style="right:-40px" class="w-8 bg-cyan-500 text-white p-2 rounded-full rounded-xl border-2 border-cyan-500 absolute top-1/2" @click='move(1000)'><font-awesome-icon icon="fa-solid fa-chevron-right"/></button>
  </div>
  </div>
</template>

<style scoped>

.flex-container{
  overflow-x: scroll;
  scroll-snap-type: x mandatory;
  overflow-y: none;
  scroll-behavior: smooth;
}

.flex-container::-webkit-scrollbar{
    display: none;
  }

.cards:not(:last-child) {
  margin-right: 14px;
}
</style>
