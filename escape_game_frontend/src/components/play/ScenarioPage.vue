<template>
<h1>{{ game.name }}</h1>
<p>{{ game.description }}</p>
<div class="button-general-div">
    <button class="btn btn-dark" @click="startGame"><i class="bi bi-send"></i> C'est parti !</button>
</div>
<div class="button-general-div">
<button class="btn btn-dark" @click="cancel"><i class="bi bi-arrow-left"></i> Retour</button>
</div>
</template>
<script>

import axios from 'axios'
export default {
    name:'ScenarioPage',

    data () {
        return {
            scenarioId: this.$route.params.scenarioId,
            scenario:{
                id:'',
                game:'',
                name:'',
                first_node: {
                    id:'',
                    label:'',
                    new: '',
                    resolved:'',
                    info:'' 
                }
            },
            game:{
                name:'',
                description:''
            },
        }
    },
    methods: {
        playGame(){
            this.$router.push({ name: 'ScenarioPage', params: { scenarioId: this.scenarioId }} )
        },
        getData(){
            axios.get("play/scenario/"+ this.scenarioId + "/")
                .then(response => {
                    this.scenario = response.data;
                    this.getGameData();

                }, (error) => {
                    console.log(error)
                }
                )
        },
        getGameData(){
            axios.get("play/game/"+ this.scenario.game + "/")
                .then(response => {
                    this.game = response.data;
                    this.$store.commit('setCurrentPlayedGameName', this.game.name)
                    document.title = `${this.game.name}`

                }, (error) => {
                    console.log(error)
                }
                )
        },
        startGame(){
            this.scenario.first_node.new = false
            this.scenario.first_node.resolved = false
            this.scenario.first_node.info = false
            this.$store.commit('unlockNode', this.scenario.first_node)
            this.$router.push({ name: 'StepPage', params: { scenarioNodeId: this.scenario.first_node.id }})
        },

        cancel(){
            this.$router.push({ name: 'GameHomepage'})
        }
    },
    created(){   
        this.getData()
        this.$store.commit('setCurrentPlayedScenarioId', this.scenarioId)
    }

}

</script>