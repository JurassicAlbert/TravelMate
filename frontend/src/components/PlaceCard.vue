<template>
  <div class="place-card">
    <h3>{{ place.name }}</h3>
    <p>{{ place.short_description }}</p>
    <router-link :to="`/place/${place.id}`">Zobacz więcej</router-link>
  </div>
</template>

<script>
export default {
  props: {
    place: Object,
  },
};
</script>

<style>
.place-card {
  border: 1px solid #ccc;
  padding: 1em;
  margin-bottom: 1em;
}
</style>
