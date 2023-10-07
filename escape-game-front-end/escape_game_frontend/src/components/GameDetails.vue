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
            axios.get("game/"+ this.$store.state.gameId )
            .then(response => {
                this.game = response.data;
            }, (error) => {console.log(error)}
            )
            // try {
            //     const response = await axios.get("game/"+ this.$store.state.gameId,
            //     { 
            //         headers: {
            //             'Content-Type':'multipart/form-data'
            //         }
            //     })
            //     this.game = response.data
            // } catch (error) {
            //     console.log(error);
            // }
        },
    },

    created() {
    //fetch tasks on page load
        this.getGameData();
    },
}
</script>