<template>
    <div>
        <button @click="createGame">Creons un jeu lol</button>
    </div>
    <div>Maintenans testons une personnalisation</div>

    <form @submit.prevent="createGameFromForm">
        <input v-model="newGame.name">
        <textarea v-model="newGame.description"></textarea>
        <button type="submit">Submit</button>
    </form>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            newGame: {
                name: '',
                description: '',
                author: '1',
            }
        }

    },
    methods: {
        createGame() {
            axios.post('game/', {
                author: '1',
                name: 'un titre',
                description: 'une descrition',
            })
                .then(response => {
                    console.log(response.data.id)
                }, (error) => { console.log(error) });
        },

        createGameFromForm() {
            try {
                axios.post('game/', this.newGame).then((response) => {
                    console.log("Patate")
                    console.log(response)
                });
                console.log("COUCOU")
            } catch (error) {
                console.error("Error during form submission:", error);
            }

        },

    }
}


</script>