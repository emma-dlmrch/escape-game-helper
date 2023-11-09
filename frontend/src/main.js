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
import Vue3Sanitize from "vue-3-sanitize";

axios.defaults.baseURL = config.API_URL;

const defaultOptions = {
    allowedTags: ['a', 'img', 'strong', 'em','h1', 'h2','h3','li','ol','ul','p','br','u', 'src', 'iframe'],
    allowedAttributes: {
      a: [ 'href' ],
      img: [ 'src' ],
      iframe: [ 'src']
    }
};

const app = createApp(App);

app.use(store).use(router)
.use(Vue3Sanitize, defaultOptions)
.mount('#app')


