# Explicación Detallada - Algoritmos Básicos

## Objetivo

Explicar los patrones de contador, acumulador, máximo, mínimo, valor previo y reporte acumulado.

## Algoritmos implementados

Los dos programas recorren una secuencia de entradas una sola vez y mantienen únicamente el estado histórico necesario para producir estadísticas y reportes.

## Ejercicio 1: temperaturas

`-100` funciona como centinela y no se incorpora a las estadísticas. El programa conserva cantidad, suma, mayor y menor.

`previo` representa la temperatura ya procesada. Cuando la diferencia es exactamente cinco grados, se aplica la fórmula de ajuste y se registra la diferencia en `informe`.

El máximo, mínimo y promedio se calculan sobre la temperatura ajustada. Esta decisión debe mantenerse consistente al interpretar resultados.

## Ejercicio 2: análisis sísmico

La zona `-1` termina el ingreso. Cuatro contadores permiten calcular porcentajes y dos acumuladores producen promedios de magnitud y profundidad.

Cada registro se concatena al informe con un ID incremental. La validación actual no rechaza zonas desconocidas: igualmente aumenta el total, pero no un contador regional. Esto puede hacer que los porcentajes conocidos no sumen 100 %.

## Complejidad

Ambos algoritmos procesan cada entrada una vez: tiempo `O(n)`. Los informes acumulados crecen con `O(n)` datos; las demás variables usan espacio constante.

## Estado

Los dos scripts compilan y cubren las actividades principales. La extensión del PDF que vuelve a leer el informe desde archivo no está implementada.

## Cómo verificar

Use cero registros, un registro y varias zonas. Para temperaturas, incluya diferencias de cinco y valores que no se ajusten. Para sismos, pruebe una zona inválida y observe el supuesto pendiente de validación.
