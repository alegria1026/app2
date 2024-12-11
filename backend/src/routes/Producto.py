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
        producto = Producto(nombre_producto=data['nombre'], precio_producto=data['precio'], descripcion_producto=data['descripcion'])
        id_producto = ProductoModel.add_producto(producto)
        return jsonify({'message': 'Producto agregado', 'id': id_producto}), 201
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500