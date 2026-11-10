from pan import Pan
from factura import Factura
from inventario import Inventario
from venta import Venta

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un número entero.")


def leer_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un valor numérico.")

# Creamos el inventario.
inventario = Inventario()

# Cargamos algunos productos iniciales.
inventario.agregar_producto(
    Pan(1, "Pan francés", 2500, 15, "kg", "000")
)

inventario.agregar_producto(
    Factura(2, "Medialuna", 500, 30, "unidad", "Dulce")
)

inventario.agregar_producto(
    Factura(3, "Factura con crema", 600, 20, "unidad", "Crema")
)


# Número de venta.
numero_venta = 1
historial_ventas = []

def consultar_ventas():
    if len(historial_ventas) == 0:
        print("Todavía no hay ventas registradas.")
        return

    print("\n===== HISTORIAL DE VENTAS =====")

    for venta in historial_ventas:
        print("\nVenta N°:", venta.get_numero())
        print("Fecha:", venta.get_fecha())

        for detalle in venta.consultar_detalles():
            producto = detalle.get_producto()

            print(
                producto.get_nombre(),
                "- Cantidad:", detalle.get_cantidad(),
                "- Subtotal: $", detalle.calcular_subtotal()
            )

        print("TOTAL: $", venta.calcular_total())
        print("-------------------------")

def mostrar_menu():
    print("\n===== PANADERÍA TRADICIONAL =====")
    print("1. Mostrar productos")
    print("2. Registrar una venta")
    print("3. Consultar stock")
    print("4. Modificar precio")
    print("5. Consultar historial de ventas")
    print("6. Registrar producto")
    print("7. Actualizar stock")
    print("8. Salir")


def registrar_venta():
    global numero_venta

    venta = Venta(numero_venta)

    while True:
        inventario.listar_productos()

        codigo = leer_entero("Código del producto (0 para terminar): ")

        if codigo == 0:
            break

        producto = inventario.buscar_producto(codigo)

        if producto is None:
            print("Producto inexistente.")
            continue

        cantidad = leer_numero("Cantidad: ")

        if venta.agregar_detalle(producto, cantidad):
            print("Producto agregado a la venta.")
        else:
            print("No se pudo agregar. Verifique la cantidad y el stock.")

    if len(venta.consultar_detalles()) == 0:
        print("No se registró ninguna venta.")
        return

    print("TOTAL A PAGAR: $", venta.calcular_total())

    while True:
        confirmar = input("¿Confirmar venta? (s/n): ").lower()

        if confirmar == "s" or confirmar == "n":
            break

        print("Respuesta incorrecta. Ingrese s o n.")

    if confirmar == "s":
        if venta.registrar_venta():
            historial_ventas.append(venta)
            print("Venta registrada correctamente.")
            numero_venta += 1
        else:
            print("No se pudo registrar la venta.")
    else:
        print("Venta cancelada.")

def consultar_stock():
    codigo = leer_entero("Ingrese el código del producto: ")

    producto = inventario.buscar_producto(codigo)

    if producto is not None:
        print(producto.mostrar_descripcion())
        print("Stock disponible:", producto.consultar_stock())
    else:
        print("Producto inexistente.")


def modificar_precio():
    codigo = leer_entero("Ingrese el código del producto: ")

    producto = inventario.buscar_producto(codigo)

    if producto is not None:
        nuevo_precio = leer_numero("Ingrese el nuevo precio: ")

        if producto.modificar_precio(nuevo_precio):
            print("Precio actualizado correctamente.")
        else:
            print("El precio debe ser mayor que cero.")
    else:
        print("Producto inexistente.")


def registrar_producto():
    print("\n===== REGISTRAR PRODUCTO =====")
    print("1. Pan")
    print("2. Factura")

    tipo_producto = leer_entero("Seleccione el tipo de producto: ")

    if tipo_producto != 1 and tipo_producto != 2:
        print("Tipo de producto incorrecto.")
        return

    codigo = leer_entero("Código: ")
    nombre = input("Nombre: ")

    precio = leer_numero("Precio: ")
    while precio <= 0:
        print("El precio debe ser mayor que cero.")
        precio = leer_numero("Precio: ")

    stock = leer_entero("Stock inicial: ")
    while stock < 0:
        print("El stock no puede ser negativo.")
        stock = leer_entero("Stock inicial: ")

    unidad = input("Unidad de venta (kg, unidad, docena, paquete): ")

    if tipo_producto == 1:
        tipo_harina = input("Tipo de harina: ")
        producto = Pan(
            codigo, nombre, precio, stock, unidad, tipo_harina
        )
    else:
        tipo = input("Tipo de factura: ")
        producto = Factura(
            codigo, nombre, precio, stock, unidad, tipo
        )

    if inventario.agregar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("Error: ya existe un producto con ese código.")


def actualizar_stock():
    print("\n===== ACTUALIZAR STOCK =====")

    codigo = leer_entero("Ingrese el código del producto: ")
    producto = inventario.buscar_producto(codigo)

    if producto is None:
        print("Producto inexistente.")
        return

    print(producto.mostrar_descripcion())
    print("Stock actual:", producto.consultar_stock())

    nueva_cantidad = leer_entero("Ingrese la nueva cantidad: ")

    while nueva_cantidad < 0:
        print("El stock no puede ser negativo.")
        nueva_cantidad = leer_entero("Ingrese la nueva cantidad: ")

    if inventario.actualizar_existencias(codigo, nueva_cantidad):
        print("Stock actualizado correctamente.")
    else:
        print("No se pudo actualizar el stock.")


# Programa principal.
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        inventario.listar_productos()
    elif opcion == "2":
        registrar_venta()
    elif opcion == "3":
        consultar_stock()
    elif opcion == "4":
        modificar_precio()
    elif opcion == "5":
        consultar_ventas()
    elif opcion == "6":
        registrar_producto()
    elif opcion == "7":
        actualizar_stock()
    elif opcion == "8":
        print("Gracias por utilizar el sistema.")
        break
    else:
        print("Opción incorrecta.")