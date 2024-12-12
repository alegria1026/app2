from flask import Blueprint, jsonify, request

from models.entities.Producto import Producto

from models.ProductoModel import ProductoModel

main=Blueprint('prducto_blueprint', __name__)

@main.route('/')
def get_productos():
    try:
        productos = ProductoModel.get_productos()
        return jsonify(productos)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/add', methods=['POST'])
def add_producto():
    try:
        data = request.get_json()
        producto = Producto('', nombre_producto=data['nombre'], precio_producto=data['precio'], descripcion_producto=data['descripcion'])
        id_producto = ProductoModel.add_producto(producto)
        return jsonify({'message': 'Producto agregado', 'id': id_producto}), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_producto(id):
    try:
        # Validar que el ID no sea vacío o undefined
        if not id or id == 'undefined':
            return jsonify({'message': 'ID inválido o no proporcionado'}), 400

        print(f"ID recibido: {id}")  # Depuración del ID recibido

        data = request.get_json()
        print(f"Datos recibidos: {data}")  # Depuración de los datos enviados desde el frontend

        # Validar datos recibidos
        if not data:
            return jsonify({'message': 'Datos inválidos'}), 400

        # Actualizar producto
        affected_rows = ProductoModel.update_producto(id, data)

        if affected_rows == 1:
            return jsonify({'message': 'Producto actualizado', 'id': id}), 200
        else:
            return jsonify({'message': 'No se actualizó ningún producto'}), 404
    except Exception as ex:
        print(f"Error al actualizar producto: {str(ex)}")  # Log de error
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id>', methods=['DELETE'])
def delete_producto(id):
    try:
        # Validar que el ID no sea vacío o undefined
        if not id or id == 'undefined':
            return jsonify({'message': 'ID inválido o no proporcionado'}), 400

        print(f"ID recibido: {id}")  # Depuración del ID recibido

        # Eliminar producto
        affected_rows = ProductoModel.delete_producto(id)

        if affected_rows == 1:
            return jsonify({'message': 'Producto eliminado', 'id': id}), 200
        else:
            return jsonify({'message': 'No se eliminó ningún producto'}), 404
    except Exception as ex:
        print(f"Error al eliminar producto: {str(ex)}")  # Log de error
        return jsonify({'message': str(ex)}), 500