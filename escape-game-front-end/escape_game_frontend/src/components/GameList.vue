<template>
    <div>
      <div v-for="game in games" v-bind:key="game.id">
        <h2>{{ game.name }}</h2>
        <p>{{ game.description }}</p>
        <p><button @click="deleteGame(game.id)">Supprimer ce jeu</button></p>
      </div>
    </div>
  </template>

<script>
import axios from 'axios';

export default {
  name: 'GameList',
  data() {
    return {
      games: [],
    };
  },

  methods: {
    async getData() {
      try {
        const response = await axios.get(
          "game/", {
            headers: {
              'Accept': 'application/json'
            }
          }
        );
        // JSON responses are automatically parsed.
        this.games = response.data;
      } catch (error) {
        console.log(error);
      }
    },

    deleteGame(game_id){
      axios.delete('game/' + game_id + "/")
        .then(response => { 
          console.log(response);
          this.getData();
        },
        (error) => { console.log("Error", error) });

     },

  },

  created() {
    //fetch tasks on page load
    this.getData();
  },
};
</script>