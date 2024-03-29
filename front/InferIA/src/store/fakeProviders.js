import { defineStore } from "pinia";


export const useFakeProviders = defineStore('useFakeProviders', () => {

    
const providers = {
    'datos.gob.es': {
      name: "datos.gob.es",
      useCase: false,
      img: "https://inferia-files.s3.eu-west-3.amazonaws.com/logos_providers/datos.gob.es.jpeg",
      description: `Datos.gob.es es la plataforma oficial del Gobierno de España para la publicación y acceso a datos abiertos. A través de esta plataforma se ponen a disposición del público una amplia variedad de conjuntos de datos generados por las administraciones públicas españolas. Estos datos abiertos abarcan diferentes áreas, como la economía, el transporte, el medio ambiente, la salud, la educación, entre otras.`,
      url:"https://datos.gob.es/",
      topics:["Institucional", "Open Data", "Federado"],
      n_data:"+ 68.000",
      geo:"España",
      type: "Abierto"
    },

    'INE':{
      name: 'INE',
      useCase: false,
      img: 'https://inferia-files.s3.eu-west-3.amazonaws.com/logos_providers/ine.png',
      description: `
      El Instituto Nacional de Estadística (INE) es el organismo oficial encargado de recopilar, analizar y difundir la información estadística en España. Su principal objetivo es brindar datos confiables y actualizados sobre la realidad demográfica, económica, social y ambiental del país.
El INE realiza numerosas actividades, como la realización de censos de población y vivienda, la elaboración de estadísticas económicas (como el PIB, el empleo, el comercio exterior, entre otras), la elaboración de indicadores sociales (como educación, salud, vivienda), la recopilación de datos, la recopilación de datos del mercado laboral y la publicación de informes y estudios demográficos.`,
      url:"https://www.ine.es/",
      topics:["Institucional", "Open Data", "Estadísticas"],
      n_data:"+ 3.000",
      geo:"España",
      type: "Abierto"
    },
    'Dades Obertes':{
      name: 'Dades Obertes',
      useCase: false,
      img: 'https://inferia-files.s3.eu-west-3.amazonaws.com/logos_providers/dadesObertes.png',
      description:
      `El Portal de Datos Abiertos de la Comunidad Valenciana es una plataforma digital que ofrece acceso a conjuntos de datos abiertos generados por la administración pública de la Comunidad Valenciana. Este portal tiene como objetivo promover la transparencia, la participación ciudadana y la reutilización de la información pública en la región.`,
      url:"https://dadesobertes.gva.es/",
      topics:["Institucional", "Open Data", "Federado"],
      n_data:"+ 1.300",
      geo:"Comunitat Valenciana, España",
      type: "Abierto"
    },
    'AEMET': {
      name: 'AEMET',
      useCase: 'bonoconsumo',
      img: 'https://inferia-files.s3.eu-west-3.amazonaws.com/logos_providers/aemet.png',
      description:
      `La Agencia Estatal de Meteorología (AEMET) es un organismo público español encargado de recopilar y proporcionar información meteorológica y climatológica en todo el territorio español. A través de una red de estaciones y satélites, AEMET realiza previsiones meteorológicas, emite avisos meteorológicos y estudia el clima y las condiciones meteorológicas en España. Su principal objetivo es salvaguardar la seguridad y el bienestar de la población, así como contribuir al desarrollo sostenible del país a través del manejo de la información meteorológica y climática.`,
      url:"https://www.aemet.es/", 
      topics:["Meteorología", "Open Data", "Climatología"],
      n_data:"-----",
      geo:"España",
      type: "Abierto"
    },
    'Open Street Maps':{
      name: 'Open Street Maps',
      useCase: 'bonoconsumo',
      img: 'https://inferia-files.s3.eu-west-3.amazonaws.com/logos_providers/osm.png',
      description: `OpenStreetMap (OSM) es un proyecto colaborativo de código abierto que crea y proporciona datos geoespaciales gratuitos y abiertos. Los usuarios de OSM contribuyen y editan información sobre calles, edificios, carreteras, puntos de interés y otras características geográficas de todo el mundo. Con una licencia abierta, los datos de OSM están disponibles para su descarga y uso en aplicaciones, mapas en línea y servicios de navegación. OSM se ha convertido en una alternativa popular a los mapas comerciales, proporcionando una plataforma comunitaria accesible para crear y actualizar datos geográficos precisos y detallados.`,
      url: "https://www.openstreetmap.org/",
      topics:["Datos espaciales", "Open Data", "GIS"],
      n_data:"-----",
      geo:"Mundial",
      type: "Abierto"
    },
    'APYMECO':{
      name: 'APYMECO',
      useCase: 'bonoconsumo',
      img: 'https://inferia-files.s3.eu-west-3.amazonaws.com/logos_providers/apymeco.png',
      description: `APYMECO es la asociación de pequeños y medianos comerciantes de la ciudad de Torrevieja. Su objetivo es promocionar el valor del comercio local, defender desde la unión los intereses de sus asociados y ser su voz ante las administraciones con el fin de construir un marco de comercio justo, transparente y de calidad.`,
      url:"https://www.apymeco.info/",
      topics:["Bonoconsumo", "Comercio", "Economía"],
      n_data:"-----",
      geo:"Alicante, España",
      type: "Privado"
    },
    'SEPE':{
      name: 'SEPE',
      useCase: 'bonoconsumo',
      img: 'https://inferia-files.s3.eu-west-3.amazonaws.com/logos_providers/sepe.png',
      description: `El Servicio Público de Empleo Estatal (SEPE) es un organismo autónomo adscrito al Ministerio de Trabajo y Economía Social. El SEPE, junto con los Servicios Públicos de Empleo de las Comunidades Autónomas, conforman el Sistema Nacional de Empleo con el fin de contribuir al desarrollo de la política de empleo, gestionar el sistema de protección por desempleo y garantizar la información sobre el mercado de trabajo.`,
      url:"https://www.sepe.es/",
      topics:["Institucional", "Estadístico", "Empleo"],
      n_data:"-----",
      geo:"España",
      type: "Abierto"
    }
  }
    ;
  ;
  ;

  return {
    providers
  }
})