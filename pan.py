
from producto import Producto


class Pan(Producto):
    def __init__(self, codigo, nombre, precio, stock, unidad_venta, tipo_harina):
        super().__init__(codigo, nombre, precio, stock, unidad_venta)
        self.__tipo_harina = tipo_harina

    def mostrar_descripcion(self):
        return (
            f"Pan: {self.get_nombre()} - "
            f"${self.get_precio()} por {self.get_unidad_venta()} "
            f"- Harina: {self.__tipo_harina}"
        )
