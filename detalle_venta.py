class DetalleVenta:
    def __init__(self, producto, cantidad):
        self.__producto = producto
        self.__cantidad = cantidad
        self.__precio_unitario = producto.get_precio()

    def calcular_subtotal(self):
        return self.__cantidad * self.__precio_unitario

    def get_producto(self):
        return self.__producto

    def get_cantidad(self):
        return self.__cantidad