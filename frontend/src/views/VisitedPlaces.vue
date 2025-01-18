<template>
  <div>
    <h1>Visited Places</h1>
    <ul>
      <li v-for="place in visitedPlaces" :key="place.id">
        <router-link :to="'/place/' + place.id">{{ place.name }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      visitedPlaces: []
    };
  },
  async created() {
    try {
      const response = await axios.get('http://127.0.0.1:8000/travel-history/');
      this.visitedPlaces = response.data;
    } catch (error) {
      console.error(error);
    }
  }
};
</script>

<style scoped>
/* Stylizowanie widoku odwiedzonych miejsc */
</style>
