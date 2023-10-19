<template>
    <div class="modal fade show background-modal" @click="goBack">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Modifier un noeud</h5>
                <button type="button" class="btn-close close-btn" aria-label="Close" @click="goBack"></button>
            </div>
            <form @submit.prevent="updateNode">
            <div class="modal-body">

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
                            <option v-for="node in otherNodes" v-bind:key="node.id" :value="node.id">{{ node.label }}</option>
                        </select>
                    </div>                    
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary btn-sm close-btn" @click="goBack">Fermer</button>
                    <button type="submit" class="btn btn-dark btn-sm">Valider</button>
                </div>
            </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'UpdateNode',
    props: ["nodeId", "gameId", "scenarioId"],
    emits: ['node-updated'],
    components: {

    },
    data() {
        return {
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
                    this.$emit('node-updated')
                },
                    (error) => { console.log("Error", error) });
        },

        goBack(e){
            console.log(e.target.className.includes("close-btn"))

            if(e.target.className.includes("background-modal")||e.target.className.includes("close-btn")){
                this.$emit('node-updated');
            }
        },
        getData(){
            this.getScenarioData()
            this.getNodeData()
            this.getStepList()
        },
    },


    created() {
        this.getData()
    }
}


</script>