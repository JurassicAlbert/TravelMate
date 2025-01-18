<template>
  <div>
    <h1>Search Places</h1>
    <input v-model="query" placeholder="Search for a place" @input="searchPlaces" />
    <button @click="fetchRecommendations">Search</button> <!-- Dodany przycisk do wyszukiwania -->
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
      query: '',    // Wartość wpisana przez użytkownika w input
      places: []    // Lista miejsc do wyświetlenia
    };
  },
  methods: {
    // Metoda, która wywołuje API do uzyskania rekomendacji
    async fetchRecommendations() {
      try {
        // Adres API, który zwróci spersonalizowane rekomendacje
        const response = await axios.post('http://127.0.0.1:8000/travel-recommendations/', {
          query: this.query  // Wysyłamy zapytanie użytkownika jako payload
        });

        // Otrzymujemy rekomendacje z API i zapisujemy je w places
        this.places = response.data.recommendations || [];
      } catch (error) {
        console.error("Error fetching places:", error);
      }
    },

    // Metoda do szukania miejsc w API (np. travel-locations)
    async searchPlaces() {
      try {
        // Możesz zaimplementować metodę do wyszukiwania w travel-locations, jeśli potrzebujesz
        const response = await axios.get(`http://127.0.0.1:8000/travel-locations/?search=${this.query}`);
        this.places = response.data;
      } catch (error) {
        console.error("Error fetching places:", error);
      }
    }
  }
};
</script>

<style scoped>
/* Stylizowanie widoku wyszukiwania miejsc */
input {
  margin: 10px 0;
  padding: 10px;
  width: 300px;
}

button {
  padding: 10px 20px;
  cursor: pointer;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 10px 0;
}
</style>
