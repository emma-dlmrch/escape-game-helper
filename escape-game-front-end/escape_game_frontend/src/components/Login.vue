<template>
    <div>
        <h1>Login</h1>
        <form @submit.prevent="submitForm">
        <label for="username">Pseudo</label>
        <input type="text" name ="username" v-model="username">
        <label for="password">Mot de passe</label>
        <input type="password" name="password" v-model ="password">
        <button type="submit">Se connecter</button>
    </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'LogIn',
    data(){
        return {
            username:'',
            password:'',
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
                    console.log(response)
                    const token = response.data.access
                    this.$store.commit('setToken', token)
                    axios.defaults.headers.common['Authorization'] = "Bearer " + token
                    console.log(response.data.id)
                    // this.$router.push({ name: 'games', params: { userId: '123' } })
                    this.$router.push('games')
                })
                .catch(error => {console.log(error)})
        }
    }
}
</script>