class Producto:
    def __init__(self, codigo, nombre, precio, stock, unidad_venta):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__unidad_venta = unidad_venta

    def consultar_stock(self):
        return self.__stock

    def actualizar_stock(self, cantidad):
        if cantidad >= 0:
            self.__stock = cantidad
            return True
        return False

    def descontar_stock(self, cantidad):
        if cantidad > 0 and cantidad <= self.__stock:
            self.__stock -= cantidad
            return True
        return False

    def modificar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            return True
        return False

    def mostrar_descripcion(self):
        return f"{self.__nombre} - ${self.__precio} por {self.__unidad_venta}"

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_unidad_venta(self):
        return self.__unidad_venta

