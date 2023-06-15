<script setup></script>

<template>
  <div class="bg-[#06283D] w-full mt-8 lg:mt-0">
    <div class="max-w-screen-xl w-full mx-auto p-10 lg:flex ">
      <div class="lg:w-1/4 w-full">
        <img src="../assets/img/inferia_sin_fondo.png" class="w-32" />
      </div>

      <div class="lg:w-1/4 w-full">
        <h4 class="font-bold mb-9  mt-12 lg:mt-0">Contacto</h4>
        <div class="mb-10"><a href="https://www.inferia.io/contact/">Contact with Us</a></div>
        <div class="mb-10"><a href="https://www.inferia.io/request-data/">Request Data</a></div>
        <div class="mb-10"><a href="https://www.inferia.io/sell-data/"> Sell Data</a></div>
        <p>
          Road San Vicente del <br />
          Raspeig s/n <br />
          03690 Alicante Spain
        </p>
      </div>

      <div class="lg:w-1/4 w-full">
        <h4 class="font-bold mb-9  mt-12 lg:mt-0">Legal</h4>
        <div class="mb-10"><a  href="https://www.inferia.io/legal-notice/">Legal Notice</a></div>
        <div class="mb-10"><a href="https://www.inferia.io/privacy-policy-2/">Privacy Policy</a></div>
        <div class="mb-10"><a href="https://www.inferia.io/politica-de-cookies/">Cookies Policy</a></div>
      </div>

      

      <div class="lg:w-1/4 w-full">
        <h4 class="font-bold mb-9 mt-12 lg:mt-0">With the support</h4>
        <a href="https://pca.ua.es/">
          <img src="../assets/img/Parque Cientifico Alicante-RGB-negativo.png" width="170" class="mb-8"
        /></a>

        <a
          href="https://www.apte.org/aptenisa-programa-de-ideacion-y-aceleracion-de-startups"
        >
          <img src="../assets/img/aptenisa.png" width="170" />
        </a>
      </div>
    </div>
  </div>
</template>

<style scoped>
#linknd {
  background-color: #0d66c2;
}

#twitter {
  background-color: #1da1f2;
}

#twitter,
#linknd {
  border-radius: 50%;
  width: 2.5em;
  height: 2.5em;
  padding: 6px;
}

h4 {
  font-weight: 600 !important;
  font-size: 17px;
  font-family: Poppins;
  color: #fff;
}

a {
  text-decoration: underline;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  color: #47b5ff;
}

a:hover{
  background-color: transparent;
  color: white !important;
}


p {
  color: #fff;
  font-size: 17px;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

</style>
