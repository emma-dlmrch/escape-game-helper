<template>
        <h1>{{ step.title }}</h1>
        <p>{{ step.text }}</p>

        <div v-if="step.has_answer">
            <div v-if="!scenarioNode.resolved">

                <form @submit="submitAnswer">
                    <div class="form-group">
                        <label for="answer">Je réponds : </label>
                        <input @click="disableWrongAnswerText" id="answer" type="text" class="form-control small-input"
                            v-model="submittedAnswer.answer" required>
                    </div>
                    <div class="button-general-div">
                        <button type="submit" class="btn btn-dark">Je tente !</button>
                    </div>
                </form>
                <p v-if="isWrongAnswer">Ce n'est pas la bonne réponse</p>

                <div v-for="clue in step.clues" v-bind:key="clue.id">
                    <div class="button-general-div"><button class="btn btn-secondary btn-sm"
                            @click="showClue(clue)">Indice</button></div>
                </div>
                <clue-modal :clueId="selectedClueId" v-if="isClueModalEnabled" @clue-read="disableClueModal"></clue-modal>
                <success-modal :unlockedNodes="nextNodes" v-if="isRightAnswer"
                    @message-read="disableSuccessModal"></success-modal>
            </div>
            <div v-else>
                <p>Enigme terminée <i class="bi bi-check-lg"></i> </p>
            </div>
        </div>
</template>

<script>
import axios from 'axios';
import ClueModal from './ClueModal.vue';
import SuccessModal from './SuccessModal.vue';

export default {
    name: 'StepPage',
    // props:['scenarioNodeId'],
    components: {
        ClueModal,
        SuccessModal
    },
    data() {
        return {
            step: {
                title: '',
                text: '',
                clues: [],
                has_answer: '',
            },
            submittedAnswer: {
                answer: ''
            },
            isClueModalEnabled: false,
            selectedClueId: '',
            isWrongAnswer: false,
            isRightAnswer: false,
            nextNodes: [],
            scenarioNode: {
                id: '',
                step: '',
                scenario: '',
            },
            scenarioNodeId: this.$route.params.scenarioNodeId,

        }
    },
    methods: {
        getStepData() {
            axios.get("play/step/" + this.scenarioNode.step + "/")
                .then(response => {
                    this.step = response.data;
                    if (this.step.has_answer === false) {
                        this.$store.commit('setNodeInfo', this.scenarioNode)
                    }
                }, (error) => {
                    console.log(error)
                }
                )

        },
        getNodeData() {
            axios.get("play/scenario_node/" + this.scenarioNodeId + "/")
                .then(response => {
                    this.scenarioNode = response.data;
                    this.getStepData()
                    //retreive node status
                    if (this.$store.state.unlockedNodes.filter(x => x.id === this.scenarioNode.id)[0]) {
                        this.scenarioNode.resolved = this.$store.state.unlockedNodes.filter(x => x.id === this.scenarioNode.id)[0].resolved
                    }
                    this.$store.commit('setNodeRead', this.scenarioNode)
                    this.$store.commit('setCurrentPlayedScenarioId', this.scenarioNode.scenario)
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
                        this.submittedAnswer.answer='';
                    } else {
                        this.submittedAnswer.answer = '';
                        this.isWrongAnswer = false
                        this.nextNodes = response.data
                        this.nextNodes.forEach((node) => {
                            node.new = true
                            node.info = false,
                                node.resolved = false,
                                this.$store.commit('unlockNode', node)
                        });
                        this.isRightAnswer = true;
                    }
                });
            } catch (error) {
                console.error("Error during form submission:", error);
            }
        },
        disableWrongAnswerText() {
            this.isWrongAnswer = false
        },

        showClue(clueId) {
            this.selectedClueId = clueId
            this.isClueModalEnabled = true
        },

        disableClueModal() {
            this.isClueModalEnabled = false
        },
        disableSuccessModal() {
            this.isRightAnswer = false
            this.$store.commit('setNodeResolved', this.scenarioNode)
        },
        isUnlocked(nodeId) {
            for (var i = 0; i<this.$store.state.unlockedNodes.length ; i++) {
                if (this.$store.state.unlockedNodes[i].id == nodeId){
                    return true
                }
            }
            this.$router.push({name : 'ErrorView'})
            return false
        }
    },
    created() {
        if (this.isUnlocked(this.scenarioNodeId)) {
            this.getNodeData()
        }
        
    },
    updated() {
        if (this.scenarioNodeId !== this.$route.params.scenarioNodeId) {
            this.scenarioNodeId = this.$route.params.scenarioNodeId;
            // this.isUnlocked(this.scenarioNodeId)
            this.getNodeData()
        }
    }
}
</script>