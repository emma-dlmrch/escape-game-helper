<template>
  <router-view />
</template>

<script>
export default {
  name: 'App',

  data() {
    return {
    }
  },

  computed: {
    authenticated() {
      return this.$store.state.isAuthenticated
    }
  },

  beforeCreate() {
    this.$store.commit('initializeStore')
  },
}
</script>

<style></style>
