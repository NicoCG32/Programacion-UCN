# Explicación Detallada - Prueba 3 2021 S1

## Objetivo

Explicar las dos soluciones integradoras y justificar sus estructuras de datos, flujo y complejidad.

## Problema A: Al super

### Modelo de datos

`ProductosXSupermercado` es una matriz de hasta 50 productos por tres supermercados. Las listas `Productos` y `Supermercados` traducen índices a nombres. `cantidades[f][c]` acumula cuántas unidades del producto `f` deben comprarse en el supermercado `c`.

### Algoritmo

1. `leerPrecios()` carga la matriz de precios.
2. Cada receta se separa por guiones.
3. Para cada ingrediente, `buscarMenorPrecio()` escoge el menor precio y acumula la cantidad requerida.
4. Se recorren las matrices para imprimir cantidades y costos.
5. `precioReceta` conserva el costo unitario de ingredientes de cada receta.

La elección del supermercado usa comparaciones estrictas. En un empate, la rama final favorece Duomarc o la segunda comparación, porque el enunciado no define un desempate.

### Complejidad

`Productos.index()` busca linealmente. Con `R` apariciones de ingredientes y `P` productos, el costo es `O(R * P)`. La impresión final recorre `O(P * 3)`.

## Problema B: Izzet Distribution

### Modelo de datos

Dos matrices `6 x 6` representan:

- Ítems pendientes en cada zona-sector.
- Cantidad de despachos realizados.

Las filas corresponden a zonas A-F y las columnas a sectores 1-6.

### Algoritmo de despacho

Cada registro aumenta una celda. `verificarDespacho()` recorre la matriz y, si encuentra más de 100 elementos, descuenta exactamente 100 y registra un despacho.

Después de procesar el archivo:

- Se multiplica cada despacho por el costo de su sector.
- Se buscan todas las ubicaciones con el máximo pendiente.
- Se suman filas para obtener pendientes por zona.
- Se ordenan totales y nombres en paralelo, de mayor a menor.

### Complejidad

La matriz tiene tamaño fijo, por lo que cada verificación cuesta una constante de 36 posiciones. Para `n` registros, el tiempo total es `O(n)`.

La implementación descuenta como máximo un despacho por celda y por registro. Sería insuficiente si un único registro dejara más de 200 unidades, aunque los datos incluidos no producen esa situación.

## Correctitud observada

Ambos scripts terminan sin excepciones con los archivos entregados. Los valores de costos, despachos, máximos y orden por zona coinciden con el ejemplo de ejecución.

## Archivos de entrada

- `precios.txt` y `recetas.txt` para `Super.py`.
- `recibidos.txt` para `Distribution.py`.

## Cómo verificar la solución

Desde la carpeta de evaluación:

```powershell
python "Solución/src/Super.py"
python "Solución/src/Distribution.py"
```

La verificación debe comparar tanto los valores globales como la asociación correcta entre nombres y listas o matrices paralelas.
