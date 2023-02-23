<script setup>

const props = defineProps(['data'])
const mediaTypes = []

const addMediaType = () => {
   for (let i = 0; i < props.data.length; i++){
        let type = props.data[i].mediaType
        if(!mediaTypes.includes(type)){
            mediaTypes.push(type)
        }
    } 
}

addMediaType()

const isSizeNull = () =>{
    for (let i = 0; i < props.data.length; i++){
        let ourSize = props.data[i].size.slice(0,4)
        if(ourSize.toLowerCase() === 'null'){
            props.data[i].size = '---'
        }
    }
}

isSizeNull()
 
</script>


<template>
    <div class="accordion w-90 mt-4" id="accordionExample">
        <div class="accordion-item" v-for="(item, index) in mediaTypes" >
        <h2 class="accordion-header" >
        <button class="accordion-button text-capitalize"  data-bs-toggle="collapse"  :data-bs-target="`.ob${index}`" aria-expanded="true">
            {{ item }}
        </button>
        </h2>
        <div  v-for="res in data"  class="w-90 collapse show" :class="`ob${index}`" >
            <div class="card-body p-3 " v-if="res.mediaType === item" >
                <h6 class="card-title">{{ res.name }}</h6>
                <h6 class="card-subtitle mb-1 mt-1 text-muted">Size   {{ res.size }} </h6>
                <a :href="res.downloadUrl" class="btn btn-primary mt-2 rounded-pill" >Download</a>
            </div>
        </div>
        </div>
    </div>
</template>


<style scoped>

.accordion-button:not(.collapsed), .accordion-item:last-of-type .accordion-button.collapsed {
    background-color: #06283d;
    color: white;
}

@media only screen and (max-width: 600px) {
    #accordionExample{
        width: 100%;
    }
}

@media only screen and (min-width: 900px) {
    #accordionExample{
       margin-bottom: 50px;
    }
}

</style>