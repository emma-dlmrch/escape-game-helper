<template>
<h1>{{ clue.title }}</h1>
    <form @submit.prevent="updateClue">
        <div class="form-group">
            <label for="title">Titre</label>
            <input id="title" type="text" class="form-control" v-model.lazy="clue.title">
        </div>
        <div class="form-group">
            <label for="text">Texte</label>
            <textarea  id="text" class="form-control" v-model="clue.text" rows="5"></textarea>
        </div>
        <div>
            <button type="submit" class="btn btn-dark">Mettre à jour l'indice</button>
            <button type="button" class="btn btn-light" @click="cancel">Annuler</button>
        </div>
    </form>

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
            }
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
                    console.log(response);
                    this.$router.push({ name: 'StepDetails', params: { gameId: this.gameId, stepId: this.stepId } })
                },
                    (error) => { console.log("Error", error) });

        },
        cancel(){
            this.$router.push({ name: 'StepDetails', params: { gameId: this.gameId, stepId: this.stepId } })
        }
    },
    created(){
        this.getClueData()
    }
}
</script>