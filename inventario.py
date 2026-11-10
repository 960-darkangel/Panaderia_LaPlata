
class Inventario:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        if self.buscar_producto(producto.get_codigo()) is None:
            self.__productos.append(producto)
            return True
        return False

    def buscar_producto(self, codigo):
        for producto in self.__productos:
            if producto.get_codigo() == codigo:
                return producto
        return None

    def listar_productos(self):
        for producto in self.__productos:
            print(producto.mostrar_descripcion())
            print("Stock:", producto.consultar_stock())
            print("--------------------")

    def actualizar_existencias(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)

        if producto is not None:
            return producto.actualizar_stock(cantidad)

        return False
