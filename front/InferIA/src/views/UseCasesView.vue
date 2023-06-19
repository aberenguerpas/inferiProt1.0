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
        Discover the unlimited potential of data and be inspired by the use cases we offer. In an information-driven world, the ability to leverage data effectively has become a critical success factor across many industries and disciplines.
      </p>
    </div>

    <!--card!-->
    
   <div class="w-full lg:w-8/12 lg:my-10 my-8 mx-auto">
    <CardBeautiful :button="true" title="Bonoconsumo" img_src="../assets/img/bonoimg.jpg" :bono="true" pointer='/useCases/bonoconsumo' 
    description="Currently, the bonoconsumo has become an effective strategy to promote economic growth and improve the quality of life of residents in cities. This phenomenon needs to be analyzed to discover its true impact on the economy of cities."
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
