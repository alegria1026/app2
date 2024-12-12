<template>
  <div id="app" class="container">
    <div class="loginBox">
      <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
      <h1 class="MainTitle">Iniciar Sesión</h1>
      <main>
        <form class="login-form" @submit.prevent="handleSubmit">
          <label for="email">Email</label>
          <input
            type="email"
            id="email"
            v-model="user.email"
            placeholder="Enter Email"
            required
          />

          <label for="password">Password</label>
          <input
            type="password"
            id="password"
            v-model="user.password"
            placeholder="Enter Password"
            required
          />

          <button type="submit">Entrar</button>
        </form>
        <p v-if="message" class="error">{{ message }}</p>
      </main>

      <div class="register">
        <p>¿No tienes una cuenta?</p>
        <router-link to="/register" aria-label="Regístrate aquí">Regístrate aquí</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: {
        email: '',
        password: '',
      },
      message: '', // Para mostrar errores o notificaciones
    };
  },

  methods: {
    async handleSubmit() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/api/usuario/login', {
          email: this.user.email,
          password: this.user.password
        });

        if (response.status === 200) {
          this.$router.push('/products'); // Redirige al dashboard o página principal
        } else {
          this.message = response.data.message || 'Error al iniciar sesión';
        }
      } catch (error) {
        this.message = 'Error al conectar con el servidor';
      }
    }
  }
};
</script>

<style scoped>
.container {
  min-width: 80vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

.loginBox {
  margin-left: 24rem;
  min-width: fit-content;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  background-color: #f2f2f2;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.MainTitle {
  font-size: 2.5rem;
  font-weight: bold;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding-bottom: 2rem;
  background: linear-gradient(90deg, #42b983, #57799c);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  transition: background 5s ease-in-out;
}

.MainTitle:hover {
  background: linear-gradient(90deg, #57799c, #42b983);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.login-form {
  width: 100%;
  max-width: 300px;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.login-form label {
  font-weight: bold;
}

.login-form input {
  padding: 0.5rem;
  border: 1px solid #cccccc;
  border-radius: 6px;
  background: #ffffff;
}

.login-form button {
  padding: 0.75rem;
  border: none;
  border-radius: 4px;
  background: #42b983;
  color: #fff;
  font-weight: bold;
  cursor: pointer;
}

.login-form button:hover {
  background: #36a273;
}

.error {
  color: red;
  margin-top: 1rem;
  font-size: 0.9rem;
}

.register {
  padding: 2rem;
  text-align: center;
}

.register a {
  color: #42b983;
  font-weight: bold;
  text-decoration: none;
}

.register a:hover {
  text-decoration: underline;
  color: #36a273;
}
</style>
