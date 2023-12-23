<template>
    <NavBar />

    <div class="welcome-page">
        <div class="header-div">
            <h1>Bienvenue</h1>
        </div>
        <p>Pour jouer, c'est par ici !</p>
        <div class = "button-general-div"><router-link :to="{ name: 'GameHomepage' }">
            <button type="button" class="btn btn-dark btn-lg">Je veux jouer <i class="bi bi-controller"></i></button>
        </router-link> </div>
    </div>
</template>

<script>
import NavBar from '../manage/NavBar.vue'
export default {
    name: 'WelcomePage',
    components: { NavBar },
    methods: {

    }
}
</script>
