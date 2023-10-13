<template>
    <div class="tree">
      <ul>
          <tree-node :treeData="data" />
      </ul>
    </div>
  </template>
  
  <script>
  import TreeNode from "./TreeNode.vue";
  
  export default {
    props: ["data"],
    components: {
      TreeNode,
    }
  };
  </script>