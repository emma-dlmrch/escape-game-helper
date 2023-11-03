<template>
<h1>Indice : {{ clue.title }}</h1>
    <form @submit.prevent="updateClue">
        <div class="form-group">
            <label for="title">Titre :</label>
            <input id="title" type="text" class="form-control" v-model.lazy="clue.title" @click="disableWasUpdatedMessage">
        </div>
        <div class="form-group">
            <label for="text">Texte :</label>
            <textarea  id="text" class="form-control" v-model="clue.text" rows="5" @click="disableWasUpdatedMessage"></textarea>
        </div>
        <div class="button-general-div">
            <button type="submit" class="btn btn-dark btn-sm"><i class="bi bi-pencil"></i> Enregistrer</button>
        </div>
        <small v-if ="wasUpdated" class="form-text text-muted"><i class="bi bi-check"></i> Modifications enregistrées !</small>
    </form>
    <p></p>
    <button type="button" class="btn btn-dark btn-sm" @click="cancel"><i class="bi bi-arrow-left"></i> Retour</button>
</template>

<script>
import axios from 'axios';

export default {
    name:'UpdateClue',
    data () {
        return {
            clueId: this.$route.params.clueId,
            stepId: this.$route.params.stepId,
            clue: {
                step:'',
                title:'',
                text:'',
            },
            wasUpdated : false
        }
    },
    methods: {
        getClueData() {
            axios.get("clue/" + this.clueId + "/")
                .then(response => {
                    this.clue = response.data;
                    console.log(response)
                }, (error) => {
                    console.log(error)
                }
                )

        },

        updateClue(){
            axios.put('clue/' + this.clueId + "/", this.clue)
                .then(response => {
                    if (response.status == 200) {
                        this.wasUpdated = true
                    }
                    // console.log(response);
                    // this.$router.push({ name: 'StepDetails', params: { gameId: this.gameId, stepId: this.stepId } })
                },
                    (error) => { console.log("Error", error) });

        },
        cancel(){
            this.$router.push({ name: 'StepDetails', params: { gameId: this.gameId, stepId: this.stepId } })
        },
        disableWasUpdatedMessage(){
            this.wasUpdated = false
        }
    },
    created(){
        this.getClueData()
    }
}
</script>