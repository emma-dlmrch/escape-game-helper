<template>
    <h2>Modifier un noeud</h2>

    <form @submit.prevent="updateNode">
        <div class="form-group">
            <label>Etape</label>
            <select v-model="node.step" class="form-control form-control-sm" required>
                <option disabled selected value> -- choisis une étape -- </option>
                <option v-for="step in stepList" v-bind:key="step.id" :value="step.id">{{ step.title }}</option>
            </select>
        </div>
        <div>
            <label>Noeud Parent</label>
            <select v-model="node.parent_node" class="form-control form-control-sm" required>
                <option disabled selected value> -- choisis un noeud parent -- </option>
                <!-- <option v-if="scenarioNodesFlat.length === 0" :value="-1">Première étape</option> -->
                <option v-for="node in otherNodes" v-bind:key="node.id" :value="node.id">{{ node.label }}</option>
            </select>
        </div>
        <button type="submit" class="btn btn-dark btn-sm">OK</button>
    </form>
</template>

<script>
import axios from 'axios';
export default {
    name: 'UpdateNode',
    components: {

    },
    data() {
        return {
            nodeId: this.$route.params.nodeId,
            scenarioId: this.$route.params.scenarioId,
            gameId: this.$route.params.gameId,
            stepList: [],
            allNodes: [],
            otherNodes: [],
            node: {
                id: '',
                step: '',
                parent_node: ''
            },
            
        }
    },
    methods: {
        getScenarioData() {
            axios.get("scenario/" + this.scenarioId + "/")
                .then(response => {
                    this.allNodes = response.data.scenario_nodes_flat
                    this.otherNodes = this.allNodes.filter(node => node.id !== this.node.id)
                }, (error) => {
                    console.log(error)
                }
                )
        },
        getNodeData() {
            axios.get("scenario_node/" + this.nodeId + "/")
                .then(response => {
                    this.node = response.data
                }, (error) => {
                    console.log(error)
                }
                )
        },
        
        getStepList() {
            axios.get("game/" + this.gameId + "/")
                .then(response => {
                    this.stepList = response.data.steps
                }, (error) => {
                    console.log(error)
                }
                )
        },
        updateNode(){
            axios.put('scenario_node/' + this.nodeId + "/", this.node)
                .then(response => {
                    console.log(response);
                    this.$router.push({ name: 'ScenarioDetails', params: { gameid: this.gameId, scenarioId: this.scenarioId } })
                },
                    (error) => { console.log("Error", error) });
        },
        getData(){
            this.getScenarioData()
            this.getNodeData()
            this.getStepList()
        }

    },


    created() {
        this.getData()
    }
}


</script>