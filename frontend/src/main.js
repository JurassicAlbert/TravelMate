import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App)
  .use(router) // Użycie routera w aplikacji
  .mount('#app')

