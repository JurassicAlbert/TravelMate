<template>
  <div class="register-container">
    <h1>Register</h1>
    <form @submit.prevent="registerUser">
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
      <div class="form-group">
        <label for="confirmPassword">Confirm Password</label>
        <input
          type="password"
          id="confirmPassword"
          v-model="confirmPassword"
          placeholder="Confirm your password"
          required
        />
      </div>
      <button type="submit" class="btn">Register</button>
    </form>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    <p v-if="successMessage" class="success">{{ successMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RegisterPage',
  data() {
    return {
      email: '',
      password: '',
      confirmPassword: '',
      errorMessage: '',
      successMessage: ''
    };
  },
  methods: {
    async registerUser() {
      // Sprawdzenie, czy hasła się zgadzają
      if (this.password !== this.confirmPassword) {
        this.errorMessage = "Passwords do not match!";
        return;
      }

      try {
        // Wysyłanie danych do backendu (rejestracja)
        await axios.post('http://127.0.0.1:8000/register/', {
          email: this.email,
          password: this.password
        });

        // Po udanej rejestracji
        this.successMessage = 'Registration successful. Please log in.';
        this.email = '';
        this.password = '';
        this.confirmPassword = '';
        this.errorMessage = ''; // Usuwanie poprzednich komunikatów o błędach
      } catch (error) {
        // Obsługa błędów
        this.errorMessage = error.response?.data?.detail || 'An error occurred during registration.';
      }
    }
  }
};
</script>

<style scoped>
/* Stylizowanie formularza rejestracji */
.register-container {
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

.success {
  color: green;
  font-size: 14px;
}
</style>
