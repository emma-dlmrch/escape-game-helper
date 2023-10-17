<template>
  <ul>
    <li :key="idx" v-for="(item, idx) in treeData">
      <span class="tf-nc">
        <div>{{ item.label }}</div>
        <div class="tree-buttons">
          <div><i @click="createNode(item.id)" class="bi bi-plus-square"></i></div>
          <div><i @click="updateNode(item.id)" class="bi bi-pencil"></i></div>
          <div><i @click="deleteNode(item.id)" class="bi bi-trash"></i></div>
        </div>
      </span>
      <tree-node :treeData="item.children" :gameId="gameId" :scenarioId="scenarioId" />
    </li>
  </ul>
</template>

<script>
import axios from 'axios';
// import LogIn from './LogIn.vue';

export default {
  name: "TreeNode",
  props: ["treeData", "gameId", "scenarioId"],
  data() {
    return {
      // modalShow: false,
    }
  },
  methods: {
    deleteNode(nodeId) {
      axios.delete('scenario_node/' + nodeId + "/")
        .then(response => {
          console.log(response);
          // this.getData();
          this.$router.go(0);
        },
          (error) => { console.log("Error", error) });
    },

    updateNode(nodeId) {
      this.$router.push({ name: 'UpdateNode', params: { gameId: this.gameId, scenarioId: this.scenarioId, nodeId: nodeId } })
    },

    createNode(parentNodeId){
      this.$router.push({ name: 'CreateNode', params: { gameId: this.gameId, scenarioId: this.scenarioId, parentNodeId: parentNodeId } })
    }
  },



  created() {
  }
}
</script>