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
              <button class="edit-btn" @click="openEditModal(product)">Editar</button>
              <button class="delete-btn" @click="deleteProduct(product.id_producto)">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="add-product">
        <button class="add-btn" @click="showFormModal = true">Agregar Producto</button>
      </div>
      <!-- Modal para agregar producto -->
      <div v-if="showFormModal" class="modal-overlay">
        <div class="modal">
          <button class="close-btn" @click="closeModal">×</button>
          <ProductForm @add-product="addProduct" />
        </div>
      </div>
      <!-- Modal para editar producto -->
      <div v-if="showEditModal" class="modal-overlay">
        <div class="modal">
          <button class="close-btn" @click="closeEditModal">×</button>
          <!-- Vista de edición del producto -->
          <EditProduct :product="editingProduct" @product-updated="editProduct" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import ProductForm from './ProductForm.vue';
import EditProduct from './EditProduct.vue'; // Importar la vista de edición

// Configuración de Axios
const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:5000/api/productos',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Variables reactivas
const products = ref([]);
const showFormModal = ref(false);
const showEditModal = ref(false);
const editingProduct = ref(null); // Producto que se está editando

// Función para obtener productos
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
    await apiClient.post('/add', product);
    await fetchProducts();
  } catch (error) {
    console.error('Error al agregar producto:', error);
  } finally {
    showFormModal.value = false;
  }
};

// Función para abrir el modal de edición
const openEditModal = (product) => {
  editingProduct.value = { ...product }; // Copia los datos del producto para editarlos
  showEditModal.value = true;
};

// Función para cerrar el modal de edición
const closeEditModal = () => {
  showEditModal.value = false;
  editingProduct.value = null;
};

// Función para actualizar un producto
const editProduct = async (updatedProduct) => {
  try {
    const id = updatedProduct.id_producto; // Asegúrate de usar el ID correcto
    await apiClient.put(`/update/${id}`, updatedProduct); // Llamada al backend para actualizar
    await fetchProducts(); // Recargar la lista de productos
  } catch (error) {
    console.error('Error al actualizar producto:', error);
  } finally {
    showEditModal.value = false;
  }
};

// Función para eliminar un producto
const deleteProduct = async (id) => {
  try {
    await apiClient.delete(`/delete/${id}`);
    products.value = products.value.filter((product) => product.id_producto !== id);
  } catch (error) {
    console.error('Error al eliminar producto:', error);
  }
};

// Función para cerrar el modal de agregar producto
const closeModal = async () => {
  showFormModal.value = false;
  await fetchProducts();
};

// Cargar productos al inicio
fetchProducts();
</script>


<style scoped>
/* Estilos del botón de edición */
.edit-btn {
  background: #ffc107;
  color: #fff;
  border: none;
  border-radius: 6px;
  margin-right: 0.5rem;
  padding: 1rem;
  margin-bottom: 0.5rem;
  box-shadow: 0 4px 10px var(--color-border-hover);

}

.edit-btn:hover {
  background: #e0a800;
}
.container {
  min-width: 85.5vw;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  background-color: var(--color-background-soft);
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
  color: #222222;

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
  padding: 1rem;
  background: #ff4d4d;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 0.5rem;
  margin-bottom: 0.5rem;
  box-shadow: 0 4px 10px var(--color-border-hover);

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
h2{
  color: #42b983;
}
</style> 