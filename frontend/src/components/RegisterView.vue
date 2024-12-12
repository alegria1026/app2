<template>
  <div id ="app" class="container">
    <div class="loginBox">
      <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
      <h1 class="MainTitle">Registrar</h1>
      <main>
        <form class="login-form" @submit.prevent="enviarDatos">
          <label for="username">Usuario</label>
          <input
              type="text"
              id="username"
              v-model="usuario.username"
              placeholder="Ingresa tu nombre de usuario"
              required
          />

          <label for="email">Email</label>
          <input
              type="email"
              id="email"
              v-model="usuario.email"
              placeholder="Ingresa tu email"
              required
          />

          <label for="password">Contraseña</label>
          <input
              type="password"
              id="password"
              v-model="usuario.password"
              placeholder="Ingresa tu contraseña"
              required
          />

          <label for="confirm-password">Confirmar Contraseña</label>
          <input
              type="password"
              id="confirm-password"
              name="confirm-password"
              placeholder="Repite tu contraseña"
              required
          />

          <button type="submit">Crear Cuenta</button>
        </form>
      </main>

      <div class="register">
        <p>¿Ya tienes una cuenta?</p> <router-link to="/" aria-label="Ingresa aquí">Ingresa aquí</router-link>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
      return{
        usuario: {
        username: '',
        email: '',
        password: ''
        }
      };
  },

  methods:{
    async enviarDatos(){
      try{
        const respuesta = await axios.post('http://127.0.0.1:5000/api/usuario/add', this.usuario);
        this.mensaje = respuesta.data.mensaje;
      } catch(error){
        this.mensaje = "Error al registrarse como usuario"
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
  margin-left: 26.8rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  background-color: #f2f2f2;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.logo {
  display: block;
  margin-bottom: 1rem;
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
<script setup lang="ts">
</script>