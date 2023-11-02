<template>
    <div>
        <h1>Créer un compte</h1>
    </div>
    <form @submit.prevent="submitForm">
        <div class="form-group">
            <label for="inputUsername">Nom d'utilisateur : </label>
            <input type="text" v-model="username" class="form-control" id="inputUsername" placeholder="Ton p'tit nom"  @click="disableAccountExistingMessage" required>
        </div>
        <div class="form-group">
            <label for="inputEmail">Adresse e-mail : </label>
            <input type="email" v-model="email" class="form-control" id="inputEmail" aria-describedby="emailHelp"
                placeholder="Ton p'tit mail"  @click="disableAccountExistingMessage" required>
                <small id="emailHelp" v-if="error.code === 'ERR_BAD_REQUEST'" class="form-text text-muted">Oops, avez-vous déjà un compte ?</small>
        </div>
        <div class="form-group">
            <label for="inputPassword">Mot de passe : </label>
            <input type="password" v-model="password" class="form-control" id="inputPassword" placeholder="Ton p'tit mot d'passe" required>

        </div>
        <div>
            <label for="captcha">Captcha : </label>
            <re-captcha @value-entered="checkCaptchaValidity" @click="disableCaptchaErrorMessage"></re-captcha>
            <small v-if="captchaErrorMessage">Captcha invalide !</small>
            
        </div>
        <button type="submit" class="btn btn-dark btn-sm"><i class="bi bi-send"></i> S'inscrire</button>
    </form>
</template>

<script>
import axios from 'axios';
import ReCaptcha from './ReCaptcha.vue'

export default {
    name: 'SignUp',
    components: {
        ReCaptcha,
    },
    data() {
        return {
            email: '',
            username: '',
            password: '',
            error:'',
            isCaptchaValid:'',
            captchaErrorMessage: false
        }
    },
    methods: {
        submitForm() {
            if (this.isCaptchaValid) {
            let formData = {
                username: this.username,
                password: this.password,
                email: this.email
            }

            axios
                .post('signup/', formData)
                .then(response => {
                    if (response.status == 200) {
                        alert("Ton compte a été créé, tu peux desormais te connecter !")
                        this.$router.push({name :'LogIn'})
                    }
                })
                .catch(error => {
                    this.error = error
                    console.log(error) })
            } else {
                this.captchaErrorMessage = true
            }
        },
        checkCaptchaValidity(isValid){
            if (isValid) {
                this.isCaptchaValid = true;
            } else {
                this.isCaptchaValid = false;
            }
        },
        disableCaptchaErrorMessage(){
            this.captchaErrorMessage = false
        },
        disableAccountExistingMessage(){
            this.error=''
        }
    }

}
</script>