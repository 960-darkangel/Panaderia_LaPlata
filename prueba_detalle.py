from pan import Pan
from detalle_venta import DetalleVenta

pan1 = Pan(1, "Pan frances", 2500, 15, "kg", "000")

detalle1 = DetalleVenta(pan1, 2)

print("PRODUCTO:", detalle1.get_producto().get_nombre())
print("CANTIDAD:", detalle1.get_cantidad())
print("SUBTOTAL: $", detalle1.calcular_subtotal())