
from pan import Pan
from factura import Factura
from inventario import Inventario

inventario = Inventario()

pan1 = Pan(1, "Pan frances", 2500, 15, "kg", "000")
factura1 = Factura(2, "Medialuna", 500, 30, "unidad", "Dulce")

inventario.agregar_producto(pan1)
inventario.agregar_producto(factura1)

print("PRODUCTOS DE LA PANADERIA")
inventario.listar_productos()

print("BUSCAR PRODUCTO")
producto = inventario.buscar_producto(1)

if producto is not None:
    print(producto.mostrar_descripcion())
