<template>
    <h1>Consulter mes informations</h1>
    <p>Il n'est pas encore possible de réinitialiser son mot de passe</p>
    <form>
        <div class="form-group">
            <label>Nom d'utilisateur</label>
            <input type="text" id="disabledInput" class="form-control" v-bind:placeholder="user.username" disabled>
        </div>
        <div class="form-group">
            <label>Adresse mail</label>
            <input type="email" id="disabledInput" class="form-control" v-bind:placeholder="user.email" disabled>
        </div>
    </form>
</template>

<script>
import axios from 'axios';

export default {
    name: 'UpdateAccount',
    data() {
        return {
            user: {
                username: '',
                password: '',
                email: '',
            },
            userId: this.$store.state.userId,
        };
    },

    computed: {
    },

    methods: {
        submitForm() {
            console.log('il faut écrire cette fonction dans le backend')
        },

        getUserData() {
            axios.get("user/" + this.userId)
                .then(response => {
                    console.log(response.data)
                    this.user = response.data
                    console.log(this.user.username)
                }, (error) => { console.log(error) }
                )
        }
    },

    created() {
        this.getUserData();
    }
}
</script>