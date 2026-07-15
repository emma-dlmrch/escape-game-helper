<template>
    <div :class="currentTheme ? `theme-${currentTheme}`:'default'">
      <PlayNav />
      
      <section class="home-section">
        <router-view />
      </section>
    </div>
</template>

<script>
import PlayNav from './PlayNav.vue';

export default {
  name: 'PlayView',
  components: {
    PlayNav
  },
  computed: {
    currentTheme() {
      return this.$store.state.currentPlayedGameTheme
    },
  },
  beforeCreate(){
    
    // this.$store.commit('initializeStore')
    
  },
}
</script>