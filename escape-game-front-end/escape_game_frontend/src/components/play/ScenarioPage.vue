<template>
<h1>{{ game.name }}</h1>
<p>{{ game.description }}</p>
<p>Scénario : {{ scenario.name }}- id {{ scenario.id }}</p>
<button @click="startGame">C'est parti !</button>
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
            axios.get("play/scenario/"+ this.scenarioId + "/") //dans le back faire une version de ce get qui renvoie pas toutes les infos ?
                .then(response => {
                    this.scenario = response.data;
                    console.log(response)
                    this.getGameData();
                    // this.$store.commit('unlockNode', this.scenario.firstNode) // marche pas ici... il faudrait le faire qu'une fois au démarrage...

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
            this.$router.push({ name: 'StepPage', params: { scenarioNodeId: this.scenario.first_node.id }})
        }
    },
    created(){
        this.getData()
    }

}

</script>