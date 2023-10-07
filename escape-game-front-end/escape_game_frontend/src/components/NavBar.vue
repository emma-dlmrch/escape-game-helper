<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" v-if="!authenticated" href="/login" >Escape Game Helper Project</a>
    <a class="navbar-brand" v-if="authenticated" href="/games" >Escape Game Helper Project</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item" v-if="!authenticated">
        <a class="nav-link" href="/signup">S'inscrire</a>
      </li>
      <li class="nav-item" v-if="!authenticated" >
        <a class="nav-link" href="/login">Se connecter</a>
      </li>
      <li class="nav-item" v-if="authenticated">
        <a class="nav-link"  href="/games">Accueil</a>
      </li>
      <li class="nav-item" v-if="authenticated">
        <a class="nav-link" @click="logout()">Se déconnecter</a>
      </li>
      <li class="nav-item" v-if="authenticated">
        <a class="nav-link" href="/update-account">Mon compte</a>
      </li>
    </ul>
  </div>
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