<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <router-link to="/manage/login" class="navbar-brand" v-if="!authenticated">Escape Game Helper Project</router-link>
    <router-link to="/manage/games" class="navbar-brand" v-if="authenticated">Escape Game Helper Project</router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item" v-if="!authenticated">
        <router-link to="/signup" class="nav-link" >S'inscrire</router-link>
      </li>
      <li class="nav-item" v-if="!authenticated" >
        <router-link to="/login" class="nav-link" >Se connecter</router-link>
      </li>
      <li class="nav-item" v-if="authenticated">
        <router-link to="/games" class="nav-link" >Accueil</router-link>
      </li>
      <li class="nav-item" v-if="authenticated">
        <a class="nav-link" @click="logout()">Se déconnecter</a>
      </li>
      <li class="nav-item" v-if="authenticated">
        <router-link to="/update-account" class="nav-link" >Mon compte</router-link>
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
        this.$store.commit('removeUserId')
        this.$router.push('/login')
    }
}

}
</script>