<template>
    <PlayNav />

  <!-- <GameHomepage />    A supprimer a terme -> géré par router path, on rentrera le nom du jeu pour y jouer -->
    <router-view />
</template>

<script>
// import GameHomepage from './GameHomepage.vue';
import PlayNav from './PlayNav.vue';

export default {
  name: 'PlayApp',
  components: {
    // GameHomepage,
    PlayNav
  },
  beforeCreate(){
    
    // this.$store.commit('initializeStore')
    
  },
}
</script>