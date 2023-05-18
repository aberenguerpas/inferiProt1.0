<script setup>
import { ref } from "vue";
import { useAdvanceSearchStore } from '../store/AdvanceSearch'
import { storeToRefs } from 'pinia'
 
//pinia
const store = useAdvanceSearchStore()
const { makePostRequest } = store

const modal = ref(null);  

const { data, headers, context } = storeToRefs(store)   //data from pinia store "advanceSearch"

const objectToSend = ref({})  //object to make the search

const handleSendForm = () => {   //takes the value of the inputs of the modal and makes the object to make the search
 objectToSend.value['context'] = context.value;
 const headersList = Object.values(headers.value)
 objectToSend.value['headers'] = headersList
  const tabdata = data.value.map(col =>{
    return Object.values(col)
  })
 objectToSend.value['content'] = tabdata
 makePostRequest(objectToSend.value)
  console.log(objectToSend.value)
}



</script>

<template>
  <!-- Button trigger modal -->
  <button
    type="button"
    class="btn btn-primary mt-4"
    data-bs-toggle="modal"
    data-bs-target="#exampleModal"
  >
    Advanced Search
  </button>

  <!-- Modal -->
  <div
    class="modal fade"
    id="exampleModal"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
    ref="modal"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Advanced Search</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="d-flex">
            <h6 class="mx-2 mt-2">Topic</h6>
            <input type="text"
            class="form-control-plaintext special-border mx-2  mb-3 text-center"
            v-model="context"
            placeholder="Esperanza de vida"
            />
          </div>
          <table class="table table-borderless">
            <thead>
              <tr>
                <th scope="col">
                  <input
                    type="text"
                    class="form-control-plaintext special-border text-center"
                    v-model="headers.header1"
                    placeholder="municipio"
                  />
                </th>
                <th scope="col">
                  <input
                    type="text"
                    class="form-control-plaintext special-border text-center"
                    v-model="headers.header2"
                    placeholder="sexo"
                  />
                </th>
                <th scope="col">
                  <input
                    type="text"
                    class="form-control-plaintext special-border text-center"
                    v-model="headers.header3"
                    placeholder="periodo"
                  />
                </th>
                <th scope="col">
                  <input
                    type="text"
                    class="form-control-plaintext special-border text-center"
                    v-model="headers.header4"
                    placeholder="total"
                  />
                </th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row"><input type="text" class="form-control text-center" v-model="data[0].col1_1" placeholder="Alicante"/></th>
                <td><input type="text" class="form-control text-center"   v-model="data[1].col2_1" placeholder="M"/></td>
                <td><input type="text" class="form-control text-center"  v-model="data[2].col3_1" placeholder="2022" /></td>
                <td><input type="text" class="form-control text-center"  v-model="data[3].col4_1" placeholder="5000" /></td>
              </tr>
              <tr>
                <th scope="row"><input type="text" class="form-control text-center"  v-model="data[0].col1_2" placeholder="Valencia"/></th>
                <td><input type="text" class="form-control text-center"  v-model="data[1].col2_2" placeholder="F"/></td>
                <td><input type="text" class="form-control text-center"  v-model="data[2].col3_2" placeholder="2023"/></td>
                <td><input type="text" class="form-control text-center"  v-model="data[3].col4_2" placeholder="5000" /></td>
              </tr>
              <tr>
                <th scope="row"><input type="text" class="form-control text-center"  v-model="data[0].col1_3" placeholder="Madrid"/></th>
                <td><input type="text" class="form-control text-center"  v-model="data[1].col2_3" placeholder="Ambos"/></td>
                <td><input type="text" class="form-control text-center"   v-model="data[2].col3_3" placeholder="2021"/></td>
                <td><input type="text" class="form-control text-center"  v-model="data[3].col4_3" placeholder="4000"/></td>
                
              </tr>
            </tbody>
          </table>
        </div>
        <div class="modal-footer">
        
        
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
            @click="handleSendForm"
          >
            Send 
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.btn-primary {
  width: 100%;
}

.special-border {
  border-bottom-color: #47b5ff;
  border-bottom-width: 2px;
}
</style>
