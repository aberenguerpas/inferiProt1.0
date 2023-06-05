<script setup>

import BreadCrumbs from '../components/BreadCrumbs.vue';
import CardBeautiful from  '../components/CardBeautiful.vue'


</script>

<template>
  <div class="container lg:my-5 my-3 lg:mx-auto lg:px-12 lg:mt-32 mt-24  min-h-screen">

    <div class="w-full lg:w-8/12 mx-auto">
      <BreadCrumbs :list="['Use Cases']"/>
    </div>
    <h1 class="text-center lg:text-5xl text-4xl font-semibold lg:my-5 lg:py-6 my-3 py-3 underline underline-offset-8 decoration-pink-500">Use Cases</h1>
    <div
      class="w-full lg:w-8/12 mx-auto my-6"
    >
      <p class="lg:px-3 text-gray-500">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla fringilla
        nibh neque, accumsan maximus nunc lobortis rhoncus. Cras feugiat ac eros
        eget rhoncus. Suspendisse rutrum bibendum egestas. Morbi eleifend at
        libero a placerat. Vestibulum tincidunt mi ultricies justo aliquam, at
        gravida tortor fringilla. Cras vitae nisi ut ex interdum ullamcorper id
        in ligula. Suspendisse potenti. Vestibulum ante ipsum primis in faucibus
        orci luctus et ultrices posuere cubilia curae; Duis dictum quam a est
        aliquam bibendum. Vestibulum elementum dui in sapien aliquam bibendum.
        Pellentesque sollicitudin metus quis sem finibus, in blandit tortor
        tempus.
      </p>
    </div>

    <!--card!-->
    
   <div class="w-full lg:w-8/12 lg:my-20 my-14 mx-auto">
    <CardBeautiful :button="true" title="Bonoconsumo" img_src="../assets/img/bonoimg.jpg" :bono="true" pointer='/useCases/bonoconsumo' 
    description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sit amet quam enim. Fusce sodales tincidunt lacinia. Donec nec dapibus libero. Quisque accumsan odio vitae metus aliquet aliquam. Curabitur quis tincidunt ex"
    />
   </div>

     
    <div class="w-full lg:w-8/12 mx-auto border-2 border-gray-100 rounded-lg lg:my-20 my-16 bg-gradient-to-r from-cyan-500 to-blue-500 p-5">
        <p class="text-white text-base px-1 text-center w-full font-light tracking-wide">Coming Soon</p>
        <h5 class="text-white text-4xl px-1 text-center w-full text-bold">More Use Cases</h5>
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
