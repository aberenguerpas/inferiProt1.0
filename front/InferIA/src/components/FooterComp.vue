<script setup></script>

<template>
  <div class="main container-fluid">
    <div class="row content-footer ">
      <div class="col-md-2 col-12 colum-style pt-1">
        <img src="../assets/img/Inferia_negativo.png" height="24" width="145" />
      </div>

      <div class="col-md-2 col-12 colum-style">
        <div class="link-container">
          <h4>Contacto</h4>
        </div>
        <div class="link-container">
          <a href="https://www.inferia.io/contact/">Contact with us </a>
        </div>
        <div class="link-container">
          <a href="https://www.inferia.io/request-data/">Request data</a>
        </div>
        <div class="link-container">
          <a href="https://www.inferia.io/sell-data/">Sell data </a>
        </div>
        <div class="pb-1">
          <p>
            Road San Vicente del Raspeig s/n <br />
            03690 Alicante <br />
            Spain
          </p>
        </div>
      </div>

      <div class="col-md-2 col-12 colum-style">
        <div class="link-container">
          <h4>Legal</h4>
        </div>
        <div class="link-container">
          <a href="https://www.inferia.io/legal-notice/" class="pb-2"
            >Legal Notice</a
          >
        </div>
        <div class="link-container">
          <a href="https://www.inferia.io/privacy-policy-2/">Privacy Policy</a>
        </div>
        <div class="link-container">
          <a href="inferia.io/politica-de-cookies/">Cookies Policy</a>
        </div>
      </div>

      <div class="col-md-3 col-12 colum-style">
        <div class="link-container">
          <h4>Social Networks</h4>
        </div>
        <div class="d-flex">
          <div
            id="linknd"
            class="d-flex justify-content-center align-items-center me-2"
          >
            <a href="https://www.linkedin.com/company/inferia/"
              ><i class="fa-brands fa-linkedin fa-lg" style="color: #ffffff"></i
            ></a>
          </div>
          <div
            id="twitter"
            class="d-flex justify-content-center align-items-center"
          >
            <a href="https://twitter.com/inferia_io"
              ><i class="fa-brands fa-twitter fa-lg" style="color: #ffffff"></i
            ></a>
          </div>
        </div>
      </div>

      <div class="col-md-2 col-12">
        <div class="link-container">
          <h4>With The Support</h4>
        </div>
        <a href="https://pca.ua.es/">
          <img src="../assets/img/pca-300x125.png" width="170"
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
  color: #1c244b;
}

.main {
  background-color: #fafafa;
  max-width: 100%;
  margin-top: 135px;
  height: auto;
}

.main a {
  text-decoration: underline;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

.link-container {
  margin-bottom: 40px;
}

p {
  color: #222222;
  font-size: 17px;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

.content-footer {
  max-width: 1300px;
  margin: 0 auto;
  padding: 40px;
}

img {
  max-width: 100%;
  height: auto;
  vertical-align: bottom;
}

@media only screen and (min-width: 600px) {
  .colum-style {
    margin-right: 20px;
  }
}

@media only screen and (max-width: 600px) {
  .content-footer {
    max-width: 100%;
    margin: 0 auto;
    padding: 40px 0px;
  }

  h4{
    margin-top: 50px;
  }
}
</style>
