<template>
  <ul>
    <li :key="idx" v-for="(item, idx) in treeData">
      <span class="tf-nc">{{ item.label }} </span>
      <tree-node :treeData="item.children" />
    </li>
  </ul>
</template>

<script>
export default {
  name: "TreeNode",
  props: ["treeData"],
}
</script>