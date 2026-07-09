# Explicación Detallada - Prueba 2 2025 S2

## Objetivo

Explicar el procesamiento implementado para Producción en lotes y delimitar las partes faltantes de ambas evaluaciones.

## Contexto del problema

`indice.txt` representa una fábrica como matriz. Cada celda indica cuántos archivos de lote existen para una máquina. Los nombres siguen la convención `fila-columna-número.txt`.

`precios.txt` asocia productos con precios unitarios. Cada lote contiene fecha y líneas con producto, cantidad y coste total de producción.

## Algoritmo implementado

### Carga de la matriz

`CrearMatriz()` lee dimensiones y carga una matriz NumPy. Los valores quedan como `float`, por lo que el ciclo convierte cada cantidad a `int`.

### Listas paralelas

`productos[i]` y `valor_unitario[i]` representan el mismo producto. `unidadesProducidas[i]` acumula sus unidades. `BuscarIndiceElemento` recupera el índice mediante búsqueda lineal.

### Recorrido de lotes

Tres ciclos recorren fila, columna y número de lote:

```text
para cada máquina
  para cada lote declarado
    abrir fila-columna-número.txt
    acumular coste y unidades
```

`leerArchivo()` suma el coste de producción del lote y actualiza las unidades globales. Finalmente, el valor del inventario se calcula como la suma de precio unitario por unidades producidas.

## Correctitud y complejidad

Si existen `L` líneas de productos y `P` productos distintos, la búsqueda lineal hace que el costo sea `O(L * P)`. Un diccionario permitiría `O(L)` esperado.

El recorrido de nombres es correcto porque usa exactamente las cantidades de `indice.txt`. La ejecución con los 350 archivos termina y produce un valor total, pero lo imprime sin `round(..., 2)`.

## Requisitos pendientes

La implementación no imprime el listado de unidades acumuladas, aunque sí conserva esos datos. Tampoco guarda acumuladores por año, pese a leer la fecha de cada lote.

La parte 2 carece de script: no hay conversión de tiempos, clasificación acumulada, detección de adelantamientos ni vuelta rápida.

## Archivos de entrada

- `archivos.zip`: `indice.txt`, `precios.txt` y archivos de lotes.
- `gp.txt`: entrada de la parte 2 no implementada.
- `Ejecucion_completa.txt` y `salida.txt`: referencias de salida.

## Cómo verificar la solución

Ejecute `Lotes.py` con la carpeta extraída `archivos/` como directorio de trabajo. Debe procesar todos los lotes sin `FileNotFoundError`.

La verificación completa requiere comparar:

1. Cada coste por lote.
2. El total final de inventario.
3. La ausencia actual de los reportes por producto y por año.
