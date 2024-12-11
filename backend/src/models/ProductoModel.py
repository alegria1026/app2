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

                connection.close
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