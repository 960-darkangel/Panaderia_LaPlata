from datetime import date
from detalle_venta import DetalleVenta


class Venta:
    def __init__(self, numero):
        self.__numero = numero
        self.__fecha = date.today()
        self.__detalles = []
        self.__registrada = False

    def agregar_detalle(self, producto, cantidad):
        if self.__registrada:
            return False

        if cantidad <= 0:
            return False

        if producto.consultar_stock() < cantidad:
            return False

        # Evitamos repetir el mismo producto en distintos detalles.
        for detalle in self.__detalles:
            if detalle.get_producto() == producto:
                nueva_cantidad = detalle.get_cantidad() + cantidad

                if nueva_cantidad > producto.consultar_stock():
                    return False

                # Actualizamos el detalle existente.
                self.__detalles.remove(detalle)
                nuevo_detalle = DetalleVenta(producto, nueva_cantidad)
                self.__detalles.append(nuevo_detalle)
                return True

        self.__detalles.append(DetalleVenta(producto, cantidad))
        return True

    def calcular_total(self):
        total = 0

        for detalle in self.__detalles:
            total += detalle.calcular_subtotal()

        return total

    def registrar_venta(self):
        if self.__registrada or len(self.__detalles) == 0:
            return False

        # Primero verificamos que todos los productos tengan stock.
        for detalle in self.__detalles:
            producto = detalle.get_producto()

            if producto.consultar_stock() < detalle.get_cantidad():
                return False

        # Recién ahora descontamos las cantidades.
        for detalle in self.__detalles:
            producto = detalle.get_producto()
            nuevo_stock = producto.consultar_stock() - detalle.get_cantidad()
            producto.actualizar_stock(nuevo_stock)

        self.__registrada = True
        return True

    def consultar_detalles(self):
        return self.__detalles

    def get_numero(self):
        return self.__numero

    def get_fecha(self):
        return self.__fecha