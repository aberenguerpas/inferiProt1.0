<script setup>
import { useAdvanceSearchStore } from '../store/AdvanceSearch'
import { storeToRefs } from 'pinia'
 
//pinia
const store = useAdvanceSearchStore()
const { results } = storeToRefs(store)

const props = defineProps(['title', 'tag'])

const handleClick = async() =>{
    try{
        results.value = 'loading'
        const response = await fetch(`http://inferia.io/api/tags/?tags=${props.tag}`)
        const res = await response.json()
        console.log(res)
        results.value = res
    }catch(error){
        console.log(error)
    }
}
</script>

<template>
    
    <div class="container card" >
        <div class="row" >
            <div class="col-6 rounded">
                <img src="../assets/img/hackaton_Img.jpg" class="" height="120" width="160">
            </div>
           <div class="col-6 pe-1">
                <div class="p-1 card-text ">
                  <p>Special Event</p>
                  <h1 class="fs-6 fw-bold py-2">{{ props.title }}</h1>
                </div>
                <button class="btn btn-primary" @click="handleClick">Check Now</button>
           </div>
        </div>
  </div>
</template>

<style scoped>

.card{
        margin-top:.5em;
        margin-bottom:.5em;
        padding: 0.5em;
        text-align: left;
        height: 140px; 
        width: 100%;
    }

.card h1{
    color: #7B6868;
}

.card.btn{
    font-size: 15px;
}

.card img {
    border-radius: 9px;
    margin: 0 auto;
    object-fit: contain;
    width: 100%;
}

.card-text{
    height: 5em;
}

@media only screen and (max-width: 600px) {
    .card img{
        height: 8em;
        margin: auto 0;
    }

    .card{
        width: 21rem;
        height: 9.5em;
    }
}

@media only screen and (min-width: 600px) and (max-width: 1000px ){

    .card{
        width: 21rem;
        height: 9.5em;
    }
}
</style>