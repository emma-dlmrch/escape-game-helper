<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <router-link :to="{ name: 'WelcomePage'}" class="navbar-brand" v-if="!authenticated">Escape Game Helper</router-link>
    <router-link :to="{ name: 'WelcomePage'}" class="navbar-brand" v-if="authenticated">Escape Game Helper</router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item" v-if="!authenticated">
        <router-link :to="{ name: 'SignUp'}" class="nav-link"><i class="bi bi-person-add"></i> S'inscrire</router-link>
      </li>
      <li class="nav-item" v-if="!authenticated" >
        <router-link :to="{ name: 'LogIn'}" class="nav-link"><i class="bi bi-lock"></i> Se connecter</router-link>
      </li>
      <li class="nav-item" >
        <router-link :to="{ name: 'GameHomepage'}" class="nav-link"><i class="bi bi-controller"></i> Jouer</router-link>
      </li>
      <li class="nav-item" v-if="authenticated">
        <router-link :to="{ name: 'GameList'}" class="nav-link"><i class="bi bi-tools"></i> Mes jeux</router-link>
      </li>
      <li class="nav-item" v-if="authenticated">
        <a class="nav-link" @click="logout()"><i class="bi bi-door-closed"></i> Se déconnecter</a>
      </li>
      <li class="nav-item" v-if="authenticated">
        <router-link :to="{ name: 'UpdateAccount'}" class="nav-link"><i class="bi bi-person-gear"></i> Mon compte</router-link>
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
        this.$router.push({name :'LogIn'})
    }
}

}
</script>