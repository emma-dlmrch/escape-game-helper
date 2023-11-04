<template>
    <!-- <PlayNav />

  <section class="home-section"> -->
    <router-view />
    <!-- </section> -->
</template>

<script>
// import PlayNav from './PlayNav.vue';

export default {
  name: 'PlayApp',
  components: {
    // PlayNav
  },
  beforeCreate(){
    
    // this.$store.commit('initializeStore')
    
  },
}
</script>