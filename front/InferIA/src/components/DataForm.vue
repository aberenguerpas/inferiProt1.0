<template>
    <div class="min-w-[256px] max-w-[500px] w-full">
        <div class="card-body flex flex-col text-center px-8  py-4 border-2 border-gray-100 rounded-md items-center justify-center">
          <i class="bi bi-megaphone " style="font-size: 3em; color:#66666E;"></i>
          <h5 class="font-bold text-sm lg:text-base">¿No encuentras los que necesitas?</h5>
         <p class="text-justify text-gray-400 mt-2 text-xs lg:text-sm">Podemos conseguirtelo, sólo dinos qué necesitas y pronto lo tendás a tu disposición! <strong>Es gratis.</strong></p>
          <a href="https://www.inferia.io/request-data/" class="rounded-full bg-[#06283D] text-white mt-3 py-2 lg:px-8 btn-btn text-sm lg:text-base">Pedir</a>
        </div>
    </div>
</template>


<style scoped>
   
    .card-body{
        box-shadow: 0px 5px 15px -4px rgba(0, 0, 0, 0.1);
    }
   
  
@media only screen and (max-width: 992px) {
    .btn-btn{
        width: 90%;
    }
}

@media only screen and (max-width: 600px) {
    .card{
        margin-bottom: 40px;
    }
}
</style>