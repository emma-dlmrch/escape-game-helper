<template>
    <div>
        <h1>Login</h1>
        <form @submit.prevent="submitForm">
        <label for="username">Pseudo</label>
        <input type="text" name ="username" v-model="username">
        <label for="password">Mot de passe</label>
        <input type="password" name="password" v-model ="password">
        <button type="submit">Se connecter</button>
        <p v-if="error.code ==='ERR_BAD_REQUEST'">Les identifiants entrés sont invalides</p>
        <p v-if="error.code ==='ERR_NETWORK'">Oops, le web service n'est pas accessible</p>
    </form>
    </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from "jwt-decode"

export default {
    name: 'LogIn',
    data(){
        return {
            username:'',
            password:'',
            error:'',
        }
    },
    methods:{
        submitForm(){
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