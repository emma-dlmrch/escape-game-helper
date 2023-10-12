<template>
    <h1>{{ step.title }}</h1>
    <form>
        <div class="form-group">
            <label>Nom de l'étape</label>
            <input type="text" class="form-control" v-model="step.title">
        </div>
        <div class="form-group">
            <label>Texte</label>
            <textarea class="form-control" v-model="step.text" rows="5"></textarea>
        </div>
        <div class="form-group">
            <label>Réponse attendue</label>
            <input type="text"  class="form-control" v-model="step.answer">
        </div>
        <div>
            <button type="submit" class="btn btn-primary">Mettre à jour l'étape</button>
        </div>
    </form>
</template>

<script>
import axios from 'axios';
export default {
    name: 'GameDetails',
    data() {
        return {
            gameId: this.$route.params.gameId,
            stepId: this.$route.params.stepId,
            step: {
                title: '',
                text: '',
                answer: '',
            },
            clues: [],
        }
    },

    methods: {
        getStepData() {
            axios.get("step/" + this.stepId + "/")
                .then(response => {
                    this.step = response.data;
                    //this.clues = response.data.clue ajouter les clues dans le serializer !!
                    console.log(response)
                }, (error) => {
                    console.log(error)
                }
                )

        },
        
        modifyStep(){
            try {
                axios.put('step/', this.step).then((response) => {
                    console.log(response)
                    this.getStepData()
                });
            } catch (error) {
                console.error("Error during form submission:", error);
            }
        }


    },
    created() {
            this.getStepData();
        },
}
</script>