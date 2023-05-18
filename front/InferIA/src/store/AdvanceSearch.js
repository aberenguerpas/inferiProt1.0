import { defineStore } from "pinia";
import { ref } from "vue";

export const useAdvanceSearchStore = defineStore("advanceSearch", () => {
  //results of the Results view. Contains all results form api response
  const results = ref([]);

  const keywords = ref(""); //keywords from search bar!

  //makes the post request in advance search option
  const makePostRequest = async (data) => {
    //It's for Google Analytics
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ event: "busqueda", searchtext: JSON.stringify(data)});

    results.value = "loading";
    keywords.value = "";
    const url = "http://inferia.io/api/search-table/";
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        body: JSON.stringify(data),
      });
      if (response.ok) {
        const res = await response.json();
        results.value = res;
        console.log("ok", res);
      }
    } catch (error) {
      console.log(error);
    }
  };

  //this is the data that makes the object to send!
  const data = ref([
    { col1_1: "", col1_2: "", col1_3: "" },
    { col2_1: "", col2_2: "", col2_3: "" },
    { col3_1: "", col3_2: "", col3_3: "" },
    { col4_1: "", col4_2: "", col4_3: "" },
  ]);

  const headers = ref({
    header1: "",
    header2: "",
    header3: "",
    header4: "",
  });

  const context = ref("");

  // end of the data to send

  return {
    makePostRequest,
    results,
    data,
    headers,
    context,
    keywords,
  };
});
