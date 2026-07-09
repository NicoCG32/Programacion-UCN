# Explicación Detallada - Ciclos

## Objetivo

Explicar cómo los ejercicios usan ciclos definidos, indefinidos, validación y fuerza bruta.

## Implementaciones

### Las tablas

Un `while` valida el número y dos ciclos `for` recorren multiplicadores del 1 al 12. En la segunda tabla, un `while` interno repite cada pregunta hasta recibir el producto correcto.

La validación actual acepta cero aunque el mensaje exige 1 a 12, porque comprueba `numero < 0` en vez de `numero < 1`.

### Salvando las notas

Tres ciclos anidados generan PIN desde `000` hasta `999`. El booleano `comprobador` permite detener todos los niveles cuando se encuentra la contraseña.

La variante extra recorre un alfabeto para generar cadenas de tres letras. Continúa iterando después de encontrarla, aunque conserva el resultado; un corte temprano sería más eficiente.

### UCENINO

El ciclo exterior termina con una cadena vacía. El ciclo interior actualiza coordenadas y omite símbolos inválidos. Luego reconstruye una ruta equivalente según desplazamiento neto.

Las coordenadas no se reinician entre entradas, por lo que cada ruta continúa desde la posición alcanzada anteriormente. Esto debe interpretarse como una aventura acumulativa.

## Complejidad

Las tablas usan `O(1)` por estar limitadas a 12 pasos. La fuerza bruta numérica examina hasta 1.000 combinaciones y la alfabética `a³` para un alfabeto de tamaño `a`. UCENINO usa `O(n)` por ruta.

## Estado

Los cuatro scripts compilan. Son soluciones de práctica con las observaciones indicadas; el PDF también contiene desafíos cuya cobertura depende de cada variante.

## Cómo verificar

Ejecute cada archivo de forma interactiva. Compruebe terminación, casos inválidos y que los contadores de intentos correspondan al orden de generación.
