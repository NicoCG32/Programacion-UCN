# Explicación Detallada - MMA Chile

## Objetivo

Explicar una solución de listas paralelas más extensa, con records, rachas, campeón, estilos y ranking.

## Implementación

`CargarPeleadores()` carga nombres, estilos, records, rachas y apodos. Los records se representan como listas internas.

`CargarCombates()` busca participantes, determina ganador, actualiza victorias, derrotas, rachas y posibles cambios de campeón. Funciones separadas encapsulan cada operación.

Los reportes posteriores identifican invictos, estilos con máximos, victorias puras y rankings. `ordenar()` debe intercambiar todas las listas para conservar la identidad del peleador.

## Invariantes

Para todo índice `i`, nombre, estilo, record, racha y apodo deben corresponder a la misma persona. Además:

```text
combates totales = victorias + derrotas + otros resultados registrados
```

Las actualizaciones deben mantener no negativos todos los componentes.

## Complejidad

Las búsquedas por nombre y máximos son lineales. El ordenamiento es `O(n²)`. Para tamaños académicos es suficiente, aunque un modelo con diccionarios y objetos sería más robusto.

## Estado

`MMA Chile.py` compila y tiene archivos de peleadores y combates. Debido a su cantidad de listas y efectos, la verificación debe ser por invariantes y casos pequeños, no solo por inspección de la salida final.

## Cómo verificar

Ejecute desde esta carpeta. Seleccione manualmente un combate, calcule el record esperado y compruebe campeón y racha. Después revise que el ranking no desincronice atributos.
