<script setup>
import IconEyeOpen from '../components/icons/IconOpenEye.vue'
import IconEyeClosed from '../components/icons/IconClosedEye.vue'
import { onBeforeMount} from 'vue';

import { ref } from 'vue'

const data = ref([])
let usefulData = ref([])

onBeforeMount(()=> {
    getCountries()
    setTimeout(makeListofCountries, 2000)
})



const info = ref(
    {
        email: '',
        password: '',
        name: '',
        phone: '',
        country: 'España'
    }
)

const showPassword = ref(false)
const passinput = ref(null)

const togglePassword = () => {
    showPassword.value = !showPassword.value
    if (passinput.value.type === 'password') {
        passinput.value.type = 'text'
    } else if (passinput.value.type === 'text') {
        passinput.value.type = 'password'
    }
}


const getCountries =  async () => {

    try{
        const res = await fetch('https://restcountries.com/v3.1/all');
        if (res.ok){
            data.value =  await res.json()
            
        
        }
           
    }catch(error){
        console.log(error)
    }
}


const makeListofCountries = () => {
   
   for(let i = 0; i < data.value.length; i++){
        
        const item = data.value[i]['translations']['spa']['common']
        const flag = data.value[i]['flags']['png']
        if(item !== 'España'){
            usefulData.value.push({name: item, image: flag})
        }
       

    }

    usefulData.value.sort((a, b) => {
        if(a.name < b.name){
            return -1
        }
        if(a.name > b.name){
            return 1
        }

        return 0
    })
   
    
}

const handlerSubmit = () => {
    console.log(`email is ${info.value.email}`)
    console.log(`password is: ${info.value.password}`)
    console.log(`name is ${info.value.name} `)
    console.log(`country is: ${info.value.country}`)
    console.log(`phone is: ${info.value.phone}`)

}




</script>


<template>
    <div class="container p-2 lg:my-5 mx-auto lg:mt-28 mt-28 h-[80vh] flex justify-center items-center min-w-[300px] ">
        <div
            class="h-[90%] lg:h-5/6 card  md:w-4/6 w-full px-2 lg:px-0  mx-auto  rounded-md flex flex-col md:flex-row place-items-center ">
            <!--left ❤-->
            <div
                class="h-full w-3/5 left  bg-gradient-to-r from-cyan-500 to-blue-500 rounded-l-md lg:flex justify-center items-center hidden ">
                <img src="../assets//img//inferia_sin_fondo.png" class="w-[60%] " />

            </div>

            <!--right ❤-->
            <div class="h-full lg:w-2/5 w-full mt-3 lg:mt-0 overflow-auto">
                <div class="mx-auto w-full px-5 lg:px-7 py-5">
                    
                    <div class="py-1">
                        <h1 class="font-bold text-2xl text-center">¡Registrate!</h1>
                    </div>
                    
                
                    <div class="py-2">
                        <!--Email 💌-->
                        <h4 class="text-xs mt-3">Email</h4>
                        <input v-model="info.email"
                            class="w-full mt-3 p-2 rounded-md border-2 focus-visible:outline-0  focus-visible:border-2 focus-visible:border-[#47b5ff] "
                            placeholder="example@email.com" />

                        <!--Password-->
                        <h4 class="text-xs mt-5">Contraseña</h4>
                        <div class=" flex items-center mt-3 border-2 rounded-md focus-within:border-[#47b5ff]">
                            <input type="password" v-model="info.password" ref="passinput"
                                class="w-10/12 p-2 focus-visible:outline-0 rounded-md  " placeholder="**********" />
                            <div class="w-2/12 flex justify-center">
                                <IconEyeOpen v-if="showPassword" @click="togglePassword" />
                                <IconEyeClosed v-else @click="togglePassword" />
                            </div>

                        </div>

                        <!--Name-->
                        <h4 class="text-xs mt-5">Nombre</h4>
                        <input 
                            v-model="info.name"
                            class="w-full mt-3 p-2 rounded-md border-2 focus-visible:outline-0  focus-visible:border-2 focus-visible:border-[#47b5ff] "
                            placeholder="Joe Doe" />

                        <!--Telefono-->
                        <h4 class="text-xs mt-5">Telefono</h4>
                        <input 
                            v-model="info.phone"
                            class="w-full mt-3 p-2 rounded-md border-2 focus-visible:outline-0  focus-visible:border-2 focus-visible:border-[#47b5ff] "
                            placeholder="777 777 777" />

                        <h4 class="text-xs mt-5">País</h4>
                        <select v-model="info.country" name="select" class="w-full mt-3 p-2 rounded-md border-2 focus-visible:outline-0  focus-visible:border-2 focus-visible:border-[#47b5ff]">
                            <template v-if="usefulData">
                                <option value="España" selected> España</option>
                                <option v-for="country in usefulData">
                                        {{ country.name }} 
                                </option>
                            </template>
                        </select>

                        <button @click="handlerSubmit"
                            class="mt-6 border-2 w-full p-2 rounded-md bg-[#06283D] text-white hover:text-[#47b5ff] hover:bg-transparent hover:font-medium hover:border-[#47b5ff] transition-all ease-linear delay-75">
                            Registrarse
                         </button>
                    </div>


                </div>
            </div>

        </div>
    </div>
</template>



<style scoped>
.card {
    box-shadow: 0 5px 15px rgba(0, 0, 0, 15%);
}



.left {
    background-image: url(../assets/img/bg-4.jpg);
    background-size: cover;
    background-repeat: no-repeat;
}

@media screen and (min-width: 1010px) and (max-width: 1280px) {

    .card {
        width: 80%;
    }
}
</style>