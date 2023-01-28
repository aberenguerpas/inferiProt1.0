<template>
<nav class="navbar navbar-expand-lg bg-body-tertiary">

    <a class="navbar-brand" href="https://www.inferia.io/"> <img src="../assets/img/Inferia_negativo.png" alt="Logo"></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="https://www.inferia.io/">Inicio</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://www.inferia.io/vende_tus_datos/">Vende tus datos</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://www.inferia.io/nuestra-historia/">Nuestra historia</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://www.inferia.io/contacto/">Contacto</a>
        </li>
        <li class="nav-item">
          <a class="nav-link btn text-light" href="https://www.inferia.io/solicitar_datos">Solicitar datos</a>
        </li>
      </ul>
    </div>

</nav>
</template>

<style scoped>
nav{
  background:#fff;
  height: 100px!important;
  max-width: 1280px!important;
  margin-left: auto;
  margin-right: auto;
  padding-left: 40px;
  padding-right: 40px;

}
#navbarNav{
  
  margin-left: 1em;
  margin-right: 1em;
}
img{
  width: 140px;
}

.nav-item>.btn{
 line-height: 1em!important;
 border-radius: 2em;
 margin-top:1em;
 padding:1em;
 --bs-nav-link-padding-y:0!important;
}
.nav-link.active{
  color: #47b5ff!important;;
}

.nav-link{
  padding-left: 20px!important;
  padding-right: 20px!important;
  line-height: 60px !important;;
  color:#222222;
  font-size:15px;
}

.navbar-collapse{
  padding: 1em;
  z-index: 10;
  margin:0;
}
@media only screen and (max-width: 992px) {
    #navbarNav{
      margin: 0;
      margin-top:1em;
     
  }
  nav{
    height: auto !important;
    margin-top:1em;
    padding-left: 20px!important;
    padding-right: 20px!important;
  }

  .navbar-collapse{
    background: #fafafa;
    margin: 0;
    padding: 0;
  }
}
</style>