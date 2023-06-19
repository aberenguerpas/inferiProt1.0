<script setup>
import { ref } from 'vue'
import DropFile from './DropFile.vue';
import { useToastify } from '../composables/toastify'



//este componente era ese de subir un archivo con drag and drop
const { showMessage } = useToastify()

const slider = ref(false)
const listOfFields = ref([])
const currentHeader = ref('')
const currentData = ref('')


const addField = () => {
  listOfFields.value.push({field: currentHeader.value, data: currentData.value})
  showMessage('added')
  currentData.value = ''
  currentHeader.value = ''
}


const deleteField = (index) =>{
  listOfFields.value.splice(index, 1);
  showMessage('deleted')
}

</script>

<template>
   <div class="card">
        <div class="card-body text-center">
          <i class="bi bi-search" style="font-size: 4rem; color:#66666E;"></i> <br>
          <h5 class="card-title fw-bold mt-2">
            Advanced Search
          </h5>
            <label class="switch mt-1">
            <input type="checkbox" checked v-model="slider">
            <span class="slider round"></span>
            </label>
            <div v-if="slider">
             
              <div>
                <input placeholder="header" v-model="currentHeader" class="mt-3">
                <input placeholder="data separated by comas" v-model="currentData" class="mt-3">
                <div class="mt-3 mb-3 d-flex" @click.prevent="addField">
                  <i class="bi bi-plus-circle-fill"></i>
                </div>
               
              </div>

              <div class="divsitos d-flex mt-2 mb-2 flex-wrap">
                <div v-for="(f, index) in listOfFields" class="small-divsi d-flex  justify-content-center align-items-center me-2 mb-1" >
                  <p>{{ f.field }}</p>  
                  <i class="bi bi-x" @click="deleteField(index)"></i>
                </div>
              </div>
            </div>
            <div v-else class="drop mt-1">
             <DropFile/>
            </div>
          <a href="https://www.inferia.io/solicitar_datos" class="btn btn-primary  btn-block mt-2 mb-2">Search</a>
        </div>
    </div>


</template>

<style scoped>

.bi-plus-circle-fill{
  color: #47b5ff;
  font-size: 22px;
}
.small-divsi{
  background-color: rgb(102, 102, 110);
  border-radius: 6px;
  padding: 2px;
  height: 25px;
  width: 70px;
}
.small-divsi p {
  color: #fff;
  width: 40px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 100%;

}
.bi-x{
  color: white;
}

.drop{
  height: 130px;
}
.card{
  height: autopx;
  padding: 0 10px;
}

input{
  margin: 0;
  border: 1px solid #cccccc;
  border-radius: 5px;
  font-size: 14px;
  width: 100%;
  padding: 2px;
}
.switch {
  position: relative;
  display: inline-block;
  width: 45px;
  height: 15px;
}
.switch input { 
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 10px;
  width: 10px;
  left: 5px;
  bottom: 4px;
  top: 2px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #47b5ff;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}


.card{
        margin-top: 1em;
        width: 100%;
    }

    h5{
        color: #66666E;
    }
    
@media only screen and (max-width: 992px) {
    h5{
        font-size: 1em!important;
        
    }
    a, p{
        font-size: 0.9em!important;
    }

    .btn-primary{
        width: 100%;
    }
}


@media only screen and (min-width: 600px) {
    .card{
        margin-bottom: 80px;
    }
}
</style>