from pan import Pan
from factura import Factura

pan1 = Pan(1, "Pan frances", 2500, 15, "kg", "000")

factura1 = Factura(2, "Medialuna", 500, 30, "unidad", "Dulce")

productos = [pan1, factura1]

for producto in productos:
    print(producto.mostrar_descripcion())
    print("Stock:", producto.consultar_stock())
    print("--------------------")
