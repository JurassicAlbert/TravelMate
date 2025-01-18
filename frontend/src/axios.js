import axios from 'axios';

// Ustawienie globalne nagłówków
axios.defaults.baseURL = 'http://127.0.0.1:8000'; // adres backendu
axios.defaults.headers.common['Content-Type'] = 'application/json';

// Dodawanie tokenu do nagłówka w przypadku, gdy jest on zapisany w localStorage
const token = localStorage.getItem('access_token');
if (token) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

export default axios;
