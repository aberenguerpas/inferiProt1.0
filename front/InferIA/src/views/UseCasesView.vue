<script setup>

import BreadCrumbs from '../components/BreadCrumbs.vue';
import CardBeautiful from  '../components/CardBeautiful.vue'


</script>

<template>
  <div class="container lg:my-5 lg:mx-auto lg:px-12 lg:mt-32 mt-24">

    <div class="w-full lg:w-8/12 mx-auto">
      <BreadCrumbs :list="['Use Cases']"/>
    </div>
    <div
      class="w-full lg:w-8/12 mx-auto my-3"
    >
      <p class="lg:px-3 text-gray-500 text-sm lg:text-base">
        Descubre el ilimitado poder de los datos e inspírate con nuestros casos de uso. En un mundo donde la información está cobrando importancia, la habilidad de aprovechar los datos de forma efectiva se ha convertido en un factor de éxito crucial en varias industrias y disciplinas.
      </p>
    </div>

    <!--card!-->
    
   <div class="w-full lg:w-8/12 lg:my-10 my-8 mx-auto">
    <CardBeautiful :button="true" title="Bonoconsumo" img_src="../assets/img/bonoimg.jpg" :bono="true" pointer='/useCases/bonoconsumo' 
    description="Actualmente, el bonoconsumo se ha convertido en una estrategia eficaz para promover el crecimiento económico y mejorar la calidad de vida de los habitantes de las ciudades. Es necesario analizar este fenómeno para descubrir su verdadero impacto en la economía de las ciudades."
    />
   </div>
  </div>
</template>

<style scoped>
.container {
  font-family: "Ubuntu", sans-serif;
}

.cardx{
  box-shadow: 0px 5px 15px -4px rgba(0, 0, 0, 0.1);
}
 
</style>
