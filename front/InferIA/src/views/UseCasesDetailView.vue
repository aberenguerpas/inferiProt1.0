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
        Currently, the consumer voucher has become an effective strategy to promote economic growth and improve the quality of life of residents in cities.
        This innovative incentive system has gained popularity in various locations due to the numerous benefits it offers both consumers and local businesses.
        At InferIA we have carried out an analysis of the measurement data in the town of <strong>Torrevieja, Alicante.</strong>
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
        <h4 class="text-3xl font-semibold">InferIA analysis</h4>
        <p class="mt-2">
          The analysis carried out in this work highlights different relevant aspects of the consumer voucher campaign.
        </p>
      </div>
    </div>

    <InfoUseCases class="lg:my-24 my-20" />

    <div class="w-full lg:w-8/12 mx-auto lg:mt-20 lg:mb-24 mt-12 mb-12 lg:flex">
      <div
        class="lg:p-6 my-5 lg:my-0 lg:w-5/12 w-full flex flex-col justify-center"
      >
        <h1 class="text-3xl font-semibold">Most active days</h1>
        <p class="mt-2">
          In the commerce sector, a relatively stable consumption is observed from Monday to Saturday, with a slight increase on Fridays. On the other hand, in the hospitality sector, a progressive growth can be seen from Monday to Friday, reaching its highest point on weekends, especially on Saturdays and Sundays.
        </p>
      </div>
      <div class="lg:w-7/12 mx-auto border-gray-100 rounded-lg mr-4">
        <Chart2 />
      </div>
    </div>
    <div class="w-full lg:w-8/12 mx-auto lg:mt-20 lg:mb-24 mt-12">
    <h1 class="text-3xl font-semibold">Activity hours</h1>
        <p class="mt-2">
          Regarding the distribution by sectors, it is observed that at 11:00 a.m. and 7:00 p.m. the use of the consumer voucher predominates in the commercial sector. Residents take advantage of these hours to shop at retail establishments and purchase a variety of products and services. On the other hand, at 3:00 p.m. and 10:00 p.m., the activity is divided between the commercial sector and the hospitality sector. Citizens choose to enjoy gastronomic experiences in restaurants and cafes during these hours.
        </p>
        </div>
    <div class="w-full lg:w-8/12 mx-auto rounded-lg">
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
