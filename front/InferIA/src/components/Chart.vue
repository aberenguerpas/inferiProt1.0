<script setup>
import Plotly from "plotly.js-dist-min";
import { onMounted, ref } from "vue";
import d from "../assets/thedata.json";

onMounted(() => {
  function filter_and_unpack(rows, key, hour, type) {
    return rows
      .filter((row) => row["Hora canje"] == hour && row["Tipo"] == type)
      .map((row) => row[key]);
  }

  var frames = [];
  var slider_steps = [];

  for (var i = 0; i < 24; i++) {
    var z_c = filter_and_unpack(d, "bonos", i, "Comercios");
    var x_c = filter_and_unpack(d, "lat", i, "Comercios");
    var y_c = filter_and_unpack(d, "lon", i, "Comercios");

    var z_h = filter_and_unpack(d, "bonos", i, "Hostelería");
    var x_h = filter_and_unpack(d, "lat", i, "Hostelería");
    var y_h = filter_and_unpack(d, "lon", i, "Hostelería");

    frames[i] = {
      data: [
        { marker: { size: z_c }, lat: x_c, lon: y_c, text: "Commerce" },
        { marker: { size: z_h }, lat: x_h, lon: y_h, text: "Hostelery" },
      ],
      name: i,
    };
    slider_steps.push({
      label: i.toLocaleString("en-US", {
        minimumIntegerDigits: 2,
        useGrouping: false,
      }),
      method: "animate",
      args: [
        [i],
        {
          mode: "immediate",
          transition: { duration: 300 },
          frame: { duration: 300 },
        },
      ],
    });
  }

  var data = [
    {
      type: "scattermapbox",
      mode: "markers",
      lon: frames[0].data[0].lon,
      lat: frames[0].data[0].lat,
      marker: {
        size: frames[0].data[0].marker.size,
        color: "red",
        opacity: 0.5,
        sizeref: (2.0 * Math.max(...frames[0].data[0].marker.size)) / 5 ** 2,
        sizemode: "area",
      },
      text: frames[0].data[0].marker.size,
      name: "Commerce",
    },
    {
      type: "scattermapbox",
      mode: "markers",
      lon: frames[0].data[0].lon,
      lat: frames[0].data[0].lat,
      marker: {
        size: frames[0].data[0].marker.size,
        color: "blue",
        opacity: 0.5,
        sizeref: (2.0 * Math.max(...frames[0].data[0].marker.size)) / 5 ** 2,
        sizemode: "area",
      },
      text: frames[0].data[0].marker.size,
      name: "Hostelry",
    },
  ];

  var layout = {
    
    height: 600,
    mapbox: {
      style: "carto-positron",
      zoom: 12,
      dragmode: false,
      center: {
        lat: 37.990882,
        lon: -0.680912,
      },
      domain: {
        x: [0, 1],
        y: [0, 1],
      },
    },
    margin: {
      r: 0,
      t: 10,
      b: 20,
      l: 20,
      pad: 0,
    },
    showlegend: true,
    legend: {
      bgcolor: "rgba(255, 255, 255, 0.7)",
      x: 0,
    },
    sliders: [
      {
        active: 0,
        steps: slider_steps,
        x: 0,
        len: 1,
        xanchor: "left",
        y: 0,
        yanchor: "top",
        pad: { t: 10, b: 10 },
        transition: {
          duration: 300
        },
      },
    ],
  };

  Plotly.newPlot("head", data, layout, {
    displayModeBar: false,
    scrollZoom: false,
  }).then(function () {
    Plotly.addFrames("head", frames);
  });
});
</script>

<template>
  <div id="head" class="w-full"></div>
</template>
