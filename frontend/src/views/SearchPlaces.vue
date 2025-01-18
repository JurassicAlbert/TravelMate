<template>
  <div>
    <h1>Search Places</h1>
    <input v-model="query" placeholder="Search for a place" @input="searchPlaces" />
    <ul>
      <li v-for="place in places" :key="place.id">
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
      query: '',
      places: []
    };
  },
  methods: {
    async searchPlaces() {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/travel-locations/?search=${this.query}`);
        this.places = response.data;
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>

<style scoped>
/* Stylizowanie widoku wyszukiwania miejsc */
</style>
