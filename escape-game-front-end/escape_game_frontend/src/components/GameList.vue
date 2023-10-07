<template>
  <h1>Tableau de bord</h1>
  <div>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Mes jeux</th>
          <th scope="col">Description</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="game in games" v-bind:key="game.id">
          <th scope="row">{{ game.name }}</th>
          <td>{{ game.description.substring(0, 20) }} ...</td>
          <td><button @click="modifyGame(game.id)" type="button" class="btn btn-dark btn-sm">Gérer</button> <button
              @click="deleteGame(game.id)" type="button" class="btn btn-outline-dark btn-sm">Supprimer</button></td>
        </tr>
        <tr>
          <th><input type ="text" v-model="newGame.name" placeholder="Nouveau jeu" maxlength="50"></th>
          <td><input type ="text" v-model="newGame.description" placeholder="Entre une description" maxlength="50"/></td>
          <td><button @click="createNewGame" type="button" class="btn btn-dark btn-sm">Créer</button></td>
        </tr>
      </tbody>
    </table>
  </div>
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
      gameTest: null,

      newGame: {
        name: '',
        description: '',
        author: '',
      }

    };
  },

  methods: {

    getData() {
      axios.get("game/")
        .then(response => {
          this.games = response.data
        }, (error) => {
          console.log(error)
        })
    },

    deleteGame(gameId) {
      axios.delete('game/' + gameId + "/")
        .then(response => {
          console.log(response);
          this.getData();
        },
          (error) => { console.log("Error", error) });

    },

    modifyGame(gameId) {
      this.$store.commit('setGameId', gameId)
      this.$router.push('/game-details', { gameId: gameId })

    },

    createNewGame() {
      try {
        if (this.newGame.name.length <1) {this.newGame.name = 'Jeu sans nom'}
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