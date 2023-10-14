<template>
    <p>{{ nodeId }}</p>
    <div v-for="node in allNodes" v-bind:key="node.id">
        <p v-if="node.id !== nodeId">{{ node.id }} - {{ nodeId }}</p>
        ça marche pas
    </div>
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
            allNodes: [],
            otherNodes: [],
            node: {
                id: '',
                step: '',
                parent_node: ''
            }
        }
    },
    methods: {
        getScenarioData() {
            axios.get("scenario/" + this.scenarioId + "/")
                .then(response => {
                    this.allNodes = response.data.scenario_nodes_flat
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
        removeSelfNode() {
            // this.otherNodes = this.allNodes
            // this.otherNodes = this.allNodes.filter(node => node.id !== this.node.id)
            const test = this.allNodes.filter(node => node.id !== this.node.id)
            console.log(test)
            console.log(this.allNodes)
        }

    },


    created() {
        this.getScenarioData()
        this.getNodeData()
        this.removeSelfNode()

    }
}


</script>