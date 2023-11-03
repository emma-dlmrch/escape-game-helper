<template>
    <h1>Etape : {{ step.title }}</h1>
    <form @submit.prevent="modifyStep">
        <div class="form-group">
            <label for="step-name">Nom de l'étape :</label>
            <input id="step-name" type="text" class="form-control" v-model.lazy="step.title" @click="disableWasUpdatedMessage" required>
        </div>
        <div class="form-group">
            <label for="step-text">Texte :</label>
            <textarea id="step-text" class="form-control" v-model="step.text" rows="5" @click="disableWasUpdatedMessage" required></textarea>
        </div>
        <div class="form-group">
            <label for="step-answer">Réponse attendue :</label>
            <input id="step-answer" type="text" class="form-control" v-model="step.answer" @click="disableWasUpdatedMessage">
            <small id="answer-help" class="form-text text-muted">Laisse le champ vide si l'étape ne requiert pas de
                réponse</small>
        </div>
        <div>
            <button type="submit" class="btn btn-dark btn-sm"><i class="bi bi-pencil"></i> Enregistrer</button>
            
        </div>
        <small v-if ="wasUpdated" class="form-text text-muted"><i class="bi bi-check"></i> Modifications enregistrées !</small>
    </form>

    <h2>Les indices</h2>
    <div class="table-responsive">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th scope="col">Titre</th>
                    <th scope="col">Texte</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="clue in clues" v-bind:key="clue.id">
                    <th scope="row"><i class="bi bi-search"></i> {{ clue.title }}</th>
                    <td><i class="bi bi-journal-text"></i> {{ clue.text.substring(0, 20) }} ...</td>
                    <td><button @click="modifyClue(clue.id)" type="button" class="btn btn-dark btn-sm"><i
                                class="bi bi-pencil"></i> Modifier</button>&nbsp;
                        <button @click="deleteClue(clue.id)" type="button" class="btn btn-outline-dark btn-sm"><i
                                class="bi bi-trash"></i> Supprimer</button>
                    </td>
                </tr>
                <tr>
                    <th><input type="text" v-model="newClue.title" placeholder="Nouvel indice" maxlength="50"
                            class="form-control small-input" /></th>
                    <td><input type="text" v-model="newClue.text" placeholder="Entre un texte" maxlength="50"
                            class="form-control small-input" /></td>
                    <td><button @click="createNewClue" type="button" class="btn btn-dark btn-sm"><i
                                class="bi bi-plus-lg"></i> Créer</button></td>
                </tr>
            </tbody>
        </table>
    </div>
    <div>
        <button @click="cancel" type="button" class="btn btn-dark btn-sm"><i class="bi bi-arrow-left"></i> Retour</button>
    </div>
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
            },
            wasUpdated: false
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
            axios.put('step/' + this.stepId + "/", this.step).then((response) => {
                if (response.status == 200) {
                    this.wasUpdated = true
                }
            }).catch((e) => {
                console.log("Couldn't edit step", e);
            });
        },

        cancel() {
            this.$router.push({ name: 'GameDetails', params: { id: this.gameId } })
        },
        createNewClue() {

            if (this.newClue.title.length < 1) { this.newClue.title = 'Indice sans nom' }
            if (this.newClue.text.length < 1) { this.newClue.text = 'Pas de description' }
            this.newClue.step = this.stepId
            axios.post('clue/', this.newClue).then((response) => {
                console.log(response)
                this.newClue.title = ''
                this.newClue.text = ''
                this.getStepData()
            }).catch((error) => {
                console.error("Error during form submission:", error);
            });

        },

        deleteClue(clueId) {
            if (confirm("Etes vous sûr.e de vouloir supprimer cet indice ?")) {
                axios.delete('clue/' + clueId + "/")
                    .then(response => {
                        console.log(response);
                        this.getStepData();
                    },
                        (error) => { console.log("Error", error) });
            }
        },
        modifyClue(clueId) {
            this.$router.push({ name: 'UpdateClue', params: { gameId: this.gameId, stepId: this.stepId, clueId: clueId } })
        },

        disableWasUpdatedMessage(){
            this.wasUpdated = false
        }


    },
    created() {
        this.getStepData();
    },
}
</script>