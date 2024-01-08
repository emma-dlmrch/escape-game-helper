<template>
  <div class="sidebar">
    <div class="logo-details">
      <i class="bx icon"></i>

      <div class="logo_name">
        <router-link :to="{ name: 'ScenarioPage', params: { scenarioId: currentScenario }}" style="text-decoration: none; color: inherit;">
          <div class="game_name">{{ navbarTitle }}</div>
        </router-link>
      </div>
      <i class="bx bx-menu" id="btn"></i>
    </div>
    <ul class="nav-list">
      <li>
        <a>
        <i class="bx bi bi-alarm-fill"></i>
          <span class="links_name" style="color: #fff">{{ playtime }}</span>
          <span class="tooltip">{{ playtime }}</span>
        </a>
      </li>

      <li v-for="node in nodes" v-bind:key="node.id">
        <router-link :to="{ name: 'StepPage', params: { 'scenarioNodeId': node.id } }" v-if="node.scenario_slug == currentScenario">

          <i v-if="node.new" class="bx bi bi-exclamation-square-fill"></i>
          <i v-else-if="node.info" class="bx bi bi-info-square"></i>
          <i v-else-if="node.resolved" class="bx bi bi-check-square"></i>
          <i v-else class="bx bi bi-question-square"></i>
          <span class="links_name">{{ node.label }}</span>
          <span class="tooltip">{{ node.label }}</span>
        </router-link>
      </li>   
      
      <li>
        <router-link :to="{name: 'WelcomePage'}">
        <i class="bx bi bi-house-fill"></i>
          <span class="links_name">Accueil</span>
          <span class="tooltip">Accueil</span>
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
      return this.$store.state.unlockedNodes
    },
    currentScenario() {
      return this.$store.state.currentPlayedScenarioId
    },
    currentGame(){
      return this.$store.state.currentPlayedGameName
    },
    navbarTitle() {
      const currentName = this.$store.state.currentPlayedGameName
      if(currentName.length > 10 && !currentName.includes(" ")){
        return currentName.slice(0, 10)+"..."
      } else if(currentName.length > 30) {
        const pieces = currentName.split(/[\s-,.]/)
        let output = ""
        pieces.some((p) => {
          const newOutput = output + p + currentName[(output+p).length]
          if(newOutput.length < 30){
            output = newOutput;
            return false
          } else {
            return true;
          }
        })
        return output.trim()+"..."
      }
      return currentName;
    },
    playtime() {
      return new Date(this.$store.state.playSeconds * 1000).toISOString().slice(11, 19);
    }
  },
  data() {
    return {
      interval: null,
      time: null
    }
  },
  beforeUnmount() {
    // prevent memory leak
    clearInterval(this.interval)
  },
  created() {
    // update the time every second
    this.interval = setInterval(() => {
      this.$store.state.playSeconds += 1;
      this.$store.commit('setPlaySeconds', this.$store.state.playSeconds);
      this.time = Intl.DateTimeFormat(navigator.language, {
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric'
      }).format()
    }, 1000)
  },
  mounted() {
    let sidebar = document.querySelector(".sidebar");
    let mainSection = document.querySelector(".home-section");
    let closeBtn = document.querySelector("#btn");

    closeBtn.addEventListener("click", () => {
      sidebar.classList.toggle("open");
      mainSection.classList.toggle("navbar-open");
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
