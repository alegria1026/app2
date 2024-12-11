<template>
  <div id="app">
    <h1>Gestión de productos</h1>
    <form @submit.prevent="enviarDatos">
      <div>
        <label for="nombre">Nombre del producto:</label> <br>
        <input type="text" id="nombre" v-model="producto.nombre" placeholder="Ejemplo" required />
      </div>
      <div>
        <label for="precio">Precio del producto:</label> <br>
        <input type="text" id="precio" v-model="producto.precio" placeholder="$50" required />
      </div>
      <div>
      <label for="descripcion"> Descripción del producto </label> <br>
      <input type="text" id="descripcion" v-model="producto.descripcion" placeholder="El producto es..." required />
      </div>
      <button type="submit">Enviar</button>
    </form>
    <p v-if="mensaje">{{ mensaje }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      producto: {
        nombre: '',
        precio: '',
        descripcion: ''
      },
      mensaje: ''
    };
  },
  methods: {
    async enviarDatos() {
      try {
        const respuesta = await axios.post('http://127.0.0.1:5000/api/productos/add', this.producto);
        this.mensaje = respuesta.data.mensaje;
      } catch (error) {
        this.mensaje = 'Error al enviar los datos';
      }
    }
  }
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
}
form {
  margin: 20px;
}
input {
  margin: 10px 0;
  padding: 5px;
}
button {
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}
</style>