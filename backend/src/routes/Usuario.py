from flask import Blueprint, jsonify, request

from models.entities.Usuario import Usuario

from models.UsuarioModel import UsuarioModel

main=Blueprint('usuario_blueprint', __name__)


@main.route('/add', methods=['POST'])
def add_usuario():
    try:
        data = request.get_json()
        usuario = Usuario('', nombre_usuario=data['username'], correo_usuario=data['email'], contrasena_usuario=data['password'])
        id_usuario = UsuarioModel.add_usuario(usuario)
        return jsonify({'message': 'Usuario agregado', 'id': id_usuario}), 201
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/login', methods=['POST'])
def login():
    try:
        # Obtener datos del cuerpo de la solicitud
        email = request.json['email']
        password = request.json['password']

        # Buscar usuario por correo y contraseña
        usuario = UsuarioModel.get_usuario_by_email(email, password)

        if usuario:
            return jsonify({
                'message': 'Inicio de sesión exitoso',
                'user': usuario.to_JSON()
            }), 200
        else:
            return jsonify({'message': 'Usuario o contraseña incorrectos'}), 401

    except Exception as ex:
        return jsonify({'message': str(ex)}), 501