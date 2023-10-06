<template>
    <div>
        <h1>S'inscrire</h1>
    </div>
    <!-- prvents stops the page to refresh -->
    <form @submit.prevent="submitForm">
        <label for="username">Pseudo</label>
        <input type="text" name ="username" v-model="username">
        <label for="email">Email</label>
        <input type="email" name ="email" v-model="email">
        <label for="password">Mot de passe</label>
        <input type="password" name="password" v-model ="password">
        <button type="submit">S'inscrire</button>
    </form>
</template>

<script>
import axios from 'axios';

export default {
    name: 'SignUp',
    data(){
        return {
            email:'',
            username:'',
            password:'',
        }
    },
    methods:{
        submitForm(){
            let formData = {
                username: this.username,
                password: this.password,
                email: this.email
            }

            axios
                .post('signup/', formData)
                .then(response => {
                    this.$router.push('/login')
                    console.log(response)
                })
                .catch(error => {console.log(error)})
        }
    }

}
</script>