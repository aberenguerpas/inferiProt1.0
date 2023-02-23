<script setup>
import { RouterLink } from "vue-router";

const props = defineProps(['data'])

</script>


<template>
    <router-link :to="`/details/${data.id}`">
  
    <div class="container card" >
        <div class="row" >
            <div class="col-2 img-col">
                <img src="../assets/img/datos.gob.jpg" class="me-3" height="100" width="100">
            </div>
           <div class="col-lg-10 col-12">
                <div class="card-body">
                    <h5 class="card-title mb-0 fw-bold">{{ data.title }}</h5>
                    <ul class="list-group list-group-horizontal">
                        <li class="list-group-item"><i class="bi bi-file-earmark-ruled"></i> CSV</li>
                        <li class="list-group-item"><i class="bi bi-patch-check"></i> <a :href="data['license']">License</a></li>
                        <li class="list-group-item free"><i class="bi bi-cash"></i> Free</li>
                    </ul>
                    <p class="mt-2 card-text text-secondary"> {{ data.description }}</p>
                </div>
           </div>
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
        text-align: left;
        height: 180px;
        width: 50rem;
        
    }
    .card-title {
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
        background-color: none!important;
    }
    .card-body{
        padding: 0;
        height: auto;
        height: 150px;
    }
    .card-text{
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    img{
        border-radius: 15px;
    }
    
    .list-group-item{
        padding-left: 0;
    }

    @media only screen and (max-width: 992px) {
    li, a{
        font-size: .9em!important;
        }
        
        .card{
            width: 25rem;
        }
    }

    h5{
        font-size: 1em;
    }
   

    
    @media only screen and (max-width: 600px) {

        .card{
            width: 22rem;
        }

        .img-col{
            display: none;
        }

        h5, ul{
            font-size: 17px;
        }
    }
    
</style>