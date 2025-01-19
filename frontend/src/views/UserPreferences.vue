<template>
  <div>
    <h1>User Preferences</h1>
    <p>{{ preferences }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      preferences: {}
    };
  },
  async created() {
    try {
      const response = await axios.get('http://127.0.0.1:8000/user-preferences/');
      this.preferences = response.data;
    } catch (error) {
      console.error(error);
    }
  }
};
</script>

<style scoped>
/* Stylizowanie widoku preferencji użytkownika */
</style>
