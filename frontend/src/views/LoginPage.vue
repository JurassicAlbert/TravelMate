<template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="loginUser">
      <div>
        <label for="email">Email:</label>
        <input
          type="email"
          id="email"
          v-model="email"
          required
        />
      </div>
      <div>
        <label for="password">Password:</label>
        <input
          type="password"
          id="password"
          v-model="password"
          required
        />
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginPage",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async loginUser() {
      try {
        // Wyślij dane logowania do backendu
        const response = await axios.post("http://127.0.0.1:8000/api/login/", {
          email: this.email,
          password: this.password,
        });

        // Po zalogowaniu zapisz tokeny
        console.log("Logged in successfully:", response.data);
        localStorage.setItem("access_token", response.data.access);
        localStorage.setItem("refresh_token", response.data.refresh);

        // Przekierowanie na stronę główną
        this.$router.push({ name: "HomePage" });
      } catch (error) {
        console.error("Error during login:", error.response ? error.response.data : error);
        alert("Invalid credentials. Please try again.");
      }
    },
  },
};
</script>

<style scoped>
/* Stylowanie formularza */
</style>
