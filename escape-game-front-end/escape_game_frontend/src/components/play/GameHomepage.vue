<template>
    <h1>Jouons !</h1>
    <p>Tu as été invité.e à jouer à un jeu !</p>
    <p>Entre le code du scénario auquel tu as été invité.e à jouer (pour l'instant il s'agit de son ID)</p>
    <form @submit.prevent="playGame">
        <div class="form-group">
            <label for="inputScenarioId">Scenario ID</label>
            <input type="text" v-model="scenarioId" class="form-control" id="inputScenarioId" required>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="deleteCheckbox" v-model="deleteScenarioHistory">
                <label class="form-check-label" for="deleteCheckbox">Je veux recommencer et supprimer ma progression
                    (irréversible) !</label>
            </div>
        </div>
        <button type="submit" class="btn btn-primary">Let's go !</button>
    </form>
    <p v-if="wrongScenarioCode">Ce code scénario n'est pas bon !</p>
</template>

<script>
import axios from 'axios';
export default {
    name: 'GameHomepage',
    data() {
        return {
            scenarioNode: {
                id: '',
                step: '',
                scenario: ''
            },
            scenarioId: '',
            deleteScenarioHistory: false,
            wrongScenarioCode: false,
        }
    },
    methods: {
        checkScenarioExists() {


        },
        playGame() {
            axios.get("play/scenario/" + this.scenarioId + "/")
                .then(response => {
                    console.log(response)
                    if (response.data.id) {
                        if (this.deleteScenarioHistory) {
                            this.$store.commit('emptyUnlockedNodes')
                        }
                        this.$store.commit('setCurrentPlayedScenarioId', this.scenarioId)
                        this.$router.push({ name: 'ScenarioPage', params: { scenarioId: this.scenarioId } })
                    } else {
                        this.wrongScenarioCode = true
                    }


                }, (error) => {
                    console.log(error)
                    this.wrongScenarioCode = true
                }
                )


        },
    },
}

</script>