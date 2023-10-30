<template>
    <h1>Jeu : {{ game.name }}</h1>
    <form @submit="modifyGame">
        <div class="form-group">
            <label for="name">Nom</label>
            <input type="text" id="name" class="form-control" v-model.lazy="game.name" required>
        </div>
        <div class="form-group">
            <label for="description">Text descriptif</label>
            <textarea class="form-control" v-model="game.description" id="description" rows="3" required></textarea>
        </div>
        <div class="button-general-div">
            <button type="submit" class="btn btn-dark btn-sm"><i class="bi bi-check-lg"></i> Mettre à jour</button>
        </div>
    </form>

    <h2>Liste d'étapes</h2>
    <div class="table-responsive">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Etapes</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="step in this.steps" v-bind:key="step.id">
                    <th scope="row"><i class="bi bi-journal-text"></i> {{ step.title }}</th>
                    <td><button @click="modifyStep(step.id)" type="button" class="btn btn-dark btn-sm"><i
                                class="bi bi-pencil"></i> Gérer</button>&nbsp;
                        <button @click="deleteStep(step.id)" type="button" class="btn btn-outline-dark btn-sm"><i
                                class="bi bi-trash"></i> Supprimer</button>
                    </td>
                </tr>
                <tr>
                    <th><input class="form-control small-input" type="text" v-model="newStep.title"
                            placeholder="Nouvelle étape" maxlength="50"></th>
                    <td><button @click="createNewStep" type="button" class="btn btn-dark btn-sm"><i
                                class="bi bi-plus-lg"></i> Créer</button></td>
                </tr>
            </tbody>
        </table>
    </div>
    <h2>Organiser mes étapes</h2>
    <div class="table-responsive">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Scénarios</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="scenario in this.scenarios" v-bind:key="scenario.id">
                    <th scope="row"><i class="bi bi-share"></i> {{ scenario.name }}</th>
                    <td><button @click="modifyScenario(scenario.id)" type="button" class="btn btn-dark btn-sm"><i
                                class="bi bi-pencil"></i> Gérer</button>&nbsp;<button @click="deleteScenario(scenario.id)"
                            type="button" class="btn btn-outline-dark btn-sm"><i class="bi bi-trash"></i> Supprimer</button>
                    </td>
                </tr>
                <tr>
                    <th><input class="form-control small-input" type="text" v-model="newScenario.name"
                            placeholder="Nouveau scénario" maxlength="50"></th>
                    <td><button @click="createNewScenario" type="button" class="btn btn-dark btn-sm"><i
                                class="bi bi-plus-lg"></i> Créer</button></td>
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
                name: '',
                game: ''
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
            if (this.newStep.title.length < 1) { this.newStep.title = 'Etape sans nom' }
            this.newStep.game = this.gameId
            axios.post('step/', this.newStep).then((response) => {
                console.log(response)

                this.newStep.title = "";
                this.getGameData()
            }).catch((error) => {
                console.error("Error during form submission:", error);
            });
        },

        createNewScenario() {
            if (this.newScenario.name.length < 1) { this.newScenario.name = 'Scenario sans nom' }
            this.newScenario.game = this.gameId
            axios.post('scenario/', this.newScenario).then((response) => {
                console.log(response)
                this.newScenario.title = "";
                this.getGameData()
            }).catch((error) => {
                console.error("Error during form submission:", error);
            });
        },

        deleteScenario(scenarioId) {
            if (confirm("Etes-vous sûr.e de vouloir supprimer ce scénario ?")) {
                axios.delete('scenario/' + scenarioId + "/")
                    .then(response => {
                        console.log(response);
                        this.getGameData();
                    },
                        (error) => { console.log("Error", error) });
            }

        },

        deleteStep(stepId) {
            if (confirm("Etes-vous sûr.e de vouloir supprimer cette étape de jeu ?")) {
                axios.delete('step/' + stepId + "/")
                    .then(response => {
                        console.log(response);
                        this.getGameData();
                    },
                        (error) => { console.log("Error", error) });
            }
        },

        modifyStep(stepId) {
            this.$router.push({ name: 'StepDetails', params: { stepId: stepId, gameId: this.gameId } })
        },

        modifyScenario(scenarioId) {
            this.$router.push({ name: 'ScenarioDetails', params: { gameId: this.gameId, scenarioId: scenarioId } })
        },
        modifyGame(e) {
            e.preventDefault();
                axios.put('game/' + this.gameId + "/", this.game).then((response) => {
                    console.log(response)
                    this.getGameData(); //pourquoi il est pas dans le then lui ?
                }, (error) => {
                    console.log(error)
                }
                );
        },
    },

    created() {
        this.getGameData();
    },
}
</script>