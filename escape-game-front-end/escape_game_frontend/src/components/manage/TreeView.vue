<template>
    <div class="tree">
      <ul>
          <tree-node :treeData="data" :gameId="gameId" :scenarioId="scenarioId" />
      </ul>
    </div>
  </template>
  
  <script>
  import TreeNode from "./TreeNode.vue";
  
  export default {
    props: ["data", "gameId", "scenarioId"],
    components: {
      TreeNode,
    }
  };
  </script>