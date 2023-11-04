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
       @create-node="transmitCreateNodeEvent" @update-node="transmitUpdateNodeEvent" @delete-node="transmitDeleteNodeEvent"/>
    </li>
  </ul>
</template>

<script>

export default {
  name: "TreeNode",
  props: ["treeData"],
  emits: ['create-node','update-node', 'delete-node'],
  data() {
    return {
    }
  },
  methods: {
    createNode(parentNodeId){
      this.$emit('create-node', parentNodeId)
    },
    transmitCreateNodeEvent(parentNodeId){
      this.$emit('create-node', parentNodeId)
    },

    updateNode(nodeId) {
      this.$emit('update-node', nodeId)
    },
    transmitUpdateNodeEvent(nodeId){
      this.$emit('update-node', nodeId)
    },

    deleteNode(nodeId) {
      this.$emit('delete-node', nodeId)
    },
    transmitDeleteNodeEvent(nodeId){
      this.$emit('delete-node', nodeId)
    },
    
  },



  created() {
  }
}
</script>