<template>
    <div class="edit-product">
      <h2>Editar Producto</h2>
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
  
        <button type="submit" class="save-btn" :disabled="isLoading">
          {{ isLoading ? 'Guardando...' : 'Guardar Cambios' }}
        </button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, watch, defineProps, defineEmits } from 'vue';
  
  const emit = defineEmits(['product-updated']); // Emitir cuando el producto ha sido actualizado
  const props = defineProps({
    product: {
      type: Object,
      required: true, // Se espera un producto a editar
    },
  });
  
  const nombre = ref('');
  const precio = ref('');
  const descripcion = ref('');
  const isLoading = ref(false);
  
  // Inicializar los valores del formulario
  watch(
    () => props.product,
    (newProduct) => {
      if (newProduct) {
        nombre.value = newProduct.nombre_producto;
        precio.value = newProduct.precio_producto;
        descripcion.value = newProduct.descripcion_producto;
      }
    },
    { immediate: true }
  );
  
  // Manejo del envío del formulario
  const handleSubmit = async () => {
    isLoading.value = true;
    try {
      emit('product-updated', {
        id_producto: props.product.id_producto,
        nombre: nombre.value,
        precio: parseFloat(precio.value),
        descripcion: descripcion.value,
      });
    } catch (error) {
      console.error('Error al actualizar producto:', error);
    } finally {
      isLoading.value = false;
    }
  };
  </script>
  
  <style scoped>
  .edit-product {
    display: flex;
    flex-direction: column;
  }
  
  .edit-product label {
    margin-bottom: 0.5rem;
    font-weight: bold;
  }
  
  .edit-product input {
    margin-bottom: 1rem;
    padding: 0.75rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    width: 100%;
  }
  
  .save-btn {
    padding: 0.75rem;
    background: #42b983;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .save-btn:disabled {
    background: #ccc;
    cursor: not-allowed;
  }
  </style>
  