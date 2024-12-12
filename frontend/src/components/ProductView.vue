<template>
  <div class="container">
    <h1 class="MainTitle">Gestión de Productos</h1>
    <div class="product-list">
      <h2>Lista de Productos</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Precio</th>
            <th>Descripción</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in products" :key="product.id_producto">
            <td>{{ product.id_producto }}</td>
            <td>{{ product.nombre_producto }}</td>
            <td>${{ product.precio_producto ? product.precio_producto.toFixed(2) : '0.00' }}</td>
            <td>{{ product.descripcion_producto }}</td>
            <td>
              <button class="delete-btn" @click="deleteProduct(product.id_producto)">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="add-product">
        <button class="add-btn" @click="showFormModal = true">Agregar Producto</button>
      </div>
      <!-- Modal -->
      <div v-if="showFormModal" class="modal-overlay">
        <div class="modal">
          <button class="close-btn" @click="closeModal">×</button>
          <!-- Formulario para agregar producto -->
          <ProductForm @add-product="addProduct" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import ProductForm from './ProductForm.vue';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:5000/api/productos',
  headers: {
    'Content-Type': 'application/json',
  },
});

const products = ref([]);
const showFormModal = ref(false);

// Función para obtener los productos
const fetchProducts = async () => {
  try {
    const response = await apiClient.get('/');
    products.value = response.data;
  } catch (error) {
    console.error('Error al cargar productos:', error);
  }
};

// Función para agregar un producto
const addProduct = async (product) => {
  try {
    await apiClient.post('/add', product); // Enviar datos al backend
    await fetchProducts(); // Recargar la lista de productos desde el backend
  } catch (error) {
    console.error('Error al agregar producto:', error);
  } finally {
    showFormModal.value = false; // Cerrar el modal
  }
};

// Función para eliminar un producto
const deleteProduct = async (id) => {
  try {
    await apiClient.delete(`/${id}`);
    products.value = products.value.filter((product) => product.id_producto !== id);
  } catch (error) {
    console.error('Error al eliminar producto:', error);
  }
};

// Función para cerrar el modal
const closeModal = async () => {
  showFormModal.value = false; // Cerrar el modal
  await fetchProducts(); // Recargar productos al cerrar el modal
};

// Cargar productos al inicio
fetchProducts();
</script>

<style scoped>
/* Estilos del componente */
.container {
  min-width: 85.5vw;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
}

.MainTitle {
  font-size: 2.5rem;
  font-weight: bold;
  text-transform: uppercase;
  background: linear-gradient(90deg, #42b983, #57799c);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 2rem;
}

.product-list {
  width: 100%;
  max-width: 600px;
  margin-bottom: 2rem;
}

.product-list table {
  width: 100%;
  border-collapse: collapse;
}

.product-list th,
.product-list td {
  border: 1px solid #ddd;
  padding: 0.75rem;
  text-align: left;
}

.product-list th {
  background-color: #f4f4f4;
}

.delete-btn {
  padding: 0.5rem 1rem;
  background: #ff4d4d;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.delete-btn:hover {
  background: #d93636;
}

.add-product {
  display: flex;
  flex-direction: row-reverse;
  padding: 1rem;
}

.add-btn {
  padding: 0.5rem 1rem;
  background: #42b983;
  color: #fff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

.add-btn:hover {
  background: #36a273;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal {
  background: #fff;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
  position: relative;
  width: 400px;
}

.close-btn {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #333;
}

.close-btn:hover {
  color: #d93636;
}
</style>