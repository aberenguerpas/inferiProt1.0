<template>
    <div class="min-w-[256px] max-w-[500px] w-full">
        <div class="card-body flex flex-col text-center px-8  py-8 border-2 border-gray-100 rounded-md items-center justify-center">
          <i class="bi bi-megaphone " style="font-size: 4rem; color:#66666E;"></i>
          <h5 class="font-bold text-lg">Haven't you found what you need?</h5>
         <p class="text-justify text-gray-400 mt-2">We can get what you need, just tell us what is it, and you will have it very soon! <span class="fw-bold">It is free.</span></p>
          <a href="https://www.inferia.io/request-data/" class="rounded-full bg-[#06283D] text-white mt-4 py-2 px-4 btn-btn">Request</a>
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