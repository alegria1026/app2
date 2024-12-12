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
        # Obtener los datos enviados en la solicitud
        data = request.get_json()

        # Llamar al modelo para realizar la actualización
        affected_rows = ProductoModel.update_producto(id, data)

        if affected_rows == 1:
            return jsonify({'message': 'Producto actualizado', 'id': id}), 200
        else:
            return jsonify({'message': 'No se actualizó ningún producto'}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500