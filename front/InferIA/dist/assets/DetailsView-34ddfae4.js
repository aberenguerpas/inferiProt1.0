import{_ as I,r as _,x as A,o as l,c as o,a as e,n as F,t as i,u as M,F as b,q as w,m as C,p as j,j as B,l as N,e as y,y as V,b as R}from"./index-a495784e.js";import{B as O}from"./BreadCrumbs-4b794510.js";import{D as G,L as P}from"./LoaderComp-6bdcf582.js";const $=a=>(j("data-v-bb07e7e8"),a=a(),B(),a),q={class:"min-w-[300px] max-w-[500px] cardx p-4 border-2 border-gray-100 rounded-md truncate w-full"},E=$(()=>e("h6",{class:"font-bold mt-3 text-sm"}," Price",-1)),J=$(()=>e("h6",{class:"font-bold mt-3 text-sm"},"License",-1)),K=["href"],U=$(()=>e("h6",{class:"font-bold mt-3 text-sm"},"Source",-1)),Y=["href"],H=$(()=>e("h6",{class:"font-bold mt-3 text-sm"}," Issued",-1)),Q={class:"px-2 text-xs pl-2"},W=$(()=>e("h6",{class:"font-bold mt-3 text-sm"},"Last modified",-1)),X={class:"px-2 text-xs pl-2"},Z=$(()=>e("h6",{class:"font-bold mt-3 text-sm"},"Temporal coverage",-1)),ee={class:"px-2 text-xs pl-2"},te=$(()=>e("h6",{class:"font-bold mt-3 text-sm"}," Geographic coverage",-1)),se={key:0,class:"px-2 text-xs pl-2"},le={key:1},oe={class:"px-2"},ae={key:2},ne={key:3,class:"mt-3"},ce={class:"cursor-pointer"},ie={__name:"MoreInfo",props:["data"],setup(a){const s=a,t=_(!0),p=_(!1),m=_("ver más"),d=_(""),r=_(!1),n=_(!1),u=A(()=>{let h=s.data.modified;return h==null?void 0:h.slice(0,16)}),D=A(()=>{var h;return(h=s.data.issued)==null?void 0:h.slice(0,16)}),k=A(()=>{var h,c,f,x;if((h=s.data.temporal)!=null&&h.startDate&&((c=s.temporal)!=null&&c.endDate)){const T=(f=s.data.temporal.startDate)==null?void 0:f.slice(0,16),g=(x=s.data.temporal.endDate)==null?void 0:x.slice(0,16);return T+" - "+g}}),S=()=>{s.data.geo?s.data.geo.length>1&&Array.isArray(s.data.geo)?(p.value=!0,d.value=s.data.geo):Array.isArray(s.data.geo)||(d.value=s.data.geo,p.value=!1,n.value=!0):d.value="---"},v=()=>{m.value==="ver más"?(d.value=s.data.geo,m.value="ver menos",r.value=!0):m.value==="ver menos"&&(S.value=s.data.geo[0],m.value="ver más",r.value=!1)};return S(),(h,c)=>(l(),o("div",q,[E,e("h6",{class:F(["font-semibold green mt-1 text-xs pl-2",{free:t.value,pay:!t.value}])}," Free",2),J,e("a",{href:a.data.license,class:"text-xs pl-2"},i(a.data.license),9,K),U,e("a",{href:`https://${a.data.provider}`,class:"text-xs pl-2"},i(a.data.provider),9,Y),H,e("p",Q,i(M(D)||"---"),1),W,e("p",X,i(M(u)||"---"),1),Z,e("p",ee,i(M(k)||"---"),1),te,r.value?(l(),o("ul",se,[(l(!0),o(b,null,w(d.value,f=>(l(),o("li",null,i(f),1))),256))])):!r.value&&!n.value?(l(),o("ul",le,[e("li",oe,i(d.value[0]),1)])):n.value?(l(),o("p",ae,i(d.value),1)):C("",!0),p.value?(l(),o("div",ne,[e("p",{onClick:v,class:"text-muted text-end"},[e("u",ce,i(m.value),1)])])):C("",!0)]))}},re=I(ie,[["__scopeId","data-v-bb07e7e8"]]);const de={class:"my-3 lg:w-5/6 w-full"},ue={class:"bg-[#06283D] p-3 rounded-lg text-white flex justify-between text-sm"},_e={class:"uppercase"},me=["onClick"],he={class:"border-2 border-gray-100 rounded-lg"},pe={key:0,class:"p-3"},ve={class:"accordion text-sm"},fe={class:"mb-2 mt-1 text-sm"},xe={class:"mt-2 bg-[#06283D] rounded-full p-2"},ge=["href"],ye={__name:"Acordeon",props:["data"],setup(a){const s=a,t=[];(()=>{for(let n=0;n<s.data.length;n++){let u=s.data[n].mediaType;t.includes(u)||t.push(u)}})(),(()=>{for(let n=0;n<s.data.length;n++)s.data[n].size.slice(0,4).toLowerCase()==="null"&&(s.data[n].size="---")})();const d=n=>{console.log(r.value[n].children.length);for(let u=1;u<r.value[n].children.length;u++)r.value[n].children[u].style.display==="none"?r.value[n].children[u].style.display="block":r.value[n].children[u].style.display="none"},r=_([]);return(n,u)=>{const D=N("font-awesome-icon");return l(),o("div",de,[(l(),o(b,null,w(t,(k,S)=>e("div",{class:"accordion-item",ref_for:!0,ref_key:"itemRefs",ref:r},[e("div",ue,[e("h2",_e,i(k),1),e("button",{class:"rounded-md",onClick:v=>d(S)},[y(D,{icon:["fas","caret-down"]})],8,me)]),(l(!0),o(b,null,w(a.data,(v,h)=>(l(),o("div",he,[v.mediaType===k?(l(),o("div",pe,[e("h6",ve,i(v.name),1),e("h6",fe,"Size: "+i(v.size),1),e("button",xe,[e("a",{href:v.downloadUrl,class:"text-white text-sm"},"Download",8,ge)])])):C("",!0)]))),256))],512)),64))])}}},be=I(ye,[["__scopeId","data-v-44d29598"]]);const we=a=>(j("data-v-a19688e8"),a=a(),B(),a),$e={key:0,class:"table-container w-full"},ke={class:"table w-full"},Se={class:"text-white py-1 rounded-lg"},De={class:"stiky-header"},Te={key:1},Ce=we(()=>e("p",{class:"description"},"Preview is not available.",-1)),Ie=[Ce],ze={__name:"TableSample",props:["sample"],setup(a){const s=a;return(t,p)=>a.sample?(l(),o("div",$e,[e("table",ke,[e("thead",Se,[e("tr",De,[(l(!0),o(b,null,w(s.sample.columns,m=>(l(),o("th",null,i(m),1))),256))])]),e("tbody",null,[(l(!0),o(b,null,w(s.sample.data,m=>(l(),o("tr",null,[(l(!0),o(b,null,w(m,d=>(l(),o("td",null,i(d),1))),256))]))),256))])])])):(l(),o("div",Te,Ie))}},Ae=I(ze,[["__scopeId","data-v-a19688e8"]]);const L=a=>(j("data-v-bc1eb026"),a=a(),B(),a),Me={key:0,class:"container lg:my-5 mx-auto lg:px-12 lg:mt-28 mt-24 min-h-screen"},je={class:"bg-white w-full lg:w-10/12 mx-auto"},Be={class:"flex title-img w-full lg:w-10/12 mx-auto"},Le=["src"],Fe={class:"ml-4 w-3/5 lg:w-11/12"},Ne={class:"my-1 break-all truncate font-bold text-base underline decoration-sky-500 underline-offset-4"},Ve={class:"w-full my-5 lg:w-10/12 mx-auto rounded max-h-[500px] table-div text-xs"},Re={class:"w-full my-5 lg:w-10/12 mx-auto lg:flex"},Oe={class:"w-full lg:3/4 lg:mix-w-[40%] lg:mx-3"},Ge=L(()=>e("h5",{class:"mx-auto font-bold text-base text-[#06283D]"},"Description",-1)),Pe={class:"mt-2 leading-6 text-justify"},qe={class:"break-all text-sm"},Ee={key:0},Je={class:"lg:my-5 mt-6"},Ke=L(()=>e("h5",{class:"mx-auto font-bold text-base text-[#06283D]"},"Resources",-1)),Ue={class:"w-full mx-auto"},Ye={class:"my-6 mx-auto w-full flex lg:block items-center justify-center"},He={class:"my-6 mx-auto w-full flex lg:block items-center justify-center"},Qe={key:1,class:"container lg:my-5 my-3 mx-auto lg:px-12 lg:mt-28 mt-28 flex items-center justify-center w-full min-h-screen"},We={__name:"DetailsView",setup(a){const s=V(),t=_({}),p=_(""),m=_(!1),d=_("ver más"),r=_("");_(!0),R(()=>{n()});const n=async()=>{try{const f=await(await fetch(`http://inferia.io/api/details/?id=${s.params.id}`,{headers:{"Content-Type":"application/json","Access-Control-Allow-Origin":"*"}})).json();t.value=f,D(),u(),k(),v(),console.log(t.value)}catch(c){console.log(c)}},u=()=>{const c=[];Array.isArray(t.value.results.theme)||(c.push(t.value.results.theme),t.value.results.theme=c)},D=()=>{const c=_(t.value.results.resources),f=[" bytes"," KB"," MB"," GB"];for(let x=0;x<c.value.length;x++){let T=0,g=c.value[x].size;for(;g>1024;){let z=Math.floor(g/1024);z=z.toString(),T++,g=z}g=g+f[T],c.value[x].size=g}t.value.resources=c.value},k=()=>{t.value.results.description.length>=250?(m.value=!0,r.value=t.value.results.description.slice(0,250)+"..."):r.value=t.value.results.description},S=()=>{d.value==="ver más"?(r.value=t.value.results.description,d.value="ver menos"):(r.value=t.value.results.description.slice(0,250)+"...",d.value="ver más")},v=()=>{if(t.value.results.sample){let c=t.value.results.sample;c=JSON.parse(c),c.columns.length>=2?p.value=c:p.value=null}else p.value=null},h=()=>{console.log("Yes viettt")};return(c,f)=>t.value.results?(l(),o("div",Me,[e("div",je,[y(O,{list:["Search",`${t.value.results.title.slice(0,15)+"..."}`]},null,8,["list"])]),e("div",Be,[e("img",{src:t.value.results.img_portal,width:"50",class:"object-contain rounded-md"},null,8,Le),e("div",Fe,[e("h1",Ne,i(t.value.results.title),1),(l(!0),o(b,null,w(t.value.results.theme,x=>(l(),o("span",{onClick:h,class:"mr-2 text-sm rounded-full bg-gradient-to-r from-cyan-500 to-blue-500 px-4 text-white"},i(x),1))),256))])]),e("div",Ve,[y(Ae,{sample:p.value},null,8,["sample"])]),e("div",Re,[e("div",Oe,[Ge,e("div",Pe,[e("p",qe,i(r.value),1)]),m.value?(l(),o("div",Ee,[e("p",{onClick:S,class:"text-muted text-end cursor-pointer"},[e("u",null,i(d.value),1)])])):C("",!0),e("div",Je,[Ke,y(be,{data:t.value.resources},null,8,["data"])])]),e("div",Ue,[e("div",Ye,[y(re,{data:t.value.results},null,8,["data"])]),e("div",He,[y(G)])])])])):(l(),o("div",Qe,[y(P)]))}},tt=I(We,[["__scopeId","data-v-bc1eb026"]]);export{tt as default};