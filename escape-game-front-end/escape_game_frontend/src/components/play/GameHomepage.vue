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
</template>

<script>
import axios from 'axios';

export default {
    name:'GameHomepage',
    data(){
        return {
            step: {
                title:'',
                text:''
            },
            answer:'',
            clues: [],
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
            console.log("Nous montrerons l'indice : " + clueId)
        }
    },
    created(){
        this.getStepData()
    }
}
</script>