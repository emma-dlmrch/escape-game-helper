<template>
<h1>{{ game.name }}</h1>
<p>{{ game.description }}</p>
<p>Scénario : {{ scenario.name }}- id {{ scenario.id }}</p>
<button class="btn btn-dark" @click="startGame">C'est parti !</button>
<!-- <router-view/> -->

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
                    console.log(response)
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
                    console.log(response)

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
        }
    },
    created(){   
        this.getData()
        this.$store.commit('setCurrentPlayedScenarioId', this.scenarioId)
    }

}

</script>