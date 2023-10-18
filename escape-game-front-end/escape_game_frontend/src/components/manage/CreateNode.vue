<template>
    <h1>Créer un noeud</h1>
    <div>Quelle étape souhaitez-vous voir apparaître après {{ parentNode.stepLabel }}</div>
    <form @submit.prevent="createNewNode">
        <div class="form-group">
            <label>Etape</label>
            <select v-model="newNode.step" class="form-control form-control-sm" required>
                <option disabled selected value> -- choisis une étape -- </option>
                <option v-for="step in stepList" v-bind:key="step.id" :value="step.id">{{ step.title }}</option>
            </select>
        </div>
        <button type="submit" class="btn btn-dark btn-sm">OK</button>
    </form>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CreateNode',
    props: ["parentNodeId", "gameId", "scenarioId"],
    emits: ['node-created'],
    data() {
        return {
            stepList: [],
            parentNode: {
                stepLabel: '',
            },
            newNode: {
                parent_node: '',
                step: '',
                scenario: ''
            },
        }
    },
    methods: {
        getStepList() {
            axios.get("game/" + this.gameId + "/")
                .then(response => {
                    this.stepList = response.data.steps
                }, (error) => {
                    console.log(error)
                }
                )
        },
        getParentNodeData() {
            axios.get("scenario_node/" + this.parentNodeId + "/")
                .then(response => {
                    // this.parentNode.step = response.data.step
                    this.parentNode.stepLabel = response.data.step_title
                }, (error) => {
                    console.log(error)
                }
                )
        },

        createNewNode() {
            try {
                this.newNode.scenario = this.scenarioId
                this.newNode.parent_node = this.parentNodeId
                axios.post('scenario_node/', this.newNode).then((response) => {
                    console.log(response)
                    // this.$router.push({ name: 'ScenarioDetails', params: { gameid: this.gameId, scenarioId: this.scenarioId } })
                    this.$emit('node-created')
                });
            } catch (error) {
                console.error("Error during form submission:", error);
            }
        },
        getData(){
            this.getParentNodeData()
            this.getStepList()
        }

    },
    created () {
        this.getData()
    }
}
</script>