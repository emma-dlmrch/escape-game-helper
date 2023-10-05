import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import axios from 'axios';
import router from './router';

//axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';


const app = createApp(App);

app.use(store).use(router, axios).mount('#app')

