import { createRouter, createWebHistory } from 'vue-router';

// Importowanie widoków z katalogu views
import HomePage from '../views/HomePage.vue';
import SearchPlaces from '../views/SearchPlaces.vue';
import PlaceDetails from '../views/PlaceDetails.vue';
import VisitedPlaces from '../views/VisitedPlaces.vue';
import UserPreferences from '../views/UserPreferences.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/search',
    name: 'search-places',
    component: SearchPlaces
  },
  {
    path: '/place/:id', // Dynamiczna trasa z parametrem `id`
    name: 'place-details',
    component: PlaceDetails,
    props: true // Przekazywanie parametru `id` do komponentu jako props
  },
  {
    path: '/visited',
    name: 'visited-places',
    component: VisitedPlaces
  },
  {
    path: '/preferences',
    name: 'user-preferences',
    component: UserPreferences
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
