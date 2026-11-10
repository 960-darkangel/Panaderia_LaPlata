
from producto import Producto


class Factura(Producto):
    def __init__(self, codigo, nombre, precio, stock, unidad_venta, tipo):
        super().__init__(codigo, nombre, precio, stock, unidad_venta)
        self.__tipo = tipo

    def mostrar_descripcion(self):
        return (
            f"Factura: {self.get_nombre()} - "
            f"${self.get_precio()} por {self.get_unidad_venta()} "
            f"- Tipo: {self.__tipo}"
        )
