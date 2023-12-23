<template>
    <NavBar />

    <div class="welcome-page">
        <div class="header-div">
            <h1>À propos de ce site</h1>
        </div>
        <h2>C'est quoi ?</h2>
        <p>Il s'agit d'un outil qui permet d'aider à concevoir des jeux de pistes sous toutes leurs formes.
            Concrètement, en tant que créateur.ice de jeux, tu pourras écrire des étapes de jeux et des énigmes, ainsi que les
            organiser dans l'ordre que tu souhaites. Les joueurs et joueuses auront accès à une interface simple sur laquelle entrer
            les réponses aux différentes énigmes qui vont leur être posées.</p>
        <h2>Fontionnalités</h2>
        <h3>Les étapes</h3>
        <p>
            Tu peux définir une étape grâce à son titre, son texte, et éventuellement sa réponse attendue. Si
            aucune réponse n'est attendue,
            l'interface de jeu ne demandera pas de réponse aux joueurs. Pour l'instant, il n'est pas possible
            d'effectuer de mise en forme,
            d'associer des médias, ou de permettre plusieurs réponses possibles. Il est toutefois possible
            d'ajouter des indices pour aider
            les joueurs bloqués à se dépatouiller.
        </p>
        <h3> Les scénarios</h3>

        <p>
            Si tu souhaites par exemple que tes joueuses et joueurs se répartissent en groupes n'effectuant pas les étapes
            de jeux dans le même ordre,
            sache qu'il est possible de créer plusieurs scénarios pour un jeu d'énigmes. Tu pourras alors donner
            un code différent à tes
            groupes pour qu'ils ne suivent pas le même ordre.
        </p>


        <div class = "button-general-div"><router-link :to="{ name: 'GameHomepage' }">
            <button type="button" class="btn btn-dark btn-lg">Je veux jouer <i class="bi bi-controller"></i></button>
        </router-link> </div>
       <div class = "button-general-div"> <router-link :to="{ name: 'GameList' }">
            <button type="button" class="btn btn-dark btn-lg">Je veux créer mes jeux <i class="bi bi-tools"></i></button>
        </router-link> </div>

    </div>
</template>

<script>
import NavBar from '../manage/NavBar.vue'
export default {
    name: 'AboutView',
    components: { NavBar },
    methods: {

    }
}
</script>
