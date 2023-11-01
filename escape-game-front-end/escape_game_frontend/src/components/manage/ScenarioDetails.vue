<template>
    <h1>Scénario : {{ scenario.name }}</h1>


    <form @submit.prevent="renameScenario">
        <div class="form-group">
            <label for="name">Nom :</label>
            <input type="text" id="name" class="form-control small-input" v-model.lazy="scenario.name" required>
        </div>
        <div class="button-general-div">
            <button type="submit" class="btn btn-dark btn-sm"><i class="bi bi-check-lg"></i> Mettre à jour</button>
        </div>
    </form>
    <div>
        <p>Pour jouer à ce scénario, dis à tes joueurs et joueuses de
            se rendre <router-link :to="{ name: 'GameHomepage' }">ici</router-link> et d'entrer le code suivant : <b>{{
                scenarioId }}</b> !</p>
        <p></p>
    </div>
    <h2>Organiser les étapes</h2>

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
            <div class="button-general-div">
                <button type="submit" class="btn btn-dark btn-sm">OK</button>
            </div>
        </form>
    </div>

    <div class="tf-tree">
        <tree-view :data="scenarioNodes" @create-node="receiveCreateNodeEvent" @update-node="receiveUpdateNodeEvent"
            @delete-node="receiveDeleteNodeEvent"></tree-view>
    </div>
    <button @click="cancel" class="btn btn-dark btn-sm"><i class="bi bi-arrow-left"></i> Retour</button>
    <create-node :parentNodeId="parentNodeId" :gameId="gameId" :scenarioId="scenarioId" v-if="isCreationFormEnabled"
        @node-created="disableCreationForm"></create-node>
    <update-node :nodeId="nodeToUpdate" :gameId="gameId" :scenarioId="scenarioId" v-if="isUpdateFormEnabled"
        @node-updated="disableUpdateForm"></update-node>
    <delete-node :nodeId="nodeToDelete" v-if="isDeleteModalEnabled" @node-deleted="disableDeleteModal"></delete-node>
</template>

<script>
import axios from 'axios'
import TreeView from './TreeView.vue'
import CreateNode from './CreateNode.vue'
import UpdateNode from './UpdateNode.vue'
import DeleteNode from './DeleteNode.vue'

export default {
    name: 'ScenarioDetails',
    components: {
        TreeView,
        CreateNode,
        UpdateNode,
        DeleteNode
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
            parentNodeId: '',
            nodeToUpdate: '',
            nodeToDelete: '',
            isCreationFormEnabled: false,
            isUpdateFormEnabled: false,
            isDeleteModalEnabled: false
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

        createFirstNode() {
            if (this.newNode.step) {
                this.newNode.parent_node = ''
                this.newNode.scenario = this.scenarioId
                axios.post('scenario_node/', this.newNode).then(() => {
                    this.getData()
                }).catch((error) => {
                    console.error("Error during form submission:", error);
                });
            }

        },
        renameScenario() {
            axios.put('scenario/' + this.scenarioId + "/", this.scenario)
                .then(() => {
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
        receiveCreateNodeEvent(parentNodeId) {
            this.parentNodeId = parentNodeId
            this.isCreationFormEnabled = true

        },
        receiveUpdateNodeEvent(nodeId) {
            this.nodeToUpdate = nodeId
            this.isUpdateFormEnabled = true

        },
        receiveDeleteNodeEvent(nodeId) {
            this.nodeToDelete = nodeId
            this.isDeleteModalEnabled = true

        },
        disableCreationForm() {
            this.isCreationFormEnabled = false
            this.getData()
        },
        disableUpdateForm() {
            this.isUpdateFormEnabled = false
            this.getData()
        },
        disableDeleteModal() {
            this.isDeleteModalEnabled = false
            this.getData()
        },

    },

    created() {
        this.getData()
    },
}


</script>