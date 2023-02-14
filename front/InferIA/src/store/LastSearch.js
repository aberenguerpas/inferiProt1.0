import  {defineStore } from 'pinia'
import { ref } from 'vue'

export const useLastKeyStore = defineStore('lastKey', ()=>{

    const keywords = ref('')

    return{
        keywords
    }
})