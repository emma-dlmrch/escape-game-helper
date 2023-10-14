<template>
    <h1 >{{ game.name }}</h1>
    <form @submit="modifyGame">
        <div class="form-group">
            <label for="name">Nom</label>
            <input type="text" id="name" class="form-control" v-model.lazy="game.name" required>
        </div>
        <div class="form-group">
            <label for="description">Text descriptif</label>
            <textarea class="form-control" v-model="game.description" id="description" rows="3" required></textarea>
        </div>
        <button type="submit" class="btn btn-light btn-sm">Modifier</button>
    </form>

    <h2>Liste d'étapes</h2>
    <div>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">Etape</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="step in this.steps" v-bind:key="step.id">
                    <th scope="row">{{ step.title }}</th>
                    <td><button @click="modifyStep(step.id)" type="button" class="btn btn-dark btn-sm">Gérer</button> <button
                         @click="deleteStep(step.id)" type="button"
                            class="btn btn-light btn-sm">Supprimer</button>
                    </td>
                </tr>
                <tr>
                    <th><input type="text" v-model="newStep.title" placeholder="Nouvelle étape" maxlength="50"></th>
                    <td><button @click="createNewStep" type="button" class="btn btn-dark btn-sm">Créer</button></td>
                </tr>
            </tbody>
        </table>
    </div>
    <h2>Organiser mes étapes</h2>
    <div>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Scénario</th>
          <th scope="col">Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="scenario in this.scenarios" v-bind:key="scenario.id">
          <th scope="row">{{ scenario.name }}</th>
          <td><button @click="modifyScenario(scenario.id)" type="button" class="btn btn-dark btn-sm">Gérer</button> <button
              @click="deleteScenario(scenario.id)" type="button" class="btn btn-light btn-sm">Supprimer</button></td>
        </tr>
        <tr>
          <th><input type ="text" v-model="newScenario.name" placeholder="Nouveau scénario" maxlength="50"></th>
          <td><button @click="createNewScenario" type="button" class="btn btn-dark btn-sm">Créer</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>

import axios from 'axios';

export default {
    name: 'GameDetails',
    data() {
        return {
            game: {
                name: '',
                description: '',
            },
            gameId: this.$route.params.id,
            steps: [],
            newStep: {
                title: '',
                game: '',
            },
            scenarios: [],
            newScenario: {
                name:'',
                game:''
            }
        }

    },
    computed: {
    },

    methods: {
        getGameData() {
            axios.get("game/" + this.gameId + "/")
                .then(response => {
                    this.game = response.data
                    this.steps = response.data.steps
                    this.scenarios = response.data.scenarios
                }, (error) => {
                    console.log(error)
                }
                )
        },

        createNewStep() {
            try {
                if (this.newStep.title.length < 1) { this.newStep.title = 'Etape sans nom' }
                this.newStep.game = this.gameId
                axios.post('step/', this.newStep).then((response) => {
                    console.log(response)
                    this.newStep.title = "";
                    this.getGameData()
                });
            } catch (error) {
                console.error("Error during form submission:", error);
            }
        },

        createNewScenario() {
            try {
                if (this.newScenario.name.length < 1) { this.newScenario.name = 'Scenario sans nom' }
                this.newScenario.game = this.gameId
                axios.post('scenario/', this.newScenario).then((response) => {
                    console.log(response)
                    this.newScenario.title = "";
                    this.getGameData()
                });
            } catch (error) {
                console.error("Error during form submission:", error);
            }
        },

        deleteScenario(scenarioId) {
            axios.delete('scenario/' + scenarioId + "/")
                .then(response => {
                    console.log(response);
                    this.getGameData();
                },
                    (error) => { console.log("Error", error) });
        },

        deleteStep(stepId) {
            axios.delete('step/' + stepId + "/")
                .then(response => {
                    console.log(response);
                    this.getGameData();
                },
                    (error) => { console.log("Error", error) });
        },

        modifyStep(stepId){
            this.$router.push({name: 'StepDetails', params: {stepId: stepId, gameId: this.gameId}})
        },

        modifyScenario(scenarioId){
            this.$router.push({name: 'ScenarioDetails', params: {gameId: this.gameId, scenarioId: scenarioId}})
        },
        modifyGame(){
            try {
                axios.put('game/' + this.gameId + "/", this.game).then((response) => {
                    console.log(response)
                }
                );
                this.getGameData();
            } catch (error) {
                console.error("Error during form submission:", error);
            }
        },
    },

    created() {
        this.getGameData();
    },
}
</script>