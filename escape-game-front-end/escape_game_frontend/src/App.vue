<template>
  <GameList msg="La liste de jeux"/>
  <GameCreate msg="La liste de jeux"/>
</template>

<script>
import GameList from './components/GameList.vue'
import GameCreate from './components/GameCreate.vue';

export default {
  name: 'App',
  components: {
    GameList, GameCreate
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
