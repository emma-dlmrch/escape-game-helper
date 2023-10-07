<template>
    <nav>
        <router-link to="/signup" v-if="!authenticated">S'inscrire</router-link>
        <router-link to="/login" v-if="!authenticated">Se connecter</router-link>
        <div v-if="authenticated">Se déconnecter<button @click="logout()"> CLICK</button></div>
    </nav>
</template>

<script>

export default {
  name: 'NavBar',
  
  computed: {
    authenticated(){
      return this.$store.state.isAuthenticated
    }
  },

  methods:{
      logout(){
        this.$store.commit('removeToken')
  }
    }

}
</script>