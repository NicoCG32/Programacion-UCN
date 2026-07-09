# Explicación Detallada - Condicionales

## Objetivo

Analizar el código deliberadamente incompleto de control de acceso y distinguir errores sintácticos, de comparación y de asignación.

## Implementación

El programa parte con tres datos: nivel, capacitación y condición de supervisor. La decisión correcta debe autorizar cuando se cumple:

```text
(nivel >= 3 y capacitación) o supervisor
```

`autorizado` y `mensaje` conservan el resultado observable.

## Errores intencionales

`elif supervisor = True` usa asignación donde Python exige una expresión. Debe emplear `==` o, de forma más directa, `elif supervisor:`.

`autorizado == False` compara, pero descarta el resultado. Para asignar corresponde `autorizado = False`. En este caso el valor ya fue inicializado, pero el error conceptual debe corregirse.

La condición inicial exige simultáneamente nivel suficiente y capacitación. Esto coincide con la lectura estricta del enunciado, mientras el supervisor actúa como excepción.

## Estado

`Codigo Incompleto.py` no compila y esa condición es deliberada: es material para depuración, no una solución terminada. La segunda actividad del PDF sobre elecciones no posee script.

## Cómo verificar

Después de corregir la sintaxis, pruebe al menos:

- Nivel suficiente con capacitación.
- Nivel suficiente sin capacitación.
- Supervisor sin capacitación.
- Persona sin ninguna condición habilitante.

Cada caso debe producir un booleano y un mensaje coherentes.
