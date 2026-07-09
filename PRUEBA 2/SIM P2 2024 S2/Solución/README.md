# Solución - Simulacro Prueba 2 - 2024 S2

**Asignatura**: Programación

**Período**: 2024 S2

**Tipo**: Simulacro Prueba 2

**Estado**: Implementada con observaciones

## Descripción

El simulacro contiene los problemas Tapper y Cinemark. Ambos poseen script y archivo de entrada.

## Explicación detallada

La simulación de barras, la matriz de asientos y los ordenamientos paralelos se explican en [EXPLICACIÓN.md](EXPLICACIÓN.md).

## Ejercicios

| Problema | Estado | Archivo |
| --- | --- | --- |
| 1. Tapper | Implementado y ejecutado | `src/Tapper.py`. |
| 2. Cinemark | Implementado y ejecutado | `src/Cinemark.py`. |

## Estructura de la solución

```text
SIM P2 2024 S2/
├── PRUEBA.pdf
├── entregas.txt
├── ventas_avatar.txt
└── Solución/
    ├── README.md
    ├── EXPLICACIÓN.md
    └── src/
        ├── Tapper.py
        └── Cinemark.py
```

## Cómo ejecutar

Desde la carpeta del simulacro:

```powershell
python "Solución/src/Tapper.py"
python "Solución/src/Cinemark.py"
```

`Cinemark.py` requiere NumPy.

## Resultado esperado

Tapper informa ingresos, proporciones, vasos restantes, atenciones y promedios por barra. Cinemark muestra ventas rechazadas, pérdida total, matriz final, fila de mayor recaudación y pérdidas ordenadas.

## Estado

- [x] Ambos problemas implementados.
- [x] Archivos de entrada disponibles.
- [x] Ambos scripts ejecutados sin excepciones.
- [x] Cinemark reproduce los valores del ejemplo.
- [ ] Revisar manualmente etiquetas de barras empatadas en Tapper.

Por esa última limitación, el estado se expresa como “implementada con observaciones”.
