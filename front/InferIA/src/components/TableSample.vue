<script setup>
const props = defineProps(['sample'])
</script>


<template>
    <div v-if="sample" class="table-container w-full" >
        <table class="table w-full">
            <thead class="text-white py-1 rounded-lg">
                <tr class="stiky-header">
                <th v-for="item in props.sample.columns" > {{ item }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="it in props.sample.data">
                    <td v-for="i in it">{{ i }}</td>
                </tr>
            </tbody>
        </table>
    </div>

    <div v-else>
        <p class="description ">Vista previa no disponible.</p>
    </div>

</template>


<style scoped>

   
   


tr.stiky-header {
    position: sticky;
    top: 0;
    right: 0;
    left: 0;
    z-index: 9;
    background: #06283d;
    border-radius: 20%;
}

.table>:not(caption)>*>* {
    padding: 0.9rem 0.9rem;
    
}

@media only screen and (max-width: 600px){
    .table-container::-webkit-scrollbar {
    display: none;
    }

    .table-container {
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */
    }

}
</style>