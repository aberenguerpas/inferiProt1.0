<script setup>
import { RouterLink } from "vue-router";
import { computed } from 'vue'

const props = defineProps(['data'])


const cutDescription = computed( ()=> {

    if(props.data.description.length >= 60){
        return props.data.description.slice(0,60) + "..."
    }else {
        return props.data.description
    }

})
</script>


<template>
    <router-link :to="`/details/${data.id}`">
        <div class="card">
            <h5 class="mt-2 card-header fw-bolder">{{data['title']}}</h5>
            <div class="card-body">
                <ul class="list-group list-group-horizontal">
                    <li class="list-group-item"><i class="bi bi-file-earmark-ruled"></i> CSV</li>
                    <li class="list-group-item"><i class="bi bi-patch-check"></i> <a :href="data['license']">Licencia</a></li>
                    <li class="list-group-item"><i class="bi bi-cash"></i> Gratis</li>
                    <li class="list-group-item"><i class="bi bi-box"></i> {{data['provider']}} </li>
                </ul>
                
                <p class="mt-2 card-text text-secondary"> {{ cutDescription  }}</p>
            
                
            </div>
        </div>
    </router-link>
  
</template>


<style scoped>
.list-group, .list-group-item{
    border: 0!important;
    margin: 0 !important;
}
    .card{
        margin-top:1em;
        margin-bottom:1em;
        padding: 1em;
        text-align: justify;
        font-size: 17px;
        
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
        text-overflow: ellipsis !important;
        overflow: hidden;
    }

    
    .list-group-item{
        padding-left: 0;
    }

    @media only screen and (max-width: 992px) {
    li, a{
        font-size: .9em!important;
        }
    }
    h5{
        font-size: 1em;
    }

    
    @media only screen and (min-width: 1000px) {
    
        .card{
            width: 45em;
        }
    }
    


</style>