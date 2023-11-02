<script setup>
import IconEyeOpen from '../components/icons/IconOpenEye.vue'
import IconEyeClosed from '../components/icons/IconClosedEye.vue'


import { ref } from 'vue'

const info = ref(
    {
        email: '',
        password: ''
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

const handlerSubmit = () => {
    console.log(`email is ${info.value.email}`)
    console.log(`password is: ${info.value.password}`)
}



</script>

<template>
    <div class="container p-2 lg:my-5 mx-auto lg:mt-28 mt-28 h-[80vh] flex justify-center items-center min-w-[300px]">
        <div
            class="h-5/6 card  md:w-4/6 w-full px-2 lg:px-0  mx-auto  rounded-md flex flex-col md:flex-row place-items-center ">

            <!--Left-->
            <div
                class="h-full w-3/5 left  bg-gradient-to-r from-cyan-500 to-blue-500 rounded-l-md lg:flex justify-center items-center hidden ">
                <img src="../assets//img//inferia_sin_fondo.png" class="w-[60%] " />

            </div>

            <!--right-->
            <div class="h-full  lg:w-2/5 w-full mt-3 lg:mt-0 flex items-center">
                <div class="mx-auto w-full px-5 lg:px-7">
                    <div class="py-1">
                        <h1 class="font-bold text-2xl text-center">¡Hola!</h1>
                    </div>

                    <div class="py-3">
                        <h4 class="text-xs mt-4">Email</h4>
                        <input v-model="info.email"
                            class="w-full mt-4 p-2 rounded-md border-2 focus-visible:outline-0  focus-visible:border-2 focus-visible:border-[#47b5ff] "
                            placeholder="example@email.com" />

                        
                        <!--password-->
                        <h4 class="text-xs mt-6">Contraseña</h4>
                        <div class=" flex items-center mt-4 border-2 rounded-md focus-within:border-[#47b5ff]">
                            <input type="password" v-model="info.password" ref="passinput"
                                class="w-10/12 p-2 focus-visible:outline-0 rounded-md  " placeholder="**********" />
                            <div class="w-2/12 flex justify-center">

                                <IconEyeOpen v-if="showPassword" @click="togglePassword" />
                                <IconEyeClosed v-else @click="togglePassword" />
                            </div>

                        </div>

                        <h4 class="text-xs mt-3 hover:text-[#47b5ff] transition-all ease-linear delay-75">¿Has olvidado
                            tu contraseña?</h4>

                        <button @click="handlerSubmit"
                            class="mt-6 border-2 w-full p-2 rounded-md bg-[#06283D] text-white hover:text-[#47b5ff] hover:bg-transparent hover:font-medium hover:border-[#47b5ff] transition-all ease-linear delay-75">
                            Iniciar sesión </button>

                        
                        <h4 class="text-xs mt-2 text-center">¿No tienes cuenta? <span class="underline underline-offset-2 text-[#06283D] hover:text-[#47b5ff] transition-all ease-linear delay-75" >Registrate</span></h4>
                    </div>

                </div>

            </div>

            <!--end of outter div ❤-->
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