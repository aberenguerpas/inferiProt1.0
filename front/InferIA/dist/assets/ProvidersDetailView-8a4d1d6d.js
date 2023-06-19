import{_ as f,y as p,l as x,o as a,c,a as t,e as r,u as e,t as i,F as h,q as y,g as d,m,p as v,j as g,z as b}from"./index-a495784e.js";import{B as w}from"./BreadCrumbs-4b794510.js";import{C as j}from"./CardBeautiful-4bd44937.js";import{u as k}from"./fakeProviders-2e485e17.js";const C=n=>(v("data-v-88272dd6"),n=n(),g(),n),B={class:"container lg:my-5 lg:mx-auto lg:px-12 lg:mt-32 mt-24"},V={class:"w-full lg:w-8/12 mx-auto"},P={class:"w-full lg:w-8/12 mx-auto my-6"},D={class:"flex items-start"},I=["src"],S={class:"flex flex-col mb-3 ml-3"},q={class:"text-left font-semibold mb-1 underline underline-offset-8 decoration-pink-500"},N=["href"],z={class:"flex flex-wrap"},F={class:"m-0.5 text-xs lg:text-base lg:my-0 rounded-full bg-gradient-to-r from-cyan-500 to-blue-500 px-4 py-0.5 text-white"},E={class:"text-sm lg:text-base text-gray-500"},R={class:"mx-auto my-6 flex flex-wrap"},A={class:"mx-auto flex flex-col justify-center items-center"},L={class:"flex justify-center items-center"},O={class:"m-3 text-center text-sm"},T={class:"mx-auto flex flex-col justify-center items-center"},U={class:"flex justify-center items-center"},W={class:"m-3 text-center text-sm"},$={class:"mx-auto flex flex-col justify-center items-center"},G={class:"flex justify-center items-center"},H={class:"m-3 text-center text-sm"},J={key:0,class:"min-w-[256px] max-w-[500px] w-full"},K=b('<div class="card-body flex flex-col text-center px-8 py-8 border-2 border-gray-100 rounded-md items-center justify-center" data-v-88272dd6><i class="bi bi-megaphone" style="font-size:2rem;color:#66666E;" data-v-88272dd6></i><h5 class="font-bold text-base" data-v-88272dd6>Are you interested in the data of this provider or similar?</h5><p class="text-justify text-sm text-gray-400 mt-2" data-v-88272dd6>We can get what you need, just tell us what is it, and you will have it very soon! <span class="fw-bold" data-v-88272dd6>It is free.</span></p><a href="https://www.inferia.io/request-data/" class="rounded-full bg-[#06283D] text-white mt-4 py-2 px-4 btn-btn" data-v-88272dd6>Request</a></div>',1),M=[K],Q={key:1,class:"w-full lg:my-20 my-14 mx-auto"},X=C(()=>t("h1",{class:"text-left text-base font-semibold my-3 underline underline-offset-8 decoration-orange-500"}," Use Cases ",-1)),Y={__name:"ProvidersDetailView",setup(n){const _=k(),{providers:o}=_,s=p().params.name;return(ee,te)=>{const l=x("font-awesome-icon");return a(),c("div",B,[t("div",V,[r(w,{list:["Providers",`${e(s)}`]},null,8,["list"])]),t("div",P,[t("div",D,[t("img",{class:"rounded-lg w-2/12",src:e(o)[e(s)].img},null,8,I),t("div",S,[t("h1",q,i(e(s)),1),t("a",{href:e(o)[e(s)].url},i(e(o)[e(s)].url),9,N),t("div",z,[(a(!0),c(h,null,y(e(o)[e(s)].topics,u=>(a(),c("div",null,[t("span",F,i(u),1)]))),256))])])]),t("p",E,i(e(o)[e(s)].description),1),t("div",R,[t("div",A,[e(o)[e(s)].type=="Open"?(a(),d(l,{key:0,class:"text-xl opacity-25",icon:["fas","lock-open"]})):(a(),d(l,{key:1,class:"text-xl opacity-25",icon:["fas","lock"]})),t("div",L,[t("p",O,i(e(o)[e(s)].type),1)])]),t("div",T,[r(l,{class:"text-xl opacity-25",icon:["fas","earth-americas"]}),t("div",U,[t("p",W,i(e(o)[e(s)].geo),1)])]),t("div",$,[r(l,{class:"text-xl opacity-25",icon:["fas","database"]}),t("div",G,[t("p",H,i(e(o)[e(s)].n_data),1)])])]),e(o)[e(s)].type=="Private"?(a(),c("div",J,M)):m("",!0),e(o)[e(s)].useCase?(a(),c("div",Q,[X,r(j,{title:"Bonoconsumo",pointer:"/useCases/bonoconsumo",img_src:"/src/assets/img/bonoimg.jpg",description:"Currently, the bonoconsumo has become an effective strategy to promote economic growth and improve the quality of life of residents in cities. This phenomenon needs to be analyzed to discover its true impact on the economy of cities."})])):m("",!0)])])}}},ce=f(Y,[["__scopeId","data-v-88272dd6"]]);export{ce as default};