# Sistema de Gestión de Panadería La Plata

Proyecto desarrollado en Python para la gestión de productos, inventario y ventas de una panadería tradicional.

## Descripción

El sistema permite administrar las operaciones básicas de mostrador de una panadería, facilitando el registro y consulta de productos, el control de stock y la gestión de ventas.

Fue desarrollado como trabajo práctico de la materia **Algoritmos y Estructuras de Datos III**, correspondiente a la carrera Analista de Sistemas.

## Funcionalidades

- Registrar nuevos productos.
- Consultar productos y sus precios.
- Consultar y actualizar el stock.
- Modificar precios.
- Registrar ventas con uno o varios productos.
- Calcular automáticamente el total de cada venta.
- Descontar las cantidades vendidas del inventario.
- Consultar el historial de ventas.

## Tecnologías utilizadas

- Python
- HTML
- CSS
- Git y GitHub

## Estructura del proyecto

- `main.py`: programa principal y menú de opciones.
- `producto.py`: clase base de productos.
- `pan.py`: clase Pan.
- `factura.py`: clase Factura.
- `inventario.py`: administración del inventario.
- `detalle_venta.py`: detalle de los productos vendidos.
- `venta.py`: gestión y registro de ventas.
- `prueba*.py`: archivos de prueba de las clases.
- `diseños/`: prototipos visuales de las pantallas en HTML y CSS.

## Requisitos

- Python 3 instalado.

## Ejecución

1. Descargar o clonar este repositorio.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```bash
python main.py
```

En algunos sistemas puede ser necesario utilizar:

```bash
python3 main.py
```

## Diseños de interfaz

La carpeta `diseños/` contiene prototipos visuales estáticos realizados con HTML y CSS. Se pueden visualizar abriendo `diseños/index.html` en un navegador web.

## Consideraciones

- El sistema funciona mediante una interfaz de consola.
- Los datos se mantienen en memoria durante la ejecución del programa.
- El historial de ventas no se conserva al cerrar el programa.
- Los prototipos HTML y CSS son representaciones visuales y no están conectados funcionalmente con el sistema Python.

## Autoría

Trabajo práctico realizado para la carrera Analista de Sistemas.

**Materia:** Algoritmos y Estructuras de Datos III.
