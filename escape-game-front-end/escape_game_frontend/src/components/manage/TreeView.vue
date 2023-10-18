<template>
    <div class="tree">
      <ul>
          <!-- <tree-node :treeData="data" :gameId="gameId" :scenarioId="scenarioId" @create-new-node="transmitCreateNodeEvent"/> -->
          <tree-node :treeData="data" @create-node="transmitCreateNodeEvent" @update-node="transmitUpdateNodeEvent"/>

      </ul>
    </div>
  </template>
  
  <script>
  import TreeNode from "./TreeNode.vue";
  
  export default {
    props: ["data"],
    emits: ['create-node', 'update-node'],
    components: {
      TreeNode,
    },
    methods: {
      transmitCreateNodeEvent(nodeId){
        this.$emit('create-node', nodeId)
      },
      transmitUpdateNodeEvent(nodeId){
        this.$emit('update-node', nodeId)
      },
    }
  };
  </script>