<template>
  <NavBar msg="Navbar" />
  <div class="manage-div"><router-view /></div>
</template>

<script>
import axios from 'axios';
import NavBar from './NavBar.vue';
import store from '../../store/index';

const createAxiosResponseInterceptor = () => {
  // inspired from https://stackoverflow.com/questions/51646853/automating-access-token-refreshing-via-interceptors-in-axios
  console.log("Is used?")
  const interceptor = axios.interceptors.response.use(
    (response) => response,
    (error) => {
      // Reject promise if usual error
      console.log("error.response.status", error.response.status)
      console.log("error", error)
      if (error.response.status !== 401) {
        return Promise.reject(error);
      }
      axios.interceptors.response.eject(interceptor);
      let token = JSON.parse(localStorage.getItem('token'))

      return axios
        .post("token/refresh/", {
          refresh: token.refresh
        })
        .then((response) => {

          token.access = response.data.access
          store.commit('setToken', token)
          console.log("TOKEN RAFRAICHI DE LA DEUXIEME FACON")
          error.response.config.headers["Authorization"] = "Bearer " + token.access
          // Retry the initial call, but with the updated token in the headers. 
          // Resolves the promise if successful
          return axios(error.response.config);
        })
        .catch((error2) => {
          // Retry failed, clean up and reject the promise
          store.dispatch('logout')
          console.log(error2)
          console.log(typeof error2)
          return Promise.reject(error2);
        })
        .finally(() => createAxiosResponseInterceptor()); // Re-attach the interceptor by running the method
    }
  );
}

export default {
  name: 'ManageApp',
  components: {
    NavBar
  },
  data() {
    return {
    }
  },

  computed: {
    authenticated() {
      return this.$store.state.isAuthenticated
    }
  },

  beforeCreate() {
    this.$store.commit('initializeStore')
    createAxiosResponseInterceptor();

  },
  updated() {
  },

  methods: {
  }

}
</script>
