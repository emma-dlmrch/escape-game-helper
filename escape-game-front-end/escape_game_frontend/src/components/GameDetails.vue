<template>
<h1>Voici le jeu {{ game.name }}</h1>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            game: {
                name: '',
                description: '',
            }
        }

    },
    computed: {
        gameId(){
            return this.$store.state.gameId
        },
    },

    methods: {
        getGameData() {
            axios.get("game/"+ this.$store.state.gameId + "/")
            .then(response => {
                this.game = response.data;
            }, (error) => {
                console.log(error)
            }
            )
        },
    },

    created() {
    //fetch tasks on page load
        this.getGameData();
    },
}
</script>