<template>
   <p id="question_chat" v-if="!opened" :class="[closed_q ? 'hidden' :'', !open ? 'hidden': '', 'chatbox-icon-container']">
    <button @click="closed_q = !closed_q">
        <font-awesome-icon icon="fa-solid fa-circle-xmark"/>
    </button>
    <span @click="minimize"> ¿En qué puedo ayudarte?</span>
    </p>
    <div @click="minimize" :class="!open ? 'hidden' :'chatbox-icon-container'">
        <div class="chatbox-icon">
            <img src="../assets/img/inferia_sin_fondo.png" width="70">
        </div>
    </div>
   
    <div :class="open ? 'hidden' : 'chatbox-container' ">
        <div class='container'>
            <img src="../assets/img/Icono.png" width="40" class="absolute z-20 bg-white rounded-full p-2 m-3">
            <h3>Asistente de búsqueda</h3>
            
            <button class="minimize_button" @click="minimize">-</button>
            
            <div id="mbox" class="messageBox">
              <div v-if="!privacy" class="privacy text-center">
                <p>Guardar las conversaciones me sirve para ir mejorando día a día, añadir nuevas funcionalidades y resolver rápidamente tus dudas.</p>
                <span class="text-base">¿Estás de acuerdo?</span><br>
                <span><button class="button_option" @click="accept_privacy">Sí</button>
                  <button class="button_option" @click="minimize">No</button>
                </span>
            </div>
                <div v-for="message in chat">
                    <div :class="message.from == 'user' ? 'messageFromUser' : 'messageFromChatGpt'">
                        <div :class="message.from == 'user' ? 'userMessageWrapper' : 'chatGptMessageWrapper'">
                            <div v-html="message.data" :class="message.from == 'user' ? 'userMessageContent' : 'chatGptMessageContent'">
                             </div>
                        </div>
                    </div>
                </div>
                <div class="flex flex-wrap">
                <div v-for="button in buttons">
                  <button class="button_option" @click="click_button(button)">{{button}} </button>
                </div>
              </div>
            </div>
            <div v-if="privacy" class="inputContainer">
                <input
                    @keyup.enter="send(message)"
                    v-model="message"
                    type="text"
                    class="messageInput"
                    placeholder="¿Cómo te puedo ayudar?"
                />
                <button
                    @click="send(message)"
                    class="askButton"
                >
                <font-awesome-icon icon="fa-solid fa-paper-plane"/>
                </button>
                </div>
        </div>
    </div>
</template>

<script setup>
 import { ref, onMounted } from 'vue';
const chat = ref([{"from":"LLM", "data": "¡Hola! Soy <strong>Infer</strong> 🤖"},
{"from":"LLM", "data": "Estoy aquí para ayudarte a encontra la información qué necesitas"},
{"from":"LLM", "data": "Prueba a pedirme alguna de estas tareas:"}])
const message = ref("")
const open = ref(true)
const closed_q = ref(false)
const opened = ref(false) // Si ha sido abierto, oculatamos el mensajito
const buttons = ref(['Hola','¿Qué es InferIA?','Pedir datos específicos al equipo','Necesito desarrollar un estudio demográfico'])
const privacy = ref(false)
const chat_id = ref()
const request_data_form = ref({})
onMounted(() => {
 
  if (sessionStorage.getItem("privacy")) {
    privacy.value = sessionStorage.getItem("privacy");
  }

  if (sessionStorage.getItem("chat_id")) {
      chat_id.value = sessionStorage.getItem("chat_id")
  }else{
    let id = Date.now()
    chat_id.value = id
    sessionStorage.setItem("chat_id", id);
  }
})

function accept_privacy(){
  privacy.value=true
  sessionStorage.setItem("privacy", true);
}
function minimize(){
    open.value = !open.value
    opened.value = true
}

function click_button(text){
  message.value = text
  send()
}

function send_form_hubspot(){
  fetch("http://localhost:8000/send_chat_form/", {
  method: "POST",
  body: JSON.stringify(request_data_form.value),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
}).then((response) => response.json())
  .then((json) => console.log(json));
}

async function send(){
    if(message.value!=""){
        buttons.value = []
        chat.value.push({"from":"user", "data":message.value})
        
        chat.value.push({"from":"LLM", "data":'<div class="typing"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>'})
        let aux = message.value
        message.value = ""

        setTimeout(() =>{
        let objDiv = document.getElementById("mbox");
     
        objDiv.scrollTop = objDiv.scrollHeight},100)
       
        await fetch("http://localhost:8000/chatbot/",
        {method:'POST',
        body: JSON.stringify({'data': aux,'chat_id': chat_id.value}),
        headers: {"Content-type": "application/json; charset=UTF-8"}}).then(response => response.json())
        .then(json =>{

          if(json['intent'] == 'request-data')
            request_data_form.value = {}

          if(json['intent'] == 'Set-name')
            request_data_form.value['name'] = aux

          if(json['intent'] == 'Set-email')
            request_data_form.value['email'] = aux
          
          if(json['intent'] == 'Set-data')
            request_data_form.value['data'] = aux

          if(json['intent'] == 'Set-freq')
            request_data_form.value['freq'] = aux
          
          if(json['intent'] == 'Set-format'){
            request_data_form.value['format'] = aux
            send_form_hubspot()
          }

          chat.value.pop()
          if(json['type']!='json'){
            chat.value.push({"from":"LLM", "data":json['msj']})
          }else{
            let data = json['msj']
            
            if (typeof data == 'string')
              data = JSON.parse(data)

            chat.value.push({"from":"LLM", "data":data['text']})
            
              if('options' in data){
                let data = JSON.parse(json['msj'])
                data['options'].forEach(option => buttons.value.push(option));
              }
              if('variables' in data){
                chat.value.push({"from":"LLM", "data":"Por cierto😊. Hemos encontrado algunos dataset que quizá te sean de utilidad🔽🔽🔽"})
                data['variables'].forEach(option=> chat.value.push({"from":"LLM", "data":"<a class='link_chat' href='"+option['url']+"' target='_blank'>"+option['title']+"</a>"}));
              }
          }
          setTimeout(() =>{
          let objDiv = document.getElementById("mbox");
          objDiv.scrollTop = objDiv.scrollHeight;}, 100)
        
        })
        .catch(err => console.log('Solicitud fallida', err)); // Capturar errores
    }
}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap');


.privacy{
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: white;
  padding: 2em;
  z-index: 100;
  margin: 0;
}

.userMessageWrapper, .chatGptMessageWrapper{
  max-width: 90%;
  min-width: 30px;
}
.example_response{
  font-style: italic;
  color: #06b6d4!important;
  list-style-type: circle;
  padding-left: 1em;
  font-weight: bold!important;
}

.button_option{
  color:white;
  padding: .5em;
  border-radius: .5em;
  background-color: #818cf8;
  font-weight: bold;
  margin:.25em;
  
}

.button_option:hover{
  background-color:#c7d2fe;
}

.chatbox-icon-container{
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 100000;
}
.chatbox-icon{
    position: relative;
    width: 75px;
    height: 75px;
    text-align: center;

  background-color: #fafafa;
  border-radius: 900px ;
  border-style: solid;
  border-width: 3px;
  border-color: #06b6d4;
  background-color: #06283D;
  
  box-shadow:  0px 50px 100px -20px;
    box-shadow:  0 20px 10px -7px rgba(50, 50, 93, 0.25);
}
#question_chat{
    position:fixed;
    bottom: 36px;
    right: 116px;
    padding: 12px;
    background-color:#06b6d4;
    color:white;
    border-radius: 18px;
    border-bottom-right-radius: 0;
    animation: fade-in 2s ease-in;
}
.close{
    display: none;
}

@keyframes slide {
  from {height: 75px;}
  to {height: 0;}
}

@keyframes fade-in {
  from {opacity: 0;}
  to {height: 100;}
}
.minimize_button{
    position:absolute;
    top:0;
    color: white;
    right:20px;
    font-size: 34px;
    animation: slide 1s ease 3.5s forwards;
}
.chatbox-container {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 1000;
  max-width: 360px;
  max-height: 600px;
  
}

.chatbox-container a{
  text-decoration: underline;
  color: #06b6d4;
}

.container {
  width: 360px;
  height: 600px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  font-family: 'Roboto', sans-serif;
}

h3 {
  font-size: 18px;
  font-weight: 500;
  text-align: center;
  color: white;
  padding: 16px;
  margin: 0;
  background-color: #06283D;
  border-bottom: 1px solid #e7e7e7;
}

.messageBox {
  scroll-behavior: smooth;
  padding: 16px;
  flex-grow: 1;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 4px;
}


.messageFromUser,
.messageFromChatGpt {
  display: flex; }

.messageBox {
  max-height: 500px;
  overflow-y: auto;
  padding: 0 16px;
  border-top: 1px solid #f0f0f0;
  border-bottom: 1px solid #f0f0f0;
  flex-grow: 1;
}


.messageFromUser,
.messageFromChatGpt {
  display: flex;
  
}

.userMessageWrapper,
.chatGptMessageWrapper {
  display: flex;
  flex-direction: column;
}

.userMessageWrapper {
  align-self: flex-end;
}

.chatGptMessageWrapper {
  align-self: flex-start;
}

.userMessageContent,
.chatGptMessageContent {
  /*max-width: 60%;*/
  padding: 8px 12px;
  border-radius: 18px;
  margin-bottom: 2px;
  font-size: 14px;
  line-height: 1.4;
}

.userMessageContent {
  background-color: #3b82f6;
  color: white;
  border-top-right-radius: 0;
}

.chatGptMessageContent {
  background-color: #EDEDED;
  color: #222;
  border-top-left-radius: 0;
}

.userMessageTimestamp,
.chatGptMessageTimestamp {
  font-size: 10px;
  color: #999;
  margin-top: 2px;
}

.userMessageTimestamp {
  align-self: flex-end;
}

.chatGptMessageTimestamp {
  align-self: flex-start;
}

.inputContainer {
  display: flex;
  align-items: center;
  padding: 8px;
  background-color: #f0f0f0;
}

.messageInput {
  flex-grow: 1;
  border: none;
  outline: none;
  padding: 12px;
  font-size: 16px;
  background-color: white;
  border-radius: 24px;
  margin-right: 8px;
}

.askButton {
  background-color: #06283D;
  color: white;
  font-size: 16px;
  padding: 8px 16px;
  border: none;
  outline: none;
  cursor: pointer;
  border-radius: 24px;
  transition: background-color 0.3s ease-in-out;
}

.askButton:hover {
  background-color: #145CB3;
}

@media (max-width: 992px) {
    .container {
        padding: 0;
    }
}


@media (max-width: 480px) {
  .container {
    width: 100%;
    max-width: none;
    border-radius: 0;
  }
}
.chatbox-container {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 1000;
}


.messageBox {
    margin:0;
  padding: 16px;
  flex-grow: 1;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.messageFromUser,
.messageFromChatGpt {
  display: flex;
}

.messageFromChatGpt{
    justify-content: start;
}

.messageFromUser{
    justify-content: end;
}

</style>

<style>


.chatGptMessageContent table tr {
    background-color: white;
    color: gray;
    text-align: left;
}
.chatGptMessageContent table tbody tr {
    border-bottom: 1px solid #dddddd;
}

.chatGptMessageContent table th {
    color: gray;
    font-weight: bold;
}
.chatGptMessageContent table tr:first-child th:first-child {
  border-top-left-radius: 10px;
}
.chatGptMessageContent table tr:first-child th:last-child {
  border-top-right-radius: 10px;
}
.chatGptMessageContent table tr:last-child td:first-child {
  border-bottom-left-radius: 10px;
}
.chatGptMessageContent table tr:last-child td:last-child {
  border-bottom-right-radius: 10px;
}

.chatGptMessageContent table tr:nth-of-type(even) {
    background-color: rgb(248, 246, 255);
}

.chatGptMessageContent table td:first-child, th:first-child {
     border-left: none;
}


.chatGptMessageContent table th, td {
    padding: 12px 15px;
}

.chatGptMessageContent table{
    border-collapse: collapse;
    margin: 25px 0;
    font-size: 0.9em;
    color:gray;
    font-family: sans-serif;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}

.link_chat{
  color:#06b6d4;
  text-decoration: underline;
}

.typing {
  align-items: center;
  display: flex;
  height: 17px;
}
.typing .dot {
  animation: mercuryTypingAnimation 1.8s infinite ease-in-out;
  background-color: #7684db ;
  border-radius: 50%;
  height: 7px;
  margin-right: 4px;
  vertical-align: middle;
  width: 7px;
  display: inline-block;
}
.typing .dot:nth-child(1) {
  animation-delay: 200ms;
}
.typing .dot:nth-child(2) {
  animation-delay: 300ms;
}
.typing .dot:nth-child(3) {
  animation-delay: 400ms;
}
.typing .dot:last-child {
  margin-right: 0;
}

@keyframes mercuryTypingAnimation {
  0% {
    transform: translateY(0px);
    background-color:#96c1ee; 
  }
  28% {
    transform: translateY(-7px);
    background-color:#88a2cc; 
  }
  44% {
    transform: translateY(0px);
    background-color: #7684db; 
  }
}
</style>