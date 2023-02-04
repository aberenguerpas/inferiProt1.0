<script setup>
    import {ref, computed} from 'vue'
    import MoreInfo from '../components/MoreInfo.vue'
    import { useRoute } from "vue-router";
    import BreadCrumbs from '../components/BreadCrumbs.vue';
    import LoaderComp from '../components/LoaderComp.vue';
    import ResourcesCard from '../components/Acordeon.vue';
    const route = useRoute()
 
    const info = ref({})
    const getData = async () =>{
        try{
            const res = await fetch(`http://inferia.io/api/details?id=${route.params.id}`)
            const jsonResponse = await res.json()
            console.log(jsonResponse)
            info.value = jsonResponse
            size()
            /*cutSuggestionTitle()*/
            themesFormated()
            cutDescription()
        }catch(error){
            console.log(error)
        }
    }

getData()

    const themesFormated = () => {
        const newTheme = []
        if(!Array.isArray(info.value.results.theme)){
            newTheme.push(info.value.results.theme)
            console.log(newTheme)
        }

        info.value.results.theme = newTheme
        console.log(info.value.results.theme)
    }


    const size =  () =>{
        const data = ref(info.value.results.resources)
        const units = ['bytes', 'KB', 'MB', 'GB']
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

    const isFree = ref(true) 

    //dESCRIPTION Btns 

    const isButtonMore = ref(false)
    const isButtonLess = ref(false)
    const cuttedDescription = ref('')

    const cutDescription = ()=> {
        if( info.value.results.description.length >= 250){
            isButtonMore.value = true
            cuttedDescription.value =  info.value.results.description.slice(0,250) + '...'
        }else{
            cuttedDescription.value = info.value.results.description
        }
    }

    const showAllDes = () =>{
        cuttedDescription.value  =  info.value.results.description
        isButtonMore.value = !isButtonMore
        isButtonLess.value = true
    }

    const showLess = () => {
        cuttedDescription.value =  info.value.results.description.slice(0,250) + '...'
        isButtonMore.value = true
        isButtonLess.value = false

    }

    //End of description toggle btns

    /*
    const price = computed( () => {
        if (info.value.price == 0){
            isFree.value = true
            return 'Gratis'
        }else{
            return info.value.price + ' €'
        }
    })*/
/*
    const datex = computed( ()=> {
        let firstData = info.value.temporal_coverage?.slice(6,16)
        let secondData = info.value.temporal_coverage?.slice(41,52)
       return firstData + ' -' + secondData
    })*/

 

   
    /*
    const cutSuggestionTitle = () => {
        info.value.comb.forEach( (element) => {
           
            if(element.title.length <= 80){
                element.title = element.title
            }else if(element.title.length > 80){
                element.title = element.title.slice(0,80) + '..'
            }
        
        })
    }*/

   const goToTheme = () =>{
    console.log('Yes viettt')  //quitar cuando don alberto me diga que hacer al fer click en el btn de theme
   }

   const cutName = computed( () => {
    if(info.value.results.title.length >= 10){
        return info.value.results.title.slice(0,15) + '...'
    }else{
        return info.value.results.title
    }
   })
 
</script>


<template>
    <div v-if="info.results" class="container mt-0 mb-0" >
        <BreadCrumbs :list="['Búsqueda', `${cutName}`]"/>
        <!--first row-->
        <div class="row f-row ">
            <div class="col-lg-8 col-12 mt-2">
                <h1> {{ info.results.title }} </h1>
                <span @click="goToTheme" class="btn btn-primary text-capitalize" v-for="theme in info.results.theme">{{ theme }}</span>
            </div>
        </div> 

        <div class="row mx-auto">
            <!--start of right and left col-->
            <!-- LEFT COLUMN 80% WIDTH-->
            <div class="col-12 col-lg-9 p-0">
                <!--first row-->
                <div class="row mt-3 pt-4 mx-auto">
                    <div class="col-12 col-lg-10 px-1">

                        <div class="text-light title rounded-pill d-inline-flex"> 
                            <h5 class="mx-auto"> Descripción</h5>
                        </div>

                        <div class="pt-4 description w-100">
                            <p>
                                {{ cuttedDescription }}
                            </p>
                            
                        </div>

                        <div v-if="isButtonMore"> 
                            <p @click="showAllDes" class="text-muted text-end "> <u>Ver más... </u> </p>
                        </div>
                        <div v-if="isButtonLess"> 
                            <p @click="showLess" class="text-muted text-end" ><u>Ver menos </u></p>
                        </div>
                    </div>
                </div>


                <!--2d TABLE-->
                <!--
                <div class="row mt-5">

                    <div class="col">
                        <div class="table-container">
                            <table class="table table-striped border table-hover">
                                <thead>
                                    <tr v-for="sampl in Object.keys(info.sample || {})">
                                        <th>{{ sampl }}</th>
                                    </tr>
                                </thead>
                                <tbody> 
                                    <tr v-for="column in info.sample">
                                        <td v-for="ob in column"> {{ ob }}</td> 
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
                -->
                <!--third-->

                <div class="row mt-3 pt-4 mx-auto ">
                    <div class="col px-1">

                        <div class="text-light title  rounded-pill d-inline-flex rs"> 
                            <h5 class="mx-auto"> Recursos</h5>
                        </div>

                       <div class="d-flex flex-wrap pt-4">
                        <ResourcesCard :data="info.resources"/>
                        </div>
                    </div>
                </div>
            </div>

            <!--RIGHT COL-->
            <div class="col-lg-3 col-12 ">
                
                <div class="row mt-3 pt-4">
                    <div class="col more-info">
                        <h5 class="fw-bold badge border border-light-subtle" :class="{ free: isFree, pay: !isFree}" > Gratis</h5>
                        <MoreInfo :data="info.results"/>
                    </div>
                </div>

                <div class="row mt-3 pt-4 data-form">
                    <div class="col ">
                        <!--dataform -->
                    </div>
                </div>
            </div>
        </div>
        
         <!--suggestion row (now commented because the content is not in the API YET!)-->
         <!--
        <div class="row mt-5 mx-auto px-2">
            <div class="col p-0">

                <div class="text-light title  rounded-pill d-inline-flex rs"> 
                  <h5 class="mx-auto"> Combina</h5>
                 </div>

            </div>
        </div>-->

       
        <!--
        <div class="row pt-4">
            <div class="col-12">
                <div class="d-flex flex-wrap">
                    <div class="card sugg" v-for="sug in info.comb" >
                        <div class="card-title d-flex">
                            <div class="sug-title">
                                <h5>{{  sug.title }}</h5> 
                            </div>
                            
                            <div class="badge bg-light text-dark border border-light-subtle comp">
                                <h6> {{ sug.compatibility }}%</h6>
                            </div>
                            
                        </div>

                        <div class="themes d-flex">
                            <div v-for="obj in sug.theme" class="badge bg-light text-dark border border-light-subtle ms-1">
                                {{ obj }}
                            </div>
                        </div>

                        <div class="description-small p-2">
                            <p> {{ sug.description }}</p>
                        </div>

                        <div class="related d-flex">
                            <div v-for="(col, index) in sug.cols" :key="index"  class="badge bg-light text-dark border border-light-subtle ms-1">
                            
                             {{ Object.keys(col)[0]}} {{ Object.values(col)[0] }}
            
                            </div>
                        </div>
                    
                    </div>
                </div>
            </div>

        </div>-->
       

    </div>

    <div class="container" v-else>
        <LoaderComp/>
    </div>
   
</template>

<style scoped>

p.text-muted.text-end {
    cursor: pointer;
}

.sugg{
    padding: 16px;

}

.sugg h5{
    line-height: 1.2;
}

.comp{
    width: 20%;
    font-weight: bold;
}

h6.badge.bg-light.text-dark {
    font-size: 18px;
    margin: 0 auto;
}

.badge.bg-light.text-dark.border.border-light-subtle.comp {
    height: 30px;
}

a.btn.btn-primary.mt-2.rounded-pill {
    float: right;
}
.sug-title{
    width: 80%;

}

.card-title.d-flex {
    height: 115px;
}


span.btn.btn-primary {
    padding: 3px;
    font-size: 14px;
}

.card{
    width: 20rem;
    margin-bottom: 10px;
}

.theme{
    background-color: #06283d;
    width: 140px;
}


.f-row{
    border-bottom: 2px solid #47b5ff;
    padding-bottom: 26px;
    margin: 0 auto;
}

.free{
    color: green;
}

.pay{
    color: #2C3E50;
    opacity: 0.9;
}

.title{
    background-color: #06283d;
    width: 160px;
    height: 40px;
    display: flex;
    align-items: center;
    padding: 0px;
    margin: 0;
}

p{
    margin-bottom: 0;
    text-align: justify;
}

.rs{
    width: 160px;
    
}

.description{
    line-height: 1.6rem;
    font-size: 17px;
    text-align: justify;
}

.border.border-primary-subtle.plus_info {
    height: auto;
    max-width: 367px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    border-radius: 6px;
    padding: 10px 20px;
    box-shadow: rgb(99 99 99 / 20%) 0px 2px 8px 0px;
}

h1{
    font-size: 20px;
}

.more-info h5, .more-info p{
    opacity: 0.8;
    
}

h6.pt-1.mx-auto {
    padding: 5px 10px;
    margin: 0;
}

.mx-auto{
    margin: 0 auto;
}


table {
	display: table;
}
table tr {
	display: table-cell;
}
table tr td {
	display: block;
}

.table-container{
    overflow-x: auto;
    overflow-y: auto;
    width: 90%;
}

h5{
    font-size: 18px;
}

h5.fw-bold.badge.border.border-light-subtle.free {
    padding: 0.8em;
}

@media only screen and (min-width: 710px){

    .card{
        margin-right: 20px;
    }
    
    .sugg{
        width: 300px;
        margin-bottom:  15px;
    }

    .data-form{
        width: 300px !important;
    }

}


@media only screen and (max-width: 1010px){

.card{
    margin-right: 20px;
    margin-bottom: 5px;
}
}

@media only screen and (max-width: 700px) {
    .col-sm-11.col-lg-8 {
    width: 330px;
    padding: 0 10px;
    }

    .description{
    width: 100%;
    line-height: 1.6rem;
    margin: 0 auto;
    font-size: 17px;
    text-align: left;
    
}

.table-container{
    overflow-x: auto;
    overflow-y: auto;
    width: 100%;
}

.card{
    width: 100%;
    margin: 10px 0;
}
}

.border.border-primary-subtle.plus_info{
    margin: 2rem 0px;
}

h5.fw-bold.badge.border.border-light-subtle.free {
    margin: 0 auto;
}


</style>