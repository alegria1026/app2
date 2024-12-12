class Usuario():
    def __init__(self, id_usuario = None, nombre_usuario = None, correo_usuario = None, contrasena_usuario = None ) -> None:
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.correo_usuario = correo_usuario
        self.contrasena_usuario = contrasena_usuario

    
    def to_JSON(self):
        return {
            'id_usuario': self.id_usuario,
            'nombre_usuario': self.nombre_usuario,
            'correo_usuario': self.correo_usuario,
            'contrasena_usuario': self.contrasena_usuario
        }