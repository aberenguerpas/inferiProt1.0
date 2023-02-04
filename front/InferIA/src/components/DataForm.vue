<template>
    <div class="card text-center">
        <div class="card-body">
          <img src="../assets/img/docs.svg">
          <h5 class="card-title">¿No encuentras lo que necesitas?</h5>
          <p class="card-text">Te los podemos conseguir, simplemente dinos lo que necesitas y en breve lo tendrás. Es gratis.</p>
          <a href="https://www.inferia.io/solicitar_datos" class="btn btn-primary">Pedir</a>
        </div>
    </div>
</template>

<script>

</script>

<style scoped>
    img{
        width: 100%;
        padding:2em;
    }
    .card{
        margin-top: 1em;
 
    }
    

@media only screen and (max-width: 992px) {

    img{
        width: 60%!important;
    }
    h5{
        font-size: 1em!important;
    }
    a,p{
        font-size: 0.9em!important;
    }

    .btn-primary{
        width: 100%;
    }

    
}
</style>