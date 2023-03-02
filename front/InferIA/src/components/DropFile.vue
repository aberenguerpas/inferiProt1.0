<script setup>
    import { ref } from 'vue'
    import { useToastify } from '../composables/toastify'
    
    const { showMessage } = useToastify()
    const file = ref(null)
    const isDragging = ref(false)
    const files = ref([])

    const onChange = () =>{
        if(file.value.files.length > 1){
            showMessage('Only one file at a time')
        }else if(file.value.files.length === 1){
            if(file.value.files[0].type === "text/csv"){
                files.value = file.value.files
            }else{
               showMessage('Only .csv are allowed')
            }
        }
    }


    const dragover = () =>{
        isDragging.value = true
    }


    const dragleave = () =>{
        isDragging.value = false
    }


    const drop = (e) =>{
      file.value.files = e.dataTransfer.files;
      onChange();
      isDragging.value = false;
    }


    const removeFile = () =>{
    files.value = []
    }
</script>

<template>

    <div class="main mt-4">
        <div class="dropzone-container" @dragover.prevent="dragover" @dragleave="dragleave" @drop.prevent="drop">
            <input
            type="file"
            name="file"
            id="fileInput"
            class="hidden-input"
            @change="onChange"
            ref="file"
            accept=".csv"
            >

            <label for="fileInput" class="file-label">
                <div v-if="isDragging"> Release to drop files here.</div>
                <div v-else> Drop files here or <u>click here</u> to upload.</div>
            </label>
            <div class="mt-3 mb-3" v-if="files.length">
                <div v-for="file in files" :key="file.name" class="">
                <p class="file-name">
                {{ file.name }}
                </p>
                <p class="file-name">{{ Math.round(file.size / 1000 ) + "kb" }} <i class="bi bi-x" @click="removeFile()"></i></p>
                </div>
            </div>
            <div v-else  class="mt-3 mt-2">
                <i class="bi bi-filetype-csv"></i>
            </div>

        </div>
    </div>

</template>

<style scoped>

.file-name{
    font-size: 11px;
}

.bi-filetype-csv{
    color: #66666E;
    font-size: 38px;
}

.bi-x{
    cursor: pointer;
    font-size: 15px;
    color: #66666E;
}

.main {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.dropzone-container {
    padding: 1rem;
    background: #f7fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    width: 100%;
    margin: 0 auto;
    height: 120px;
}

.hidden-input {
    opacity: 0;
    overflow: hidden;
    position: absolute;
    width: 1px;
    height: 1px;
}

.file-label {
    font-size: 14px;
    display: block;
    cursor: pointer;
    color: #66666E;
}

</style>