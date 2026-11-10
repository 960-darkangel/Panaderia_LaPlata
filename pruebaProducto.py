from producto import Producto

producto1 = Producto(1, "Pan", 2500, 15, "kg")

print(producto1.mostrar_descripcion())
print("Stock disponible:", producto1.consultar_stock())
