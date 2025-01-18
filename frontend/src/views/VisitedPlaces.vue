<template>
  <div>
    <h1>Odwiedzone miejsca</h1>
    <div v-if="visitedPlaces.length">
      <PlaceCard v-for="place in visitedPlaces" :key="place.id" :place="place" />
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
      visitedPlaces: [],
    };
  },
  async created() {
    const response = await axios.get('http://127.0.0.1:8000/api/visited/');
    this.visitedPlaces = response.data;
  },
};
</script>
