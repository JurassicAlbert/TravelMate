import { createRouter, createWebHistory } from 'vue-router';
import SearchPlaces from '../views/SearchPlaces.vue';
import PlaceDetails from '../views/PlaceDetails.vue';
import VisitedPlaces from '../views/VisitedPlaces.vue';

const routes = [
  { path: '/', component: SearchPlaces, name: 'search' },
  { path: '/place/:id', component: PlaceDetails, name: 'place-details' },
  { path: '/visited', component: VisitedPlaces, name: 'visited' },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
