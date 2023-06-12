<script setup>
import Plotly from "plotly.js-dist-min";
import { onMounted } from "vue";
import dataActividad from '../assets/data_actividad.json'

onMounted(()=> {
    var trace1 = {
  x: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
  y: dataActividad.Comercio,
  name: 'Commerce',
  type: 'bar',
  marker :{
    color: '#3f37c9'
  }
};

var trace2 = {
  x: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
  y: dataActividad.Hostelería,
  name: 'Hostelry',
  type: 'bar',
  marker: {
    color: '#e63946'
  }
};

var data = [trace1, trace2];

var layout = {
  dragmode: 'false',
  barmode: 'stack', 
  yaxis: {fixedrange: true},
  xaxis : {fixedrange: true},
  showlegend: true, 
  legend: {x: 0, y: 1.1, orientation: 'h'},
 
  height: 350,
  margin:{
    l: 40,
    r: 10,
    b: 40,
    t: 10,
  }


};

Plotly.newPlot('chart2', data, layout, {displayModeBar: false,  scrollZoom: false});
})

</script>

<template>

    <div id="chart2" class="w-full">

    </div>
</template>