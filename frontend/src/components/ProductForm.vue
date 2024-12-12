<template>
  <div class="product-form">
    <h2>Agregar Producto</h2>
    <form @submit.prevent="handleSubmit">
      <label for="name">Nombre del Producto</label>
      <input
        type="text"
        id="name"
        v-model="nombre"
        placeholder="Nombre del producto"
        required
      />

      <label for="precio">Precio</label>
      <input
        type="number"
        id="precio"
        v-model="precio"
        placeholder="Precio"
        min="0"
        required
      />

      <label for="description">Descripción</label>
      <input
        type="text"
        id="description"
        v-model="descripcion"
        placeholder="Descripción del producto"
        required
      />

      <button type="submit" class="add-btn" :disabled="isLoading">
        {{ isLoading ? 'Cargando...' : 'Agregar Producto' }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue';

// Declarar el evento que será emitido al padre
const emit = defineEmits(['add-product']);

const nombre = ref('');
const precio = ref('');
const descripcion = ref('');
const isLoading = ref(false);

// Función para limpiar el formulario
const clearForm = () => {
  nombre.value = '';
  precio.value = '';
  descripcion.value = '';
};

// Manejo del envío del formulario
const handleSubmit = async () => {
  if (!nombre.value || !precio.value || !descripcion.value) {
    alert('Por favor, completa todos los campos.');
    return;
  }

  if (parseFloat(precio.value) < 0) {
    alert('El precio no puede ser un valor negativo.');
    return;
  }

  isLoading.value = true;

  try {
    const product = {
      nombre: nombre.value,
      precio: parseFloat(precio.value),
      descripcion: descripcion.value,
    };

    // Emitir evento con los datos del producto
    emit('add-product', product);

    clearForm(); // Limpia el formulario
    alert('Producto agregado exitosamente.');
  } catch (error) {
    console.error('Error al agregar producto:', error);
    alert('Hubo un problema al agregar el producto.');
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
/* Estilos del formulario */
.product-form {
  width: 100%;
  max-width: 400px;
  padding: 2rem;
  background: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.product-form label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.product-form input {
  width: 100%;
  padding: 0.75rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.add-btn {
  width: 100%;
  padding: 0.75rem;
  background: #42b983;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.add-btn:disabled {
  background: #ccc;
  cursor: not-allowed;
}
</style>