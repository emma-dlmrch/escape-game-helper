<template>
    <h1>{{ step.title }}</h1>
    <form  @submit.prevent="modifyStep">
        <div class="form-group">
            <label for="step-name">Nom de l'étape</label>
            <input id="step-name" type="text" class="form-control" v-model.lazy="step.title" required>
        </div>
        <div class="form-group">
            <label for="step-text">Texte</label>
            <textarea id="step-text" class="form-control" v-model="step.text" rows="5" required></textarea>
        </div>
        <div class="form-group">
            <label for="step-answer">Réponse attendue</label>
            <input id="step-answer" type="text" class="form-control" v-model="step.answer">
            <small id="answer-help" class="form-text text-muted">Laisse le champ vide si l'étape ne requiert pas de réponse</small>
        </div>
        <div>
            <button type="submit" class="btn btn-dark">Mettre à jour l'étape</button>
            <button @click="cancel" type="button" class="btn btn-light">Retour</button>
        </div>
    </form>

    <h2>Les indices</h2>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">Titre</th>
                <th scope="col">Texte</th>
                <th scope="col">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="clue in clues" v-bind:key="clue.id">
                <th scope="row">{{ clue.title }}</th>
                <td>{{ clue.text.substring(0, 20) }} ...</td>
                <td><button @click="modifyClue(clue.id)" type="button" class="btn btn-dark btn-sm">Modifier</button> <button
                        @click="deleteClue(clue.id)" type="button" class="btn btn-outline-dark btn-sm">Supprimer</button>
                </td>
            </tr>
            <tr>
                <th><input type="text" v-model="newClue.title" placeholder="Nouvel indice" maxlength="50"></th>
                <td><input type="text" v-model="newClue.text" placeholder="Entre un texte" maxlength="50" /></td>
                <td><button @click="createNewClue" type="button" class="btn btn-dark btn-sm">Créer</button></td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import axios from 'axios';
export default {
    name: 'GameDetails',
    data() {
        return {
            gameId: this.$route.params.gameId,
            stepId: this.$route.params.stepId,
            step: {
                title: '',
                text: '',
                answer: '',
            },
            clues: [],
            newClue: {
                title: '',
                text: '',
                step: ''
            }
        }
    },

    methods: {
        getStepData() {
            axios.get("step/" + this.stepId + "/")
                .then(response => {
                    this.step = response.data;
                    this.clues = response.data.clues
                    console.log(response)
                }, (error) => {
                    console.log(error)
                }
                )

        },

        modifyStep() {
            try {
                axios.put('step/' + this.stepId + "/", this.step).then((response) => {
                    console.log(response)
                }
                );
                this.$router.push({ name: 'GameDetails', params: { id: this.gameId } })
            } catch (error) {
                console.error("Error during form submission:", error);
            }
        },

        cancel() {
            this.$router.push({ name: 'GameDetails', params: { id: this.gameId } })
        },
        createNewClue() {

            try {
                if (this.newClue.title.length < 1) { this.newClue.title = 'Indice sans nom' }
                if (this.newClue.text.length < 1) { this.newClue.text = 'Pas de description' }
                this.newClue.step = this.stepId
                axios.post('clue/', this.newClue).then((response) => {
                    console.log(response)
                    this.getStepData()
                });
            } catch (error) {
                console.error("Error during form submission:", error);
            }

        },

        deleteClue(clueId){
            axios.delete('clue/' + clueId + "/")
                .then(response => {
                    console.log(response);
                    this.getStepData();
                },
                    (error) => { console.log("Error", error) });
        },
        modifyClue(clueId){
            console.log(clueId)
            this.$router.push({ name: 'UpdateClue', params: { gameId: this.gameId, stepId: this.stepId, clueId:clueId } })
        }


    },
    created() {
        this.getStepData();
    },
}
</script>