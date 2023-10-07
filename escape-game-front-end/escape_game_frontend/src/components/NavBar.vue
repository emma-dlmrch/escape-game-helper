<template>
    <nav>
        <router-link to="/signup" v-if="!authenticated">S'inscrire</router-link>
        <router-link to="/login" v-if="!authenticated">Se connecter</router-link>
        <router-link to="/games" v-if="authenticated">Accueil</router-link>
        <div v-if="authenticated"><button @click="logout()">Se déconnecter</button></div>
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
        this.$router.push('/login')
    }
}

}
</script>