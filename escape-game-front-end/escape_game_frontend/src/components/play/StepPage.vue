<template>
    <h1>{{ step.title }}</h1>
    <p>{{ step.text }}</p>
    <form @submit="submitAnswer">
        <div class="form-group">
            <label for="answer">Je réponds : </label>
            <input id="answer" type="text" class="form-control" v-model="submittedAnswer.answer" required>
        </div>
        <div>
            <button type="submit" class="btn btn-dark">Je tente !</button>
        </div>
    </form>
    <p v-if="isWrongAnswer">Ce n'est pas la bonne réponse</p>

    <div v-for="clue in step.clues" v-bind:key="clue.id">
        <button class="btn btn-dark" @click="showClue(clue)">Indice caché</button>
    </div>
    <clue-modal :clueId="selectedClueId" v-if="isClueModalEnabled" @clue-read="disableClueModal"></clue-modal>

    <!-- <div v-for="node in nextNodes" v-bind:key="node.id">{{ node.id }}, step : {{ node.step }}, scenario : {{ node.scenario
    }}</div> -->
</template>

<script>
import axios from 'axios';
import ClueModal from './ClueModal.vue';

export default {
    name: 'StepPage',
    // props:['scenarioNodeId'],
    components: {
        ClueModal
    },
    data() {
        return {
            step: {
                title: '',
                text: '',
                clues: []
            },
            submittedAnswer: {
                answer: ''
            },
            isClueModalEnabled: false,
            selectedClueId: '',
            // scenarioNodeId: 88,
            isWrongAnswer: false,
            nextNodes: [],
            scenarioNode: {
                id: '',
                step: '',
                scenario:'',
            },
            scenarioNodeId: this.$route.params.scenarioNodeId

        }
    },
    methods: {
        getStepData() {
            axios.get("play/step/"+this.scenarioNode.step +"/")
                .then(response => {
                    this.step = response.data;
                    console.log(response)
                }, (error) => {
                    console.log(error)
                }
                )

        },
        getNodeData() {
            axios.get("play/scenario_node/"+ this.scenarioNodeId + "/")
                .then(response => {
                    this.scenarioNode = response.data;
                    console.log(response)
                    this.getStepData()
                    this.$store.commit('unlockNode', this.scenarioNode) //il faudrait le faire qu'une fois au démarrage...
                }, (error) => {
                    console.log(error)
                }
                )
        },
        submitAnswer(e) {
            e.preventDefault()
            try {
                axios.post('play/scenario_node/answer/' + this.scenarioNodeId + "/", this.submittedAnswer).then((response) => {
                    if (response.data.message == false) {
                        this.isWrongAnswer = true
                    } else {
                        this.submittedAnswer.answer = "";
                        this.isWrongAnswer = false
                        this.nextNodes = response.data
                        this.nextNodes.forEach((node) => {
                            console.log("node", node)
                            this.$store.commit('unlockNode', node)
                        });
                    }
                });
            } catch (error) {
                console.error("Error during form submission:", error);
            }
        },

        showClue(clueId) {
            this.selectedClueId = clueId
            this.isClueModalEnabled = true
        },

        disableClueModal() {
            this.isClueModalEnabled = false
        },
    },
    created() {
        this.getNodeData()
    },
    updated() {
        if(this.scenarioNodeId !== this.$route.params.scenarioNodeId){
            this.scenarioNodeId = this.$route.params.scenarioNodeId;
            this.getNodeData()
        }
    }
}
</script>