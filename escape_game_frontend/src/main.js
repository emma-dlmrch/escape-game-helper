import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import axios from 'axios'
import router from './router'
import "bootstrap/dist/css/bootstrap.css"
import 'treeflex/dist/css/treeflex.css';
import "bootstrap-icons/font/bootstrap-icons.css";
import "bootstrap/dist/js/bootstrap.js"
import "./assets/styles.css";
import config from './settings.js';


axios.defaults.baseURL = config.API_URL;


const app = createApp(App);

app.use(store).use(router).mount('#app')


