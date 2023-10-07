<template>
    <h1>Mes jeux</h1>
    <div>
      <div>Bonjour tu es le user numéro {{ userId }}</div>
      <div v-for="game in games" v-bind:key="game.id">
        <h2>{{ game.name }}</h2>
        <p>{{ game.description }}</p>
        <p><button @click="deleteGame(game.id)">Supprimer ce jeu</button></p>
        <p><button @click="modifyGame(game.id)">Modifier ce jeu</button></p>
      </div>
    </div>
    <h2>Créer un nouveau jeu</h2>
    <form @submit.prevent="createNewGame">
        <label for="name">Nom du jeu</label>
        <input name="name" v-model="newGame.name">
        <label for="description">Description du jeu</label>
        <textarea name="description" v-model="newGame.description"></textarea>
        <button type="submit">OK</button>
    </form>
  </template>

<script>
import axios from 'axios';

export default {
  name: 'GameList',
  components: {

  },
  data() {
    return {
      games: [],
      userId: this.$store.state.userId,
      gameTest : null,

      newGame: {
                name: '',
                description: '',
                author: '',
            }

    };
  },

  methods: {

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

    createNewGame() {
      try {
        this.newGame.author = this.$store.state.userId
        axios.post('game/', this.newGame).then((response) => {
          console.log(response)
          this.getData()
        });
      } catch (error) {
          console.error("Error during form submission:", error);
      }
    },
  },

  created() {
    //fetch tasks on page load
    this.getData();
  },
};
</script>