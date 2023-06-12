<script setup>
import { onMounted } from "vue";
import { ref } from "vue";
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";



const open = ref(false);

const toggleModal = () => {
   open.value = !open.value
   if(open.value){
    hbspt.forms.create({
    region: "eu1",
    portalId: "26607839",
    formId: "b511ec5a-358f-4510-ae42-42703e0d92d8",
    target: "#theTarget",
  });
   }
}

 

</script>

<template>  

  <div class="w-full  flex items-center justify-center lg:my-16 my-14">
    <button class="bg-[#06283D] rounded-full text-white mx-auto px-8 py-4 text-lg" @click="toggleModal"> Download Full Reports </button>
  </div>
 
  <TransitionRoot as="template" :show="open">
    <Dialog as="div" class="relative z-10" @close="open = false">
      <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0" enter-to="opacity-100" leave="ease-in duration-200" leave-from="opacity-100" leave-to="opacity-0">
        <div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
      </TransitionChild>

      <div class="fixed inset-0 z-10 overflow-y-auto">
        <div class="flex min-h-full items-center justify-center p-4 text-center sm:items-center sm:p-0">
          <TransitionChild as="template" enter="ease-out duration-300" enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95" enter-to="opacity-100 translate-y-0 sm:scale-100" leave="ease-in duration-200" leave-from="opacity-100 translate-y-0 sm:scale-100" leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95">
            <DialogPanel class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
              <div class="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4">
                <div class="flex items-center justify-center mx-auto w-full">
                 
                  <div class=" text-center py-5 sm:mt-0 w-10/12 mx-auto">
                    <DialogTitle as="h3" class="text-xl font-semibold leading-6 text-[#06283D] py-2">Download Full Report</DialogTitle>
                    <div class=" w-full" id="theTarget" v-once>
                      
                    </div>
                  </div>
                </div>
              </div>
            
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>


</template>
