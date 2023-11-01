<template>
  <h1>Tableau de bord</h1>
  <div class="table-responsive">
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">Jeux</th>
          <th scope="col">Description</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="game in games" v-bind:key="game.id">
          <th scope="row"><i class="bi bi-puzzle"></i> {{ game.name }}</th>
          <td><i class="bi bi-book"></i> {{ game.description.substring(0, 20) }} ...</td>
          <td><button @click="modifyGame(game.id)" type="button" class="btn btn-dark btn-sm"><i class="bi bi-pencil"></i>
              Gérer</button>&nbsp;
            <button @click="deleteGame(game.id)" type="button" class="btn btn-outline-dark btn-sm"><i
                class="bi bi-trash"></i> Supprimer</button>
          </td>
        </tr>
        <tr>
          <th><input class="form-control small-input" type="text" v-model="newGame.name" placeholder="Nouveau jeu"
              maxlength="50"></th>
          <td><input class="form-control small-input" type="text" v-model="newGame.description"
              placeholder="Entre une description" maxlength="50" /></td>
          <td><button @click="createNewGame" type="button" class="btn btn-dark btn-sm"><i class="bi bi-plus-lg"></i>
              Créer</button></td>
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

      if (confirm("Etes-vous sur.e de supprimer ce jeu ? Cela supprimera toutes les étapes et scénarios associés")) {
        axios.delete('game/' + gameId + "/")
          .then(response => {
            console.log(response);
            this.getData();
          },
            (error) => {
              console.error(error)
            });
      }

    },

    modifyGame(gameId) {
      this.$router.push({ name: 'GameDetails', params: { id: gameId } })

    },

    createNewGame() {
      if (this.newGame.name.length < 1) { this.newGame.name = 'Jeu sans nom' }
      this.newGame.author = this.$store.state.userId
      axios.post('game/', this.newGame).then((response) => {
        console.log(response)
        this.newGame.name = "";
        this.newGame.description = "";
        this.getData()
      }).catch((error) => {
        console.log(error)
      });
    },
  },

  created() {
    this.getData();
  },
};
</script>