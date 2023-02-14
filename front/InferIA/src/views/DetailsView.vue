<script setup>
    import { ref, onMounted } from 'vue'
    import MoreInfo from '../components/MoreInfo.vue'
    import { useRoute } from 'vue-router';
    import BreadCrumbs from '../components/BreadCrumbs.vue';
    import LoaderComp from '../components/LoaderComp.vue';
    import Acordeon from '../components/Acordeon.vue';
    import TableSample from '../components/TableSample.vue';
    import DataForm from '../components/DataForm.vue';

    const route = useRoute()
    const info = ref({})
    const sampleTable = ref('')
    //for the cutted Description
    const isButtonMore = ref(false)
    const btnTitle = ref('ver más')
    const cuttedDescription = ref('')
    const isFree = ref(true) 

    onMounted(() => {
        getData()
    })


    const getData = async () =>{
        try{
            const res = await fetch(`http://inferia.io/api/details?id=${route.params.id}`)
            const jsonResponse = await res.json()
            info.value = jsonResponse
            addSizeFormat()
            themesFormated()
            cutDescription()
            getSample()
        }catch(error){
            console.log(error)
        }
    }



    const themesFormated = () => {
        const newTheme = []
        if(!Array.isArray(info.value.results.theme)){
            newTheme.push(info.value.results.theme)
            info.value.results.theme = newTheme
        }
    }


    const addSizeFormat =  () =>{
        const data = ref(info.value.results.resources)
        const units = [' bytes', ' KB', ' MB', ' GB']
        for (let i = 0; i < data.value.length ; i++){
            let count =  0
            let result = data.value[i].size
            while(result > 1024) {
                let x = Math.floor(result / 1024)
                x = x.toString()
                count ++
                result = x
            }
            result = result + units[count]
            data.value[i].size = result
        }
        info.value.resources = data.value
    }

    //dESCRIPTION Btns 

    const cutDescription = ()=> {
        if(info.value.results.description.length >= 250){
            isButtonMore.value = true
            cuttedDescription.value =  info.value.results.description.slice(0,250) + '...'
        }else{
            cuttedDescription.value = info.value.results.description
        }
    }

    const showMoreOrLess = () => {
        if( btnTitle.value ==='ver más'){
            cuttedDescription.value = info.value.results.description
            btnTitle.value = 'ver menos'
        }else{
            cuttedDescription.value =  info.value.results.description.slice(0,250) + '...'
            btnTitle.value = 'ver más'
        }
    }

    const getSample = () =>{
        if(info.value.results.sample){
            let sample = info.value.results.sample
            sample = JSON.parse(sample)
            if(sample.columns.length >= 2){
                sampleTable.value = sample
            }else{
                sampleTable.value= null
            }
        }else{

            sampleTable.value = null
        }
    }


   const goToTheme = () =>{
    console.log('Yes viettt')  //quitar cuando don alberto me diga que hacer al fer click en el btn de theme
   }
 
</script>


<template>
    <div v-if="info.results" class="container " >
        <BreadCrumbs :list="['Búsqueda', `${info.results.title.slice(0,15)+'...'}`]"/>
        <div class="row mt-5" >
            <div class="col-lg-10 col-12 ">
                <div class="d-flex title-img">
                    <img src="../assets/img/datos.gob.jpg" height="100" width="100">
                    <div class="ms-3">
                        <h1 class="mt-1 text-break fw-bold"> {{ info.results.title }} </h1>
                        <span @click="goToTheme" class="btn btn-primary text-capitalize me-2" v-for="theme in info.results.theme">{{ theme }}</span>
                    </div>
                </div>
            </div>
        </div> 

        <!--Second row-->
        <div class="row mt-4 mx-auto">
            <div class="col px-1">
                <TableSample :sample="sampleTable"/> 
            </div>
        </div> 

        <div class="row mx-auto mt-4">
            <div class="col-12 col-lg-9 p-0 ">
                
                <!--first row -->
                <div class="row mt-4 mx-auto">
                    <div class="col-12 col-lg-11 px-1"> <!--I have put col-lg-10 to make all cols 90% in big screens-->
                        <h5 class="mx-auto fw-bold fs-4"> Descripción</h5>
                        <div class="mt-4 description">
                            <p> {{ cuttedDescription }}</p>
                        </div>
                        <div v-if="isButtonMore"> 
                            <p @click="showMoreOrLess"  class="text-muted text-end cursor-pointer"> <u>{{ btnTitle }}</u> </p>
                        </div>
                    </div>
                </div>
                
                <!--third-->
                <div class="row mt-4 mx-auto ">
                    <div class="col-12 col-lg-11  px-1">
                        <h5 class="mx-auto  fw-bold fs-4"> Recursos</h5>
                        <Acordeon :data="info.resources"/>
                    </div>
                </div>

                <!--
                <div class="row mt-4  mx-auto ">
                    <div class="col-12 col-lg-11 px-1">
                        <h5 class="mx-auto fw-bold fs-4"> Productos combinables</h5>
                        <div id="container">
                            <div class="combinable-container px-2">

                                <div class="combinable p-4 mt-4 mb-4">
                                    <div class="d-flex flex-row">
                                        <img src="../assets/img/datos.gob.jpg" height="50"> 
                                        <h6 class="ms-3 fw-bold ">Madrid: Población por municipo y sexo</h6>
                                    </div>
                                
                                    <p class="mt-3 combinable-descr">Tabla de INEbase Madrid: Población por municipios y sexo. Anual. Cifras Oficiales de Población de los Municipios Españoles: Revisión del Padrón Municipal</p>

                                    <div class="d-flex flex-row mt-2">
                                        <p class="w-50 mt-1 fw-bold fs-4 free"> 80%</p>
                                        <h6 class="fw-bold badge border border-light-subtle w-50" :class="{ free: isFree, pay: !isFree}" > Gratis</h6>
                                    </div>
                                </div>

                                <div class="combinable p-4 mt-4 ms-4 mb-4">
                                    <div class="d-flex flex-row">
                                        <img src="../assets/img/datos.gob.jpg" height="50"> 
                                        <h6 class="ms-3 fw-bold ">Calendario de cercanías</h6>
                                    </div>
                                
                                    <p class="mt-3 combinable-descr">Calendario de los servicios de cercanías</p>

                                    <div class="d-flex flex-row mt-2">
                                        <p class="w-50 mt-1 fw-bold fs-4 orange"> 74%</p>
                                        <h6 class="fw-bold badge border border-light-subtle w-50" :class="{ free: isFree, pay: !isFree}" > Gratis</h6>
                                    </div>
                                </div>

                                <div class="combinable p-4 mt-4 ms-4 mb-4">
                                    <div class="d-flex flex-row">
                                        <img src="../assets/img/datos.gob.jpg" height="50"> 
                                        <h6 class="ms-3 fw-bold ">Rutas cercanías</h6>
                                    </div>
                                
                                    <p class="mt-3 combinable-descr">Rutas cercanías</p>

                                    <div class="d-flex flex-row mt-2">
                                        <p class="w-50 mt-1 fw-bold fs-4 orange"> 70%</p>
                                        <h6 class="fw-bold badge border border-light-subtle w-50" :class="{ free: isFree, pay: !isFree}" > Gratis</h6>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div> -->
            </div>

            <!--RIGHT COL-->
            <div class="col-lg-3 col-12 right-col px-1">
                <div class="row mt-4">
                    <div class="col">
                        <MoreInfo :data="info.results"/>
                    </div>
                </div>
                
                <div class="row mt-2">
                    <div class="col">
                        <DataForm/>
                    </div>
                </div> 
            </div>
        </div>
    </div>

    <div class="container text-center " v-else>
        <LoaderComp/>
    </div>
   
</template>

<style scoped>

.combinable-descr{
    height: 100px;
}

#container{
    display: flex;
    overflow: auto;
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */
}

#container::-webkit-scrollbar {
    display: none;
}

.combinable-container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  
}
.combinable{
    box-shadow: rgb(99 99 99 / 20%) 0px 2px 8px 0px;
    border-radius: 8px;
    width: 400px;
    height: 260px;
}
.title-img img{
    box-shadow: rgb(99 99 99 / 20%) 0px 2px 8px 0px;  /*ok*/
}

.pay{
    color: #2C3E50;
    opacity: 0.9;
}
.description{
    line-height: 1.6rem;
    text-align: justify;
}

img{
    border-radius: 15px;
}

h6.fw-bold.badge.border.border-light-subtle.free {
    padding: 0.8em;
    font-size: 17px;
}

@media only screen and (min-width: 900){
    .combinable-container.px-2 {
    margin-bottom: 39px;
    }
    .col.more-info {
    margin-top: 100px;
}
}

@media only screen and (max-width: 700px) {
    .description{
    font-size: 17px;
    text-align: left;
    }
    .right-col{
        margin-bottom: 40px;
    }
}
</style>