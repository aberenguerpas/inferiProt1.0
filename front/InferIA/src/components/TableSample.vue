<script setup>
const props = defineProps(['sample'])
</script>


<template>
    <div v-if="sample" class="table-container " >
        <table class="table table-striped">
            <thead class="text-light py-1">
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
        <p class="description ">Preview is not available.</p>
    </div>

</template>


<style scoped>
.table-container{
    overflow: scroll;
    max-width: 100%;
    border-radius: 8px;
    box-shadow: rgb(99 99 99 / 20%) 0px 2px 8px 0px;
    max-height: 600px;
}


tr.stiky-header {
    position: sticky;
    top: 0;
    z-index: 999;
    background: #06283d;
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