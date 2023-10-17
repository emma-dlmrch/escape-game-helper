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

// import VueBlocksTree from 'vue3-blocks-tree';
// import 'vue3-blocks-tree/dist/vue3-blocks-tree.css';

//axios.defaults.withCredentials = true
// axios.defaults.headers.common['Accept'] = "application/json"
// axios.defaults.headers.common['Content-Type'] = "application/json"
axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';
// let defaultoptions = {treeName:'blocks-tree'}


const app = createApp(App);

// app.use(store).use(router).use(VueBlocksTree,defaultoptions).mount('#app')
app.use(store).use(router).mount('#app')

