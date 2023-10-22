<template>
    <p> entre l'id du scénario auquel tu as été invité à jouer (à terme, code)</p>
    <form @submit.prevent="playGame">
        <div class="form-group">
                <label for="inputScenarioId">Scenario ID</label>
                <input type="text" v-model="scenarioId" class="form-control" id="inputScenarioId" required>
            </div>
            <button type="submit" class="btn btn-primary">Let's go</button>
    </form>
</template>

<script>
export default {
    name: 'GameHomepge',
    data(){
        return {
            scenarioNode: {
                id: '',
                step: '',
                scenario:''
            },
            scenarioId:''
        }
    },
    methods: {
        playGame(){
            this.$router.push({ name: 'ScenarioPage', params: { scenarioId: this.scenarioId }} )
        },
    },
}

</script>