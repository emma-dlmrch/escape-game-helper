<template>
    <div class="modal fade show background-modal" @click="goBack">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLiveLabel">Créer un noeud</h5>
                    <button type="button" class="close-btn close" @click="goBack" aria-label="Close">
                        <span aria-hidden="true">×</span>
                    </button>
                </div>
                <form @submit.prevent="createNewNode">
                    <div class="modal-body">
                        <p>Quelle étape souhaitez-vous voir apparaître après <b>{{ parentNode.stepLabel }}</b> ?</p>
                        <div class="form-group">
                            <label>Etape</label>
                            <select v-model="newNode.step" class="form-control form-control-sm" required>
                                <option disabled selected value> -- choisis une étape -- </option>
                                <option v-for="step in stepList" v-bind:key="step.id" :value="step.id">{{ step.title }}
                                </option>
                            </select>
                        </div>
                        <!-- <button type="submit" class="btn btn-dark btn-sm">OK</button> -->

                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary btn-sm close-btn" @click="goBack">Close</button>
                        <button type="submit" class="btn btn-dark btn-sm">Save changes</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CreateNode',
    props: ["parentNodeId", "gameId", "scenarioId"],
    emits: ['node-created'],
    data() {
        return {
            stepList: [],
            parentNode: {
                stepLabel: '',
            },
            newNode: {
                parent_node: '',
                step: '',
                scenario: ''
            },
        }
    },
    methods: {
        getStepList() {
            axios.get("game/" + this.gameId + "/")
                .then(response => {
                    this.stepList = response.data.steps
                }, (error) => {
                    console.log(error)
                }
                )
        },
        getParentNodeData() {
            axios.get("scenario_node/" + this.parentNodeId + "/")
                .then(response => {
                    // this.parentNode.step = response.data.step
                    this.parentNode.stepLabel = response.data.step_title
                }, (error) => {
                    console.log(error)
                }
                )
        },

        createNewNode() {
            try {
                this.newNode.scenario = this.scenarioId
                this.newNode.parent_node = this.parentNodeId
                axios.post('scenario_node/', this.newNode).then((response) => {
                    console.log(response)
                    // this.$router.push({ name: 'ScenarioDetails', params: { gameid: this.gameId, scenarioId: this.scenarioId } })
                    this.$emit('node-created')
                });
            } catch (error) {
                console.error("Error during form submission:", error);
            }
        },
        goBack(e){
            // this.$emit('node-created')
            if(e.target.className.includes("background-modal")||e.target.className.includes("close-btn")){
                this.$emit('node-created');
            }
        },
        getData() {
            this.getParentNodeData()
            this.getStepList()
        }

    },
    created() {
        this.getData()
    }
}
</script>