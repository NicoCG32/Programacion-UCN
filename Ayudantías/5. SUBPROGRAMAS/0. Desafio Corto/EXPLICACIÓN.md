# Explicación Detallada - Contar Palabras

## Objetivo

Comparar una solución basada en herramientas del lenguaje con una aproximación manual al conteo de palabras.

## Implementación

`ContarPalabras(texto)` usa:

```python
len(texto.split())
```

`split()` sin argumento agrupa secuencias de espacios y produce las palabras. Esta variante es breve y robusta frente a múltiples espacios.

`ContarPalabras2(texto)` recorre caracteres y construye una lógica manual. Su valor pedagógico es mostrar estado y transiciones; debe compararse cuidadosamente con espacios iniciales, finales o repetidos.

`Ej.py` es un archivo de trabajo y no representa necesariamente la solución final.

## Complejidad

Ambas estrategias recorren el texto y usan tiempo `O(n)`. `split()` crea una lista adicional de palabras, por lo que usa `O(n)` de memoria. Una solución manual puede usar espacio constante si no construye nuevas cadenas.

## Estado

La solución comparativa está implementada y compila. El alcance se limita al conteo separado por espacios; no realiza tokenización lingüística de signos o contracciones.

## Cómo verificar

Pruebe texto vacío, una palabra, varios espacios y signos de puntuación. Defina previamente qué resultado se espera en cada caso.
