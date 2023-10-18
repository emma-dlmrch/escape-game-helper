<template>
    <h1>{{ scenario.name }}</h1>
    <div><button @click="cancel" class="btn btn-dark btn-sm">Retour</button></div>
    <h2>Renommer le scénario</h2>
    <form @submit.prevent="renameScenario">
        <div class="form-group">
            <label for="name">Nom du scénario</label>
            <input type="text" id="name" class="form-control" v-model.lazy="scenario.name" required>
        </div>
        <button type="submit" class="btn btn-dark btn-sm">OK</button>
    </form>
    <h2>Gérer mes noeuds de scénario</h2>

    <div v-if="!scenarioNodesFlat.length">
    <h3>Quelle sera votre étape d'introduction ?</h3>
    <form @submit.prevent="createFirstNode">
        <div class="form-group">
            <label>Etape</label>
            <select v-model="newNode.step" class="form-control form-control-sm" required>
                <option disabled selected value> -- choisis une étape -- </option>
                <option v-for="step in stepList" v-bind:key="step.id" :value="step.id">{{ step.title }}</option>
            </select>
        </div>
        <button type="submit" class="btn btn-dark btn-sm">OK</button>
    </form>
</div>

    <div class="tf-tree">
        <tree-view :data="scenarioNodes" @create-node="receiveCreateNodeEvent" @update-node="receiveUpdateNodeEvent"></tree-view>
    </div>
    <create-node :parentNodeId="parentNodeId" :gameId="gameId" :scenarioId="scenarioId" v-if="isCreationFormEnabled" @node-created="disableCreationForm"></create-node>
    <update-node :nodeId="nodeToUpdate" :gameId="gameId" :scenarioId="scenarioId" v-if="isUpdateFormEnabled" @node-updated="disableUpdateForm"></update-node>

</template>

<script>
import axios from 'axios'
import TreeView from './TreeView.vue'
import CreateNode from './CreateNode.vue'
import UpdateNode from './UpdateNode.vue'

export default {
    name: 'ScenarioDetails',
    components: {
        TreeView,
        CreateNode,
        UpdateNode
    },
    data() {
        return {
            items: '',
            scenarioId: this.$route.params.scenarioId,
            scenario: {
                name: ''
            },
            scenarioNodes: [],
            scenarioNodesFlat: [],
            newNode: {
                parent_node: '',
                step: '',
                scenario: ''
            },
            stepList: [],
            gameId: this.$route.params.gameId,
            parentNodeId:'',
            nodeToUpdate:'',
            isCreationFormEnabled: false,
            isUpdateFormEnabled: false
        }

    },

    methods: {

        getScenarioData() {
            axios.get("scenario/" + this.scenarioId + "/")
                .then(response => {
                    this.scenario = response.data
                    this.scenarioNodes = response.data.scenario_nodes
                    this.scenarioNodesFlat = response.data.scenario_nodes_flat
                    console.log(this.scenarioNodes)
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

        createNewNode() {
            if (this.newNode.step && this.newNode.parent_node) {
                if (this.newNode.parent_node === -1) {
                    this.newNode.parent_node = ''
                }
                try {
                    this.newNode.scenario = this.scenarioId
                    axios.post('scenario_node/', this.newNode).then((response) => {
                        console.log(response)
                        this.getData()
                    });
                } catch (error) {
                    console.error("Error during form submission:", error);
                }
            }

        },
        createFirstNode() {
            if (this.newNode.step) {
                    this.newNode.parent_node = ''
                try {
                    this.newNode.scenario = this.scenarioId
                    axios.post('scenario_node/', this.newNode).then((response) => {
                        console.log(response)
                        this.getData()
                    });
                } catch (error) {
                    console.error("Error during form submission:", error);
                }
            }

        },

        deleteNode(nodeId) {
            axios.delete('scenario_node/' + nodeId + "/")
                .then(response => {
                    console.log(response);
                    this.getData();
                },
                    (error) => { console.log("Error", error) });
        },
        renameScenario() {
            axios.put('scenario/' + this.scenarioId + "/", this.scenario)
                .then(response => {
                    console.log(response);
                    this.getData();
                },
                    (error) => { console.log("Error", error) });
        },
        cancel() {
            this.$router.push({ name: 'GameDetails', params: { id: this.gameId } })
        },

        getData() {
            this.getScenarioData()
            this.getStepList()
        },
        modifyNode(nodeId) {
            this.$router.push({name: 'UpdateNode', params: {gameId: this.gameId, scenarioId: this.scenarioId, nodeId:nodeId}})
            // let node = this.scenarioNodesFlat[nodeId]
            // axios.put('scenario_node/' + nodeId + "/", node)
            //     .then(response => {
            //         console.log(response);
            //         this.getData();
            //     },
            //         (error) => { console.log("Error", error) });
        },
        receiveCreateNodeEvent(parentNodeId){
            this.parentNodeId = parentNodeId
            this.isCreationFormEnabled = true

        },
        receiveUpdateNodeEvent(nodeId){
            this.nodeToUpdate = nodeId
            this.isUpdateFormEnabled = true

        },
        disableCreationForm(){
            this.isCreationFormEnabled = false
            this.getData()
        },
        disableUpdateForm(){
            this.isUpdateFormEnabled = false
            this.getData()
        }

    },

    created() {
        this.getData()
    },
}


</script>

<!-- IMPLEMENT
https://www.cssscript.com/semantic-hierarchy-tree-treeflex/
or 
https://www.cssscript.com/clean-tree-diagram/
 -->