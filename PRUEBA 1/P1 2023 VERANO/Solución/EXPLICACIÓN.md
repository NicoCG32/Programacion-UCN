# Explicación Detallada - Prueba 1 Verano 2023

## Objetivo

Explicar la implementación disponible para el análisis de vehículos y dejar explícita la cobertura parcial de la evaluación.

## Contexto del problema

`autos.txt` está organizado por bloques. Una línea de cabecera contiene la marca y la cantidad de modelos; las líneas siguientes describen modelo, motor, cilindrada, potencia, transmisión y años de fabricación.

El programa debe calcular estadísticas locales por marca y estadísticas globales para todo el archivo.

## Algoritmo implementado

`Autos.py` aplica un recorrido secuencial con dos niveles:

1. El `while` exterior lee una marca.
2. El `for` interior procesa exactamente la cantidad de vehículos declarada.
3. Las variables locales se reinician al comenzar cada marca.
4. Las variables globales se conservan hasta terminar el archivo.

### Búsquedas por marca

`mayor_cilindrada` conserva el máximo observado y los datos del vehículo asociado. La eficiencia se calcula como:

```text
eficiencia = caballos de fuerza / cilindrada
```

Los contadores `cont_auto`, `cont_man` y `cont_total` permiten calcular porcentajes al finalizar el bloque.

### Búsquedas globales

El programa mantiene:

- La menor cilindrada y su modelo.
- El menor año inicial entre vehículos cuya fabricación continúa.
- La suma de períodos y cantidad de vehículos descontinuados.

El promedio de fabricación usa:

```text
promedio = suma de períodos / cantidad de descontinuados
```

## Flujo de datos

```text
autos.txt
  -> cabecera de marca
  -> vehículos de la marca
  -> estadísticas locales
  -> acumuladores globales
  -> reporte final
```

El script supone que el archivo está bien formado y que existe al menos un vehículo descontinuado. Si `descontinuados` fuera cero, la división final fallaría.

## Correctitud y complejidad

Cada vehículo se procesa una sola vez. Para `n` registros, el tiempo es `O(n)` y el espacio adicional es `O(1)`, sin contar las cadenas leídas.

Los máximos y mínimos son correctos bajo la condición indicada por el enunciado de que los resultados relevantes son únicos.

## Diferencias respecto del enunciado

- Solo se implementa el problema 2.
- No existe solución para la máquina de relojes.
- No se documentó la respuesta del ruteo.
- El símbolo del porcentaje automático se imprime como `$`.
- La salida tiene una errata en “transmisión”.
- No se cierran los archivos mediante `close()` ni un bloque `with`.

Estas diferencias justifican el estado parcial.

## Archivos de entrada

- `autos.txt`: utilizado por `Autos.py`.
- `relojes.txt`: corresponde al problema no implementado.

## Cómo verificar la solución

Desde la carpeta de la evaluación:

```powershell
python "Solución/src/Autos.py"
```

La ejecución debe finalizar sin excepciones y producir estadísticas para Ferrari y Renault. Los valores principales coinciden con el ejemplo del enunciado, salvo las diferencias de formato ya indicadas.
