class Producto():
    def __init__(self, id_producto = None, nombre_producto = None, precio_producto = None, descripcion_producto = None ) -> None:
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.precio_producto = precio_producto
        self.descripcion_producto = descripcion_producto

    def __init__(self, nombre_producto = None, precio_producto = None, descripcion_producto = None ) -> None:
        self.nombre_producto = nombre_producto
        self.precio_producto = precio_producto
        self.descripcion_producto = descripcion_producto
    
    def to_JSON(self):
        return {
            'id_producto': self.id_producto,
            'nombre_producto': self.nombre_producto,
            'precio_producto': self.precio_producto,
            'descripcion_producto': self.descripcion_producto
        }
    