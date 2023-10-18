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
      <tree-node :treeData="item.children" :item="item"
       @create-node="transmitCreateNodeEvent" @update-node="transmitUpdateNodeEvent"/>
    </li>
  </ul>
</template>

<script>
import axios from 'axios';

export default {
  name: "TreeNode",
  props: ["treeData"],
  emits: ['create-node','update-node'],
  data() {
    return {
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
    createNode(parentNodeId){
      // this.$router.push({ name: 'CreateNode', params: { gameId: this.gameId, scenarioId: this.scenarioId, parentNodeId: parentNodeId } })
      this.$emit('create-node', parentNodeId)
    },
    transmitCreateNodeEvent(parentNodeId){
      this.$emit('create-node', parentNodeId)
    },

    updateNode(nodeId) {
      // this.$router.push({ name: 'UpdateNode', params: { gameId: this.gameId, scenarioId: this.scenarioId, nodeId: nodeId } })
      this.$emit('update-node', nodeId)
    },
    transmitUpdateNodeEvent(nodeId){
      this.$emit('update-node', nodeId)
    },
    
  },



  created() {
  }
}
</script>