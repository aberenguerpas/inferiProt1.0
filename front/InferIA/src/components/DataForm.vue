<template>
    <div class="card">
        <div class="card-body text-center">
            <i class="bi bi-megaphone " style="font-size: 4rem; color:#66666E;"></i>
          <h5 class="card-title fw-bold">Haven't you found what you need?</h5>
          <p class="card-text">We can get what you need, just tell us what is it, and you will have it very soon! <span class="fw-bold">It is free.</span></p>
          <a href="https://www.inferia.io/solicitar_datos" class="btn btn-primary float- mt-2">Request</a>
        </div>
    </div>
</template>


<style scoped>
    .card{
        margin-top: 1em;
        width: 100%;
    }

    h5{
        color: #66666E;
    }
    
@media only screen and (max-width: 992px) {
    h5{
        font-size: 1em!important;
        
    }
    a, p{
        font-size: 0.9em!important;
    }

    .btn-primary{
        width: 100%;
    }
}


@media only screen and (min-width: 600px) {
    .card{
        margin-bottom: 80px;
    }
}
</style>