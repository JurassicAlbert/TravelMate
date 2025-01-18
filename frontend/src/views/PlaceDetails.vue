<template>
  <div>
    <h1>{{ place.name }}</h1>
    <p>{{ place.description }}</p>

    <h2>Opinie</h2>
    <ul>
      <li v-for="review in place.reviews" :key="review.id">
        <strong>{{ review.author }}:</strong> {{ review.text }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      place: null,
    };
  },
  async created() {
    const { id } = this.$route.params;
    const response = await axios.get(`http://127.0.0.1:8000/api/places/${id}/`);
    this.place = response.data;
  },
};
</script>
