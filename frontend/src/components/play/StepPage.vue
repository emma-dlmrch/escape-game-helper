<template>
    <h1>{{ step.title }}</h1>
    <div v-if="scenarioNode.resolved">
            <p class="resolved-text"> <i class="bi bi-check-lg"></i> Enigme résolue</p>
        </div>
    <div class="riddle-section">
        <div   v-html="$sanitize(step.text)"></div>
        <div v-for="(clue, index) in step.clues" v-bind:key="clue.id">
                <div class="button-general-div"><button class="btn btn-secondary btn-sm" @click="showClue(clue)"><i
                            class="bi bi-search"></i> Indice #{{ index + 1 }}</button></div>
            </div>
    </div>


    <div v-if="step.has_answer">
        <div v-if="!scenarioNode.resolved">

            <form @submit="submitAnswer" class = "reponse-section">
                <div class="form-group reponse-input-container">
                    <!-- <label for="answer">Je réponds : </label> -->
                    <input id="answer" type="text" class="form-control small-input reponse-input"
                        v-model="submittedAnswer.answer" required>
                </div>
                <div class="reponse-button-container">
                    <button type="submit" class="btn btn-dark reponse-button"><i class="bi bi-send"></i></button>
                </div>
            </form>

            
            <clue-modal :clueId="selectedClueId" v-if="isClueModalEnabled" @clue-read="disableClueModal"></clue-modal>
            <success-modal :unlockedNodes="nextNodes" v-if="isRightAnswer"
                @message-read="disableSuccessModal"></success-modal>
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
                game_name:''
            },
            submittedAnswer: {
                answer: ''
            },
            isClueModalEnabled: false,
            selectedClueId: '',
            isRightAnswer: false,
            nextNodes: [],
            scenarioNode: {
                id: '',
                step: '',
                scenario: '',
                scenario_slug: '',
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
                    this.$store.commit('setCurrentPlayedGameName', this.step.game_name)
                    document.title = `${this.step.title} - ${this.step.game_name}`
                }, (error) => {
                    console.log(error)
                }
                )

        },
        getNodeData() {
            console.log(atob("cG91dGNob3V6YmVraXN0YW4="));
            axios.get("play/scenario_node/" + this.scenarioNodeId + "/")
                .then(response => {
                    this.scenarioNode = response.data;
                    this.getStepData()
                    //retreive node status
                    if (this.$store.state.unlockedNodes.filter(x => x.id === this.scenarioNode.id)[0]) {
                        this.scenarioNode.resolved = this.$store.state.unlockedNodes.filter(x => x.id === this.scenarioNode.id)[0].resolved
                    }
                    this.$store.commit('setNodeRead', this.scenarioNode)
                    this.$store.commit('setCurrentPlayedScenarioId', this.scenarioNode.scenario_slug)
                }, (error) => {
                    console.log(error)
                }
                )
        },
        submitAnswer(e) {
            e.preventDefault()
            axios.post('play/scenario_node/answer/' + this.scenarioNodeId + "/", this.submittedAnswer).then((response) => {
                if (response.data.message == false) {
                    this.submittedAnswer.answer = '';
                    window.alert("Ce n'est pas la bonne réponse")

                } else {
                    this.submittedAnswer.answer = '';
                    this.nextNodes = response.data
                    this.nextNodes.forEach((node) => {
                        node.new = true
                        node.info = false,
                            node.resolved = false,
                            this.$store.commit('unlockNode', node)
                    });
                    this.isRightAnswer = true;
                }
            }).catch((error) => {
                console.error("Error during form submission:", error);
            });
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
            for (var i = 0; i < this.$store.state.unlockedNodes.length; i++) {
                if (this.$store.state.unlockedNodes[i].id == nodeId) {
                    return true
                }
            }
            this.$router.push({ name: 'ErrorView' })
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
            this.getNodeData()
        }
    }
}
</script>