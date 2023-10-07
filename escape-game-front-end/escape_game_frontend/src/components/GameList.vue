<template>
    <div>
      <div>Bonjour tu es le user numéro {{ userId }}</div>
      <div v-for="game in games" v-bind:key="game.id">
        <h2>{{ game.name }}</h2>
        <p>{{ game.description }}</p>
        <p><button @click="deleteGame(game.id)">Supprimer ce jeu</button></p>
        <p><button @click="modifyGame(game.id)">Modifier ce jeu</button></p>
      </div>
    </div>
    <div>hello, voici un jeu test {{ gameTest }}</div>
    <GameCreate msg="La liste de jeux"/>
  </template>

<script>
import axios from 'axios';
import GameCreate from './GameCreate.vue';

export default {
  name: 'GameList',
  components: {
    GameCreate
  },
  data() {
    return {
      games: [],
      userId: this.$store.state.userId,
      gameTest : null
    };
  },

  methods: {
    // async getData() {
    //   try {
    //     const response = await axios.get("game/");
    //     // JSON responses are automatically parsed.
    //     this.games = response.data;
    //   } catch (error) {
    //     console.log(error);
    //   }
    // },
    getData(){
      axios.get("game/")
        .then(response => {
          this.games = response.data
        }, (error) => {
          console.log(error)
        })
    },

    deleteGame(gameId){
      axios.delete('game/' + gameId + "/")
        .then(response => { 
          console.log(response);
          this.getData();
        },
        (error) => { console.log("Error", error) });

     },
     
    modifyGame(gameId){
      this.$store.commit('setGameId', gameId)
      this.$router.push('/game-details', {gameId: gameId})

    },

    getGameTest(){
      axios.get("game/1")
        .then(response => {
          this.games = response.data
        }, (error) => {
          console.log(error)
        })
    }

  },

  created() {
    //fetch tasks on page load
    this.getData();
    this.getGameTest();
  },
};
</script>