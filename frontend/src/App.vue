<template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="loginUser">
      <div>
        <label for="email">Email:</label>
        <input type="email" v-model="email" id="email" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" id="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    async loginUser() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/login/', {
          email: this.email,
          password: this.password,
        });

        console.log('Logged in successfully:', response.data);
        localStorage.setItem('access_token', response.data.access);
        this.$router.push({ name: 'Home' }); // przekierowanie na stronę główną po zalogowaniu
      } catch (error) {
        console.error('Error during login:', error.response ? error.response.data : error);
        alert('Invalid credentials');
      }
    },
  },
};
</script>

