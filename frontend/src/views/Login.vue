<template>
  <div class="login-container">
    <h1>Login</h1>
    <form @submit.prevent="loginUser">
      <div class="form-group">
        <label for="email">Email</label>
        <input
          type="email"
          id="email"
          v-model="email"
          placeholder="Enter your email"
          required
        />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input
          type="password"
          id="password"
          v-model="password"
          placeholder="Enter your password"
          required
        />
      </div>
      <button type="submit" class="btn">Login</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage', // Zmieniona nazwa komponentu na wieloczłonową
  data() {
    return {
      email: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    async loginUser() {
      // Zalogowanie danych przed wysłaniem
      console.log("Sending data:", {
        email: this.email,
        password: this.password
      });

      try {
        const response = await axios.post('http://127.0.0.1:8000/login/', {
          email: this.email,
          password: this.password
        });

        // Zapisanie tokenów w localStorage
        localStorage.setItem('access_token', response.data.access);
        localStorage.setItem('refresh_token', response.data.refresh);

        // Ustawienie tokena w nagłówkach dla przyszłych zapytań
        axios.defaults.headers['Authorization'] = `Bearer ${response.data.access}`;

        // Przekierowanie użytkownika po udanym logowaniu
        this.$router.push({ name: 'home' });
      } catch (error) {
        // Obsługa błędów
        this.errorMessage = error.response?.data?.detail || 'An error occurred';
        console.error("Login error:", error); // Logowanie błędów
      }
    }
  }
};
</script>

<style scoped>
/* Stylizowanie formularza logowania */
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}

.error {
  color: red;
  font-size: 14px;
}
</style>
