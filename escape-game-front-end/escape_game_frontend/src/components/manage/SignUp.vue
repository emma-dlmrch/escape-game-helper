<template>
    <div>
        <h1>Créer un compte</h1>
    </div>
    <form @submit.prevent="submitForm">
        <div class="form-group">
            <label for="inputUsername">Nom d'utilisateur</label>
            <input type="text" v-model="username" class="form-control" id="inputUsername" placeholder="Ton p'tit nom">
        </div>
        <div class="form-group">
            <label for="inputEmail">Adresse e-mail</label>
            <input type="email" v-model="email" class="form-control" id="inputEmail" aria-describedby="emailHelp"
                placeholder="Ton p'tit mail">
            <!-- <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small> -->
        </div>
        <div class="form-group">
            <label for="inputPassword">Mot de passe</label>
            <input type="password" v-model="password" class="form-control" id="inputPassword" placeholder="Ton p'tit mot d'passe">
            <small id="emailHelp" v-if="error.code === 'ERR_BAD_REQUEST'" class="form-text text-muted">Oops, avez-vous déjà un compte ?</small>

        </div>
        <button type="submit" class="btn btn-primary">S'inscrire</button>
    </form>
</template>

<script>
import axios from 'axios';

export default {
    name: 'SignUp',
    data() {
        return {
            email: '',
            username: '',
            password: '',
            error:'',
        }
    },
    methods: {
        submitForm() {
            let formData = {
                username: this.username,
                password: this.password,
                email: this.email
            }

            axios
                .post('signup/', formData)
                .then(response => {
                    this.$router.push({name :'LogIn'})
                    console.log(response)
                })
                .catch(error => {
                    this.error = error
                    console.log(error) })
        }
    }

}
</script>