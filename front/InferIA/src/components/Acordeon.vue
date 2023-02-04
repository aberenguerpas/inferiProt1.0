<script setup>


const props = defineProps(['data'])

console.log(props.data)

const mediaTypes = []

const addMediaType = () => {
   for (let i = 0; i < props.data.length; i++){
        let type = props.data[i].mediaType
        //console.log(props.data[i].mediaType)
        if(mediaTypes.includes(type)){
            console.log('not included')
        }else{
            mediaTypes.push(type)
        }
    } 
    console.log(mediaTypes)
}




addMediaType()

 
</script>


<template>

    <div class="accordion mb-5" id="accordionExample">
        <div class="accordion-item" v-for="(item, index) in mediaTypes" >
        <h2 class="accordion-header" >
        <button class="accordion-button text-capitalize"  data-bs-toggle="collapse"  :data-bs-target="`.ob${index}`" aria-expanded="true">
            {{ item }}
        </button>
        </h2>
        <div  v-for="res in data"  class="accordion-collapse collapse show" :class="`ob${index}`" >
            <div class="card-body p-3 " v-if="res.mediaType === item" >
                <h6 class="card-title">{{ res.name }}</h6>
                <h6 class="card-subtitle mb-1 mt-1 text-muted">{{ res.size }} - {{ res.mediaType }} </h6>
                <a :href="data.downloadUrl" class="btn btn-primary mt-2 rounded-pill">Descargar</a>
            </div>
        </div>

        </div>

    </div>

  
</template>


<style scoped>

#accordionExample{
    width: 90%;
}


#accordion-collapse {
    width: 100%;
}
</style>