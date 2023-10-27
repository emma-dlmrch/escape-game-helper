<template>
    <NavBar />
    <div class = "welcome-page">
    <h1>Jouons !</h1>
    <p>Tu as été invité.e à jouer à un jeu !</p>
    <p>Entre le code du scénario auquel tu as été invité.e à jouer</p>
    <form @submit.prevent="playGame">
        <div class="form-group">
            <label for="inputScenarioId">Code</label>
            <input type="text" v-model="scenarioId" class="form-control" id="inputScenarioId" @click="removeErrorMessage" required>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="deleteCheckbox" v-model="deleteScenarioHistory">
                <label class="form-check-label" for="deleteCheckbox">Je veux recommencer et supprimer ma progression
                    (irréversible) !</label>
            </div>
        </div>
        <div class ="centered-button"><button type="submit" class="btn btn-secondary btn-lg"><i class="bi bi-controller"></i> Let's go !</button></div>
        
    </form>
    <p v-if="wrongScenarioCode">Ce code scénario n'est pas bon !</p>
</div>
</template>

<script>
import NavBar from '../manage/NavBar.vue'
import axios from 'axios';
export default {
    name: 'GameHomepage',
    components: {NavBar},
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
                    if (error.response.status=="404") { //what is better?
                        this.wrongScenarioCode = true
                        this.scenarioId=''
                    }
                }
                )


        },

        removeErrorMessage(){
            this.wrongScenarioCode = false
        }
    },
}

</script>