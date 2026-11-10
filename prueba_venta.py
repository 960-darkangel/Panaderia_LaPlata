from pan import Pan
from factura import Factura
from venta import Venta

# Creamos los productos.
pan1 = Pan(1, "Pan francés", 2500, 15, "kg", "000")
factura1 = Factura(2, "Medialuna", 500, 30, "unidad", "Dulce")

# Creamos una venta.
venta1 = Venta(1)

# Agregamos productos.
venta1.agregar_detalle(pan1, 2)
venta1.agregar_detalle(factura1, 6)

# Mostramos los detalles.
print("VENTA N°:", venta1.get_numero())
print("FECHA:", venta1.get_fecha())
print("-------------------------")

for detalle in venta1.consultar_detalles():
    producto = detalle.get_producto()

    print(producto.get_nombre())
    print("Cantidad:", detalle.get_cantidad())
    print("Subtotal: $", detalle.calcular_subtotal())
    print("-------------------------")

# Calculamos el total.
print("TOTAL: $", venta1.calcular_total())

# Registramos la venta.
if venta1.registrar_venta():
    print("Venta registrada correctamente.")
else:
    print("No se pudo registrar la venta.")

# Consultamos el stock actualizado.
print("-------------------------")
print("STOCK RESTANTE:")
print("Pan:", pan1.consultar_stock(), "kg")
print("Medialunas:", factura1.consultar_stock(), "unidades")