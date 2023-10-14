<template>
  <ul>
    <li :key="idx" v-for="(item, idx) in treeData">
      <span class="tf-nc">{{ item.label }} - <p @click="deleteNode(item.id)">X</p> - M - +</span>
      <tree-node :treeData="item.children" />
    </li>
  </ul>
</template>

<script>
import axios from 'axios';
// import LogIn from './LogIn.vue';

export default {
  name: "TreeNode",
  props: ["treeData"],
  data() {
    return {
      modalShow: false
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

  },
}
</script>