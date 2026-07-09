# Explicación Detallada - Simulacro Prueba 2 2024 S2

## Objetivo

Explicar cómo ambos programas representan estado, procesan archivos y mantienen datos relacionados durante búsquedas y ordenamientos.

## Problema 1: Tapper

### Modelo y algoritmo

Cada barra posee cuatro datos paralelos:

- Nombre.
- Ingreso acumulado.
- Entregas procesadas.
- Lista de vasos aún no vendidos.

`detector()` examina el final de la lista activa. Un trago se vende inmediatamente; dos cervezas consecutivas o tres bebidas consecutivas se retiran y generan ingreso.

El estado restante se conserva para la próxima línea de la misma barra. Esto es esencial: una combinación puede completarse entre entregas distintas.

### Reportes

El programa calcula ingresos por barra, porcentaje de ingreso por producto, vasos destruidos, cantidad de atenciones y promedio. Los ordenamientos intercambian listas en paralelo para conservar correspondencia.

La lógica de barras más y menos atendidas mezcla índices después de ordenar; en empates, las etiquetas impresas deben revisarse manualmente. No afecta el procesamiento principal de ingresos.

## Problema 2: Cinemark

### Matriz de sala

Una matriz `10 x 10` usa:

- `-1`: asiento restringido.
- `0`: asiento permitido no vendido.
- `1`: asiento estándar vendido.
- `2`: asiento DBOX vendido.

La inicialización alterna posiciones permitidas según paridad de fila y columna.

### Procesamiento de ventas

Cada línea identifica fila, asiento y tipo. Si la celda contiene `-1`, se registra ingreso perdido; si está habilitada, se marca la venta y se acumula recaudación por fila.

Al finalizar, los `-1` se reemplazan por cero para presentar la matriz. Un máximo identifica la fila de mayor recaudación y un ordenamiento paralelo presenta pérdidas crecientes.

## Correctitud y complejidad

Si Tapper procesa `n` vasos, su recorrido principal es `O(n)`, más ordenamientos cuadráticos sobre el pequeño conjunto de barras. Cinemark procesa `v` ventas en `O(v)` y ordena diez filas en `O(10²)`.

Ambos scripts finalizan con los datos entregados. Cinemark reproduce pérdida total, fila E y pérdidas por fila del ejemplo.

## Archivos de entrada

- `entregas.txt` para Tapper.
- `ventas_avatar.txt` para Cinemark.

## Cómo verificar la solución

Ejecute ambos scripts desde la carpeta del simulacro. Además de comparar cifras, revise que las listas paralelas mantengan la misma entidad después de cada ordenamiento.
