# Explicación Detallada - Rumbo al Verano

## Objetivo

Explicar el cruce de dos archivos mediante fecha y la separación del problema en funciones.

## Implementación

`CalcularTiempo` transforma `MM:SS` a segundos. `leerEntrenamiento(fecha)` recorre el archivo de actividad y calcula gasto para la fecha solicitada. `leerDieta(fecha)` procesa consumo calórico.

El ciclo principal solicita fechas hasta recibir `-1`, invoca ambas funciones y compara calorías consumidas y quemadas para evaluar la meta.

Cada función abre y recorre su archivo desde el inicio. Esto simplifica el diseño, aunque repite trabajo si se consultan muchas fechas.

## Correctitud y complejidad

Si entrenamiento tiene `e` líneas, dieta `d` y se consultan `q` fechas, el costo es `O(q * (e + d))`. Cargar índices por fecha permitiría una sola lectura.

La conversión de tiempo debe validar exactamente dos componentes y segundos en rango. Los casos sin datos se manejan mediante acumuladores en cero y mensajes específicos.

## Estado

`Rumbo al Verano.py` implementa el flujo principal y compila con ambos archivos. `Ej.py` es material de trabajo.

## Cómo verificar

Ejecute desde esta carpeta. Consulte una fecha presente en ambos archivos, una presente en solo uno y una inexistente. Verifique manualmente la conversión de al menos un tiempo.
