# Solución - Prueba 3 - 2021 S1

**Asignatura**: Programación

**Período**: 2021 S1

**Tipo**: Prueba 3

**Estado**: Completa para los datos entregados

## Descripción

La evaluación contiene dos problemas integradores: planificación de compras en supermercados e inventario de una empresa de distribución.

Ambos problemas poseen implementación y archivos de entrada. Los scripts fueron ejecutados con los datos incluidos y reproducen los resultados principales del enunciado.

## Explicación detallada

Consulta [EXPLICACIÓN.md](EXPLICACIÓN.md) para estudiar matrices, listas paralelas, acumuladores, búsqueda de mínimos, despachos y ordenamiento.

## Ejercicios

| Problema | Estado | Archivo |
| --- | --- | --- |
| A. Al super | Implementado y ejecutado | `src/Super.py`. |
| B. Izzet Distribution | Implementado y ejecutado | `src/Distribution.py`. |

## Estructura de la solución

```text
P3 2021 S1/
├── PRUEBA.pdf
├── precios.txt
├── recetas.txt
├── recibidos.txt
└── Solución/
    ├── README.md
    ├── EXPLICACIÓN.md
    └── src/
        ├── Super.py
        └── Distribution.py
```

## Cómo ejecutar

Desde la carpeta de evaluación:

```powershell
python "Solución/src/Super.py"
python "Solución/src/Distribution.py"
```

Se requiere NumPy.

## Resultado esperado

`Super.py` informa productos y total por supermercado, además del costo de cada receta. `Distribution.py` reporta despachos, matriz de cantidades, costo total, ubicación con más pendientes y totales por zona.

## Estado

- [x] Ambos enunciados implementados.
- [x] Archivos de entrada disponibles.
- [x] Ambos scripts ejecutados sin excepciones.
- [x] Resultados principales coinciden con el ejemplo.

La clasificación “completa” se refiere a los datos entregados. Existen supuestos de robustez documentados en la explicación.
