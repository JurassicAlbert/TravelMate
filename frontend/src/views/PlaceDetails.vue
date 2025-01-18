<template>
  <div>
    <h1>{{ place.name }}</h1>
    <p>{{ place.description }}</p>
    <h3>Reviews:</h3>
    <ul>
      <li v-for="review in place.reviews" :key="review.id">{{ review.text }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['id'],
  data() {
    return {
      place: {}
    };
  },
  async created() {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/travel-locations/${this.id}/`);
      this.place = response.data;
    } catch (error) {
      console.error(error);
    }
  }
};
</script>

<style scoped>
/* Stylizowanie szczegółów miejsca */
</style>
