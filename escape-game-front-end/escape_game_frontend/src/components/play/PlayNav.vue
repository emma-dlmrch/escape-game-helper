<template>
  <div class="sidebar">
    <div class="logo-details">
      <i class="bx icon"></i>

      <div class="logo_name">Etapes</div><i class="bx bx-menu" id="btn"></i>
    </div>
    <ul class="nav-list">
      <li v-for="node in nodes" v-bind:key="node.id">
        <router-link :to="{ name: 'StepPage', params: { 'scenarioNodeId': node.id } }" v-if="node.scenario == currentScenario">

          <i v-if="node.new" class="bx bi bi-exclamation-square-fill"></i>
          <i v-else-if="node.info" class="bx bi bi-info-square"></i>
          <i v-else-if="node.resolved" class="bx bi bi-check-square"></i>
          <i v-else class="bx bi bi-question-square"></i>
          <span class="links_name">{{ node.label }}</span>

          <span class="tooltip">{{ node.label }}</span>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'PlayNav',
  components: {
  },
  computed: {
    nodes() {
      //tried to write a filter here instead of seeting a v-if == currentScenario above, but did not succeed
      return this.$store.state.unlockedNodes
    },
    currentScenario() {
      return this.$store.state.currentPlayedScenarioId
    }
  },
  mounted() {
    let sidebar = document.querySelector(".sidebar");
    let closeBtn = document.querySelector("#btn");

    closeBtn.addEventListener("click", () => {
      sidebar.classList.toggle("open");
      menuBtnChange();
    });

    function menuBtnChange() {
      if (sidebar.classList.contains("open")) {
        closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
      } else {
        closeBtn.classList.replace("bx-menu-alt-right", "bx-menu");
      }
    }
  }
}

</script>