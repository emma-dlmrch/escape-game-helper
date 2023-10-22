<template>
  <!-- ici il y aura la liste des noeuds (ou étapes??? à définir) débloqués
    Représentés avec des badges new pour que dans le cas où plusieurs noeuds sont débloqués, le joueur s'en rende compte -->
  <!-- <div class="side-navbar" id="nav-bar">
    <nav class="nav">
      <div>Etapes débloquées : </div>
      <div v-for="node in nodes" v-bind:key="node.id"> -
        <router-link :to="{ name: 'StepPage', params: { 'scenarioNodeId': node.id } }">{{ node.id }}</router-link>
        -
      </div>
    </nav>
  </div> -->

  <div class="sidebar closed">
    <div class="logo-details"><i class="icon"></i>
      <div class="logo_name"><a href="/go">LOGO</a></div><i class="bx bx-menu" id="btn"></i>
    </div>
    <ul class="nav-list">
      <li v-for="node in nodes" v-bind:key="node.id">
        <router-link :to="{ name: 'StepPage', params: { 'scenarioNodeId': node.id } }">
        <a href="#"><i class="element">{{ node.id }}</i><span class="links_name">{{ node.label }}</span></a><span
          class="tooltip">{{ node.label }}</span></router-link></li>
    </ul>
  </div>

</template>

<script>
// import GameHomepage from './GameHomepage.vue';
export default {
  name: 'PlayNav',
  components: {
    // GameHomepage
  },
  data() {
    return {
      nodes: this.$store.state.unlockedNodes,
    }
  },
}
</script>