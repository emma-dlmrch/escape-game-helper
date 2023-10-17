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

    <!-- <h3>Créer un noeud</h3>
    <form @submit.prevent="createNewNode">
        <div class="form-group">
            <label>Etape</label>
            <select v-model="newNode.step" class="form-control form-control-sm" required>
                <option disabled selected value> -- choisis une étape -- </option>
                <option v-for="step in stepList" v-bind:key="step.id" :value="step.id">{{ step.title }}</option>
            </select>
        </div>
        <div>
            <label>Noeud Parent</label>
            <select v-model="newNode.parent_node" class="form-control form-control-sm" required>
                <option disabled selected value> -- choisis un noeud parent -- </option>
                <option v-if="scenarioNodesFlat.length === 0" :value="-1">Première étape</option>
                <option v-for="node in scenarioNodesFlat" v-bind:key="node.id" :value="node.id">{{ node.label }}</option>
            </select>
        </div>
        <button type="submit" class="btn btn-dark btn-sm">OK</button>
    </form> -->
    <!-- <h3>Liste des noeuds</h3>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">Mes noeuds</th>
                <th scope="col">Noeud parent</th>
                <th scope="col">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="node in scenarioNodesFlat" v-bind:key="node.id">
                <th scope="row">{{ node.label }}</th>
                <td>{{ node.parent_node_title }}</td>
                <td><button @click="modifyNode(node.id)" type="button" class="btn btn-dark btn-sm">Modifier</button> <button
                        @click="deleteNode(node.id)" type="button" class="btn btn-outline-dark btn-sm">Supprimer</button>
                </td>
            </tr>
        </tbody>
    </table> -->


    <!-- <h3>Schéma</h3> -->
    <!-- <draggable v-model="scenarioNodes"> -->
    <div class="tf-tree">
        <tree-view :data="scenarioNodes" :gameId="gameId" :scenarioId="scenarioId"></tree-view>
    </div>
    <!-- </draggable> -->
</template>

<script>
import axios from 'axios'
import TreeView from './TreeView.vue'
// import draggable from 'vuedraggable'

export default {
    name: 'ScenarioDetails',
    components: {
        TreeView,
        // draggable
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