<template>
    <div>
        <h1>Se connecter</h1>
        <form @submit.prevent="submitForm">
            <div class="form-group">
                <label for="inputUsername">Nom d'utilisateur</label>
                <input type="text" v-model="username" class="form-control" id="inputUsername" placeholder="Ton p'tit nom">
            </div>
            <div class="form-group">
                <label for="inputPassword">Mot de passe</label>
                <input type="password" v-model="password" class="form-control" id="inputPassword"
                    placeholder="Ton p'tit mot d'passe">
                <small id="emailHelp" v-if="error.code === 'ERR_BAD_REQUEST'" class="form-text text-muted">Les identifiants
                    entrés sont invalides</small>
                <small id="emailHelp" v-if="error.code === 'ERR_NETWORK'" class="form-text text-muted">Oops, le web service
                    n'est pas accessible</small>
            </div>
            <button type="submit" class="btn btn-primary">Se connecter</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from "jwt-decode"

export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            error: '',
        }
    },
    methods: {
        submitForm() {
            const formData = {
                username: this.username,
                password: this.password
            }

            axios
                .post('token/', formData)
                .then(response => {
                    const token = response.data.access
                    this.$store.commit('setToken', token)
                    axios.defaults.headers.common['Authorization'] = "Bearer " + token
                    const userId = jwt_decode(token).user_id
                    this.$store.commit('setUserId', userId)
                    this.$router.push('games')
                })
                .catch(error => {
                    console.log(error)
                    this.error = error
                })
        }
    }
}
</script>