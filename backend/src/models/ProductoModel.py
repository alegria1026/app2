from database.db import get_connection
from .entities.Producto import Producto

class ProductoModel():

    def get_productos():
        try:
            connection = get_connection()

            productos = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT id_producto, nombre_producto, precio_producto, descripcion_producto FROM public.producto")
                resultset = cursor.fetchall()

                for row in resultset:
                    producto = Producto(row[0], row[1], row[2], row[3])
                    productos.append(producto.to_JSON())

                connection.close()
                return productos
        except Exception as ex:
            raise Exception(ex)
    
    def add_producto(producto):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                query = 'INSERT INTO public.producto (nombre_producto, precio_producto, descripcion_producto) VALUES (%s, %s, %s) RETURNING id_producto'
                cursor.execute(query, (producto.nombre_producto, producto.precio_producto, producto.descripcion_producto))

                id_producto = cursor.fetchone()[0]
                connection.commit()
                connection.close()
                return id_producto
        except Exception as ex:
            raise Exception(ex)
        
    def update_producto(id_producto, data):
        try:
            connection = get_connection()

            # Construir dinámicamente los campos a actualizar
            update_fields = []
            update_values = []

            if 'nombre' in data:
                update_fields.append("nombre_producto = %s")
                update_values.append(data['nombre'])

            if 'precio' in data:
                update_fields.append("precio_producto = %s")
                update_values.append(data['precio'])

            if 'descripcion' in data:
                update_fields.append("descripcion_producto = %s")
                update_values.append(data['descripcion'])

            # Si no hay campos para actualizar
            if not update_fields:
                raise Exception("No se proporcionaron campos para actualizar")

            # Agregar id_producto al final de los valores
            update_values.append(id_producto)

            # Generar consulta SQL dinámica
            query = f"UPDATE public.producto SET {', '.join(update_fields)} WHERE id_producto = %s"

            # Ejecutar la consulta
            with connection.cursor() as cursor:
                cursor.execute(query, update_values)
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    def delete_producto(id_producto):
        try:
            connection = get_connection()

            # Ejecutar la consulta para eliminar el producto por su ID
            query = "DELETE FROM public.producto WHERE id_producto = %s"
            
            with connection.cursor() as cursor:
                cursor.execute(query, (id_producto,))
                affected_rows = cursor.rowcount  # Verifica cuántas filas fueron afectadas
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
