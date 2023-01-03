<script setup>
const props = defineProps({
  data: String
})
</script>

<template>
  <div class="card">
    <p class="m-0">
        <span class="fw-bolder"> {{ data['provider'] }}</span>
        <span class="float-end"> {{ new Date(data['modified']).toLocaleDateString('es-Es')}}</span>
    </p>
  <h5 class="mt-2 card-header fw-bolder">{{data['title']}}</h5>
  <div class="card-body">
    <ul class="list-group list-group-horizontal">
        <li class="list-group-item"><i class="bi bi-file-earmark-ruled"></i> CSV</li>
        <li class="list-group-item"><i class="bi bi-patch-check"></i> <a :href="data['license']">Licencia</a></li>
        <li class="list-group-item"><i class="bi bi-cash"></i> Gratis</li>
    </ul>
    
    <p class="mt-2 card-text text-secondary">{{data['description']}}</p>
    
    <a class="btn btn-info text-white float-end" :href="data['resources'][0]['downloadUrl']">Descargar</a>
   
  </div>
</div>
</template>


<style scoped>
.list-group, .list-group-item{
    border: 0!important;
    margin: 0 !important;
}
    .card{
        margin-top:1em;
        margin-bottom:1em;
        padding: 2em;
        text-align: left;
    }
    .card:hover{
       background-color: #fafafa; 
    }
    .card-header {
        padding:0!important;
        background: none;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        white-space: nowrap!important;
        border: none;

    }
    .card-body{
        padding: 0;
    }
    .card-text{
        max-height: 120px;
        overflow-y: scroll !important;
        text-overflow: ellipsis !important;
    }

    .list-group-item{
        padding-left: 0;
    }


</style>