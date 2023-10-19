import { createApp } from 'vue'
import VueSocials from 'vue-socials';
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import './assets/main.css'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faLockOpen, faLock, faEarthAmerica, faDatabase, faTable, faCaretDown, faChevronLeft, faChevronRight, faPaperPlane, faCircleXmark } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faLockOpen, faLock, faEarthAmerica, faDatabase, faTable, faCaretDown, faChevronLeft, faChevronRight, faPaperPlane, faCircleXmark)

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(VueSocials)
app.use(router)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')

