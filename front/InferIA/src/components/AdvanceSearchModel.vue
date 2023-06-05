<script setup>
import { ref } from "vue";
import { useAdvanceSearchStore } from "../store/AdvanceSearch";
import { storeToRefs } from "pinia";
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";

const open = ref(false);
const inputHeaderClass = 'bg-white  border-b-2  border-[#47B5FF]  placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-sky-500 block w-6/12 sm:text-sm focus:ring-1"'
const inputClasses ="bg-white border-2  placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-sky-500 block w-6/12 rounded-md sm:text-sm focus:ring-1";
const toggleModal = () => {
  open.value = !open.value;
};

//pinia
const store = useAdvanceSearchStore();
const { makePostRequest } = store;

const modal = ref(null);

const { data, headers, context } = storeToRefs(store); //data from pinia store "advanceSearch"

const objectToSend = ref({}); //object to make the search

const handleSendForm = () => {
  //takes the value of the inputs of the modal and makes the object to make the search
  objectToSend.value["context"] = context.value;
  const headersList = Object.values(headers.value);
  objectToSend.value["headers"] = headersList;
  const tabdata = data.value.map((col) => {
    return Object.values(col);
  });
  objectToSend.value["content"] = tabdata;
  makePostRequest(objectToSend.value);
  console.log(objectToSend.value);
};
</script>

<template>
  <!-- Button trigger modal -->
  <div class="w-full">
    <button
      @click="toggleModal"
      type="button"
      class="rounded-full bg-[#06283D] text-white py-2 my-6 w-full"
    >
      Advanced Search
    </button>
  </div>

  <TransitionRoot as="template" :show="open">
    <Dialog as="div" class="relative z-10" @close="open = false">
      <TransitionChild
        as="template"
        enter="ease-out duration-300"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="ease-in duration-200"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div
          class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
        />
      </TransitionChild>

      <div class="fixed inset-0 z-10 overflow-y-auto">
        <div
          class="flex min-h-full items-center justify-center p-2 text-center sm:items-center sm:p-0"
        >
          <TransitionChild
            as="template"
            enter="ease-out duration-300"
            enter-from="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            enter-to="opacity-100 translate-y-0 sm:scale-100"
            leave="ease-in duration-200"
            leave-from="opacity-100 translate-y-0 sm:scale-100"
            leave-to="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
          >
            <DialogPanel
              class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg"
            >
              <div class="bg-white px-2 pb-4  sm:p-6 sm:pb-4">
                <div class="flex items-center justify-center mx-auto w-full">
                  <div class="text-center py-5 sm:mt-0 w-10/12 mx-auto">
                    <DialogTitle
                      as="h3"
                      class="text-xl font-semibold leading-6 text-[#06283D] py-2"
                      >Advanced Search</DialogTitle
                    >
                    <div class="w-full">
                      <hr />
                      <div class="flex w-full border-200 my-2 items-center justify-center">
                        <h6 class="text-center w-6/12 font-semibold">Topic</h6>
                        <input
                          type="text"
                          class="mt-1 px-3 py-2 text-center"
                          :class="inputHeaderClass"
                          v-model="context"
                          placeholder="Topic"
                        />
                      </div>
                      <table class="table table-auto">
                        <thead>
                          <tr class="w-full">
                            <th scope="col">
                              <input
                                type="text"
                                class="form-control special-border text-center w-full"
                                :class="inputHeaderClass"
                                v-model="headers.header1"
                                placeholder="header1"
                              />
                            </th>
                            <th scope="col">
                              <input
                                type="text"
                                class="form-control special-border text-center w-full"
                                :class="inputHeaderClass"
                                v-model="headers.header2"
                                placeholder="header2"
                              />
                            </th>
                            <th scope="col">
                              <input
                                type="text"
                                class="form-control special-border text-center w-full"
                                :class="inputHeaderClass"
                                v-model="headers.header3"
                                placeholder="header3"
                              />
                            </th>
                            <th scope="col">
                              <input
                                type="text"
                                class="form-control special-border text-center w-full"
                                :class="inputHeaderClass"
                                v-model="headers.header4"
                                placeholder="header4"
                              />
                            </th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <th scope="row">
                              <input
                                type="text"
                                class="form-control text-center"
                                :class="inputClasses"
                                v-model="data[0].col1_1"
                                placeholder="value1"
                              />
                            </th>
                            <td>
                              <input
                                type="text"
                                class="form-control text-center"
                                :class="inputClasses"
                                v-model="data[1].col2_1"
                                placeholder="value2"
                              />
                            </td>
                            <td>
                              <input
                                type="text"
                                class="form-control text-center"
                                :class="inputClasses"
                                v-model="data[2].col3_1"
                                placeholder="value3"
                              />
                            </td>
                            <td>
                              <input
                                type="text"
                                class="form-control text-center"
                                :class="inputClasses"
                                v-model="data[3].col4_1"
                                placeholder="value4"
                              />
                            </td>
                          </tr>
                          <tr>
                            <th scope="row">
                              <input
                                type="text"
                                class="form-control text-center"
                                :class="inputClasses"
                                v-model="data[0].col1_2"
                                placeholder="value5"
                              />
                            </th>
                            <td>
                              <input
                                type="text"
                                class="form-control text-center"
                                :class="inputClasses"
                                v-model="data[1].col2_2"
                                placeholder="value6"
                              />
                            </td>
                            <td>
                              <input
                                type="text"
                                class="form-control text-center"
                                :class="inputClasses"
                                v-model="data[2].col3_2"
                                placeholder="value7"
                              />
                            </td>
                            <td>
                              <input
                                type="text"
                                class="form-control text-center"
                                :class="inputClasses"
                                v-model="data[3].col4_2"
                                placeholder="value 8"
                              />
                            </td>
                          </tr>
                          <tr>
                            <th scope="row">
                              <input
                                type="text"
                                class="form-control text-center"
                                :class="inputClasses"
                                v-model="data[0].col1_3"
                                placeholder="value 9"
                              />
                            </th>
                            <td>
                              <input
                                type="text"
                                class="form-control text-center"
                                :class="inputClasses"
                                v-model="data[1].col2_3"
                                placeholder="value 10"
                              />
                            </td>
                            <td>
                              <input
                                type="text"
                                class="form-control text-center"
                                :class="inputClasses"
                                v-model="data[2].col3_3"
                                placeholder="value 11"
                              />
                            </td>
                            <td>
                              <input
                                type="text"
                                class="form-control text-center"
                                :class="inputClasses"
                                v-model="data[3].col4_3"
                                placeholder="value 12"
                              />
                            </td>
                          </tr>
                        </tbody>
                      </table>
                      <button
                        type="button"
                        class="rounded-full bg-[#06283D] text-white py-2 w-full mt-6 text-lg"
                        @click="handleSendForm"
                      >
                        Search
                      </button>
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

<style scoped>
.btn-primary {
  width: 100%;
}

div#headlessui-dialog-panel-5 {
  height: 420px;
}

input.form-control.text-center {
  width: 100%;
  padding: 5px 8px;
  margin: 4px 0px;
}
</style>
