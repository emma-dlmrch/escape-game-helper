<template>
    <h1>{{ scenario.name }}</h1>
    <h2>Gérer mes noeuds</h2>

    <h3>Créer un noeud</h3>
    <form>
        <div class="form-group">
            <label>Etape</label>
            <select v-model="newNode.step" class="form-control form-control-sm">
                <option disabled selected value> -- choisis une étape -- </option>
                <option v-for="step in stepList" v-bind:key="step.id" :value="step.id">{{ step.title }}</option>
            </select>
        </div>
        <div>
            <label>Noeud Parent</label>
            <select v-model="newNode.parent_node" class="form-control form-control-sm">
                <option disabled selected value> -- choisis un noeud parent -- </option>
                <option v-for="node in scenarioNodesFlat" v-bind:key="node.id" :value="node.id">{{ node.label }}</option>
            </select>
        </div>
        <button type="button" class="btn btn-dark btn-sm" @click="createNewNode">OK</button>
    </form>
    <h3>Liste des noeuds</h3>
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
            <!-- <tr>
                <th><input type="text" v-model="newNode.step" placeholder="Etape" maxlength="50"></th>
                <td><input type="text" v-model="newNode.parent" placeholder="Parent" maxlength="50" />
                </td>
                <td><button @click="createNewNode" type="button" class="btn btn-dark btn-sm">Créer</button></td>
            </tr> -->
        </tbody>
    </table>


    <h3>Schéma</h3>
    <!-- <draggable v-model="scenarioNodes"> -->
    <div class="tf-tree">
        <tree-view :data="scenarioNodes"></tree-view>
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
    }, //might need to use computed values for select 
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
                scenario:''
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
            if ((!this.newNode.step) || (!this.newNode.parent_node)) {
                console.log("ça va pas le faire")
            } else {
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

        deleteNode(nodeId){
            axios.delete('scenario_node/' + nodeId + "/")
                .then(response => {
                    console.log(response);
                    this.getData();
                },
                    (error) => { console.log("Error", error) });
        },

        getData(){
            this.getScenarioData()
            this.getStepList()
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