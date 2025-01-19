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
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async loginUser() {
      try {
        // Wyślij dane logowania (email, password) do backendu
        const response = await axios.post("http://127.0.0.1:8000/api/login/", {
          email: this.email,
          password: this.password,
        });

        // Po udanym logowaniu, zapisz tokeny (access i refresh) w localStorage
        console.log("Logged in successfully:", response.data);
        localStorage.setItem("access_token", response.data.access);
        localStorage.setItem("refresh_token", response.data.refresh);

        // Przekierowanie na stronę główną lub inną stronę po udanym logowaniu
        this.$router.push({ name: "Home" }); // Załóżmy, że masz route o nazwie "Home"
      } catch (error) {
        // Obsługuje błąd logowania
        console.error("Error during login:", error.response ? error.response.data : error);
        alert("Invalid credentials. Please try again.");
      }
    },
  },
};
</script>

<style scoped>
.login {
  width: 300px;
  margin: 0 auto;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 5px;
}

input {
  padding: 10px;
  margin-bottom: 15px;
}

button {
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
