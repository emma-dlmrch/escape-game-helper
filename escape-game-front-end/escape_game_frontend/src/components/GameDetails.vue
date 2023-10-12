<template>
    <h1>{{ game.name }}</h1>
    <form>
        <div class="form-group">
            <label>Nom</label>
            <input type="text" id="disabledInput" class="form-control" v-bind:placeholder="game.name">
        </div>
        <div class="form-group">
            <label>Text descriptif</label>
            <textarea class="form-control" v-bind:placeholder="game.description" rows="3"></textarea>
        </div>
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
                    <td><button @click="modifyStep(step.id)" type="button" class="btn btn-dark btn-sm">Gérer</button>
                        <button @click="deleteStep(step.id)" type="button"
                            class="btn btn-outline-dark btn-sm">Supprimer</button>
                    </td>
                </tr>
                <tr>
                    <th><input type="text" v-model="newStep.title" placeholder="Nouvelle étape" maxlength="50"></th>
                    <td><button @click="createNewStep" type="button" class="btn btn-dark btn-sm">Créer</button></td>
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
            }
        }

    },
    computed: {
    },

    methods: {
        getGameData() {
            axios.get("game/" + this.gameId + "/")
                .then(response => {
                    this.game = response.data;
                    this.steps = response.data.steps
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
        }
    },

    created() {
        this.getGameData();
    },
}
</script>