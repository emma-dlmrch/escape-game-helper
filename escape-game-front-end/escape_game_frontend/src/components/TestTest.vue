<template>
    <div>
      <div v-for="post in posts" v-bind:key="post.id">
        <h2>{{ post.title }}</h2>
        <p>{{ post.body }}</p>
      </div>
    </div>
  </template>

<script>
import axios from 'axios';

export default {
  name: 'TestTest',
  data() {
    return {
      posts: [],
    };
  },

  methods: {
    async getData() {
      try {
        const response = await axios.get(
          "http://jsonplaceholder.typicode.com/posts"
        );
        // JSON responses are automatically parsed.
        this.posts = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },

  created() {
    //fetch tasks on page load
    this.getData();
  },
};
</script>