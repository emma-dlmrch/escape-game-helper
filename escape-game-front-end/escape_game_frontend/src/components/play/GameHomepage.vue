<template>
    <h1>{{ step.title }}</h1>
    <p>{{ step.text }}</p>
    <form @submit="sendAnswer">
        <div class="form-group">
            <label for="answer">Je réponds : </label>
            <input id="answer" type="text" class="form-control" v-model="answer">
        </div>
        <div>
            <button type="submit" class="btn btn-dark">Je tente !</button>
        </div>
    </form>

    <div v-for="clue in clues" v-bind:key="clue.id">
        <button class="btn btn-dark" @click="showClue(clue.id)">Indice caché</button>
    </div>
    <clue-modal :clueId="selectedClueId" v-if="isClueModalEnabled" @clue-read="disableClueModal"></clue-modal>
</template>

<script>
import axios from 'axios';
import ClueModal from './ClueModal.vue';

export default {
    name:'GameHomepage',
    components: {
        ClueModal
    },
    data(){
        return {
            step: {
                title:'',
                text:''
            },
            answer:'',
            clues: [],
            isClueModalEnabled: false,
            selectedClueId: ''

        }
    },
    methods: {
        getStepData() {
            axios.get("step/1/")
                .then(response => {
                    this.step = response.data;
                    this.clues = response.data.clues
                    console.log(response)
                }, (error) => {
                    console.log(error)
                }
                )

        },
        sendAnswer(){
            console.log("NOUS ENVERRONS CETTE REPONSE : " + this.answer)
        },

        showClue(clueId){
            this.selectedClueId = clueId
            this.isClueModalEnabled = true
        },

        disableClueModal(){
            this.isClueModalEnabled = false
        },
    },
    created(){
        this.getStepData()
    }
}
</script>