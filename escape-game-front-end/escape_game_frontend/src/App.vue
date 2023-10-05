<template>
  <nav>
    <router-link to="/signup">S'inscrire</router-link>
    <router-link to="/login">Se connecter</router-link>
    <router-view/>
  </nav>
  <GameList msg="La liste de jeux"/>
  <GameCreate msg="La liste de jeux"/>

</template>

<script>
import GameList from './components/GameList.vue'
import GameCreate from './components/GameCreate.vue';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    GameList, GameCreate
  },

  beforeCreate(){
    this.$store.commit('initializeStore')
    const token = this.$store.state.token

    if (token ) {
      axios.defaults.headers.common['Authentication'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authentication'] = ''
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
