# Explicación Detallada - Cibercrisis

## Objetivo

Explicar la descomposición funcional y la lectura por bloques del archivo de ataques.

## Implementación

`DeterminarSiEsMalware` unifica nombres terminados en `ware`. `DeterminarCosto` aplica costo básico, triple o total según efectividad. `DetAtaqueMasRec` compara contadores y retorna “Variado” ante empate.

El archivo alterna cabeceras de continente con una cantidad determinada de países. El ciclo exterior procesa continentes y el interior consume exactamente sus registros.

Para cada país se cuentan tipos y se promedia efectividad. Para cada continente se acumulan ataques efectivos, costos y efectividad total. Finalmente se conserva el continente de mayor promedio como posible foco futuro.

## Correctitud y complejidad

Cada ataque se procesa una vez, por lo que el tiempo es `O(n)`. El espacio adicional es constante si no se almacenan todos los registros.

La clasificación de malware depende del sufijo y debe normalizar mayúsculas si los datos no son uniformes. Los empates continentales requieren una política explícita si el enunciado no garantiza unicidad.

## Estado

`cibercrisis.py` es la solución principal y compila con el archivo incluido. `Ej.py` representa una versión de trabajo más directa.

## Cómo verificar

Ejecute desde esta carpeta para que `ataques.txt` sea local. Compare promedios, cantidad de ataques efectivos, costos y foco futuro con cálculos manuales de un bloque pequeño.
