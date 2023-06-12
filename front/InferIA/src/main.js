import { createApp } from 'vue'
import VueSocials from 'vue-socials';
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import './assets/main.css'





const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(VueSocials)
app.use(router)
app.mount('#app')

