from database.db import get_connection
from .entities.Usuario import Usuario

class UsuarioModel():
    
    def add_usuario(usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                query = 'INSERT INTO public.usuario (nombre_usuario, correo_usuario, contrasena_usuario) VALUES (%s, %s, %s) RETURNING id_usuario'
                cursor.execute(query, (usuario.nombre_usuario, usuario.correo_usuario, usuario.contrasena_usuario))

                id_usuario = cursor.fetchone()[0]
                connection.commit()
                connection.close()
                return id_usuario
        except Exception as ex:
            raise Exception(ex)
    
    @staticmethod
    def get_usuario_by_email(email, password):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                query = 'SELECT id_usuario, nombre_usuario, correo_usuario, contrasena_usuario FROM public.usuario WHERE correo_usuario = %s AND contrasena_usuario = %s'
                cursor.execute(query, (email, password))
                row = cursor.fetchone()

                if row:
                    return Usuario(
                        id_usuario=row[0],
                        nombre_usuario=row[1],
                        correo_usuario=row[2],
                        contrasena_usuario=row[3]
                    )
                return None
        except Exception as ex:
            raise Exception(f"Error al obtener el usuario por email y contraseña: {ex}")

