<template>
  <div>
    <h1>Wyszukaj miejsca podróży</h1>
    <input v-model="searchQuery" placeholder="Wpisz nazwę miejsca" />
    <button @click="searchPlaces">Szukaj</button>

    <div v-if="places.length">
      <h2>Wyniki wyszukiwania:</h2>
      <PlaceCard v-for="place in places" :key="place.id" :place="place" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import PlaceCard from '../components/PlaceCard.vue';

export default {
  components: { PlaceCard },
  data() {
    return {
      searchQuery: '',
      places: [],
    };
  },
  methods: {
    async searchPlaces() {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/places/?search=${this.searchQuery}`
      );
      this.places = response.data;
    },
  },
};
</script>
