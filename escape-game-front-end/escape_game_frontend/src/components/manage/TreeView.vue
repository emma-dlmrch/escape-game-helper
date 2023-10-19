<template>
    <div class="tree">
      <ul>
          <tree-node :treeData="data" @create-node="transmitCreateNodeEvent" @update-node="transmitUpdateNodeEvent" @delete-node="transmitDeleteNodeEvent"/>

      </ul>
    </div>
  </template>
  
  <script>
  import TreeNode from "./TreeNode.vue";
  
  export default {
    props: ["data"],
    emits: ['create-node', 'update-node', 'delete-node'],
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
      transmitDeleteNodeEvent(nodeId){
        this.$emit('delete-node', nodeId)
      },
    }
  };
  </script>