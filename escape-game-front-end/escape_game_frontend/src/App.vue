<template>
    <!-- <NavBar msg="Navbar" /> -->
    <!-- <router-view/> -->
    <router-view />
</template>

<script>
import axios from 'axios';
// import NavBar from './components/manage/NavBar.vue';

export default {
  name: 'App',
  components: {
    // NavBar
  },
  data(){
        return {
        }
    },
  
  computed: {
    authenticated(){
      return this.$store.state.isAuthenticated
    }
  },

  beforeCreate(){
    this.$store.commit('initializeStore')
    const token = this.$store.state.token

    if (token ) {
      axios.defaults.headers.common['Authorization'] = "Bearer " + token.access
    } else {
      delete axios.defaults.headers.common["Authorization"]
    }
  },

  methods:{
      logout(){
        this.$store.commit('removeToken')
  }
    }

}
</script>

<style>

</style>
