# Explicación Detallada - Furbo Furbo

## Objetivo

Explicar el uso de listas paralelas para representar equipos y mantener su consistencia durante actualizaciones y ordenamientos.

## Implementación

`cargarLiga()` llena listas de nombres, partidos y goles. El índice `i` identifica al mismo equipo en todas ellas.

`cargarPartidos()` busca ambos equipos y actualiza resultados. `calcularPuntaje` y `calcularDif` derivan puntaje y diferencia de goles.

`buscarMayores` conserva todos los índices empatados en el máximo. `buscarGanador` aplica criterios sucesivos. `ordenar()` intercambia todas las listas relacionadas cada vez que cambia el orden.

El intercambio sincronizado es la invariante principal: nunca debe moverse el nombre sin sus estadísticas.

## Correctitud y complejidad

Las búsquedas por nombre son lineales. Con `p` partidos y `e` equipos, la actualización cuesta `O(p * e)`. El ordenamiento usado es cuadrático, `O(e²)`.

Un diccionario podría localizar equipos en tiempo constante esperado, pero las listas paralelas son el objetivo pedagógico.

## Estado

La solución compila y dispone de ambos archivos. Su salida depende de conservar la misma longitud y correspondencia en todas las listas.

## Cómo verificar

Ejecute desde esta carpeta y compruebe manualmente un partido. Después del ordenamiento, revise que puntos, goles y nombre sigan describiendo al mismo equipo.
