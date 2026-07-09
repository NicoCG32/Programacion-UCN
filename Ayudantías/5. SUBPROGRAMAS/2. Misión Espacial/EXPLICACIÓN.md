# Explicación Detallada - Misión Espacial

## Objetivo

Explicar cómo las funciones separan conversiones, fórmulas, clasificación y generación de informes.

## Implementación

`CalcularKM` normaliza distancias expresadas con unidades diferentes. `DeterminarIndice` combina gravedad, temperatura y radiación. `Clasificar` traduce el índice a una categoría.

`DeterminarSimilitudes` y `DeterminarDiferencia` comparan cada planeta con valores de referencia. `ImprimirInforme` concentra el formato de salida.

El ciclo principal lee `exoplanetas.txt`, convierte cada registro y actualiza máximos, mínimos y promedios condicionales.

Esta división permite probar fórmulas sin leer archivos. Cada función posee entradas y retorno identificables, que es el objetivo central de la ayudantía.

## Correctitud y complejidad

Para `n` planetas, el tiempo es `O(n)` y el espacio adicional es `O(1)` si solo se conservan agregados. La corrección depende de mantener unidades coherentes antes de aplicar fórmulas.

El archivo se abre sin declarar `encoding`; en sistemas con otra codificación podrían aparecer errores con caracteres especiales.

## Estado

`Mision.py` es la solución desarrollada y compila. `Ej.py` contiene funciones de apoyo o una versión inicial, no el flujo completo.

## Cómo verificar

Ejecute con `exoplanetas.txt` en el directorio de trabajo. Pruebe además las funciones con valores conocidos y verifique límites exactos entre categorías.
