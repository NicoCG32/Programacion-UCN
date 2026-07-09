# Solución - RECA - 2025 S2

**Asignatura**: Programación

**Período**: 2025 S2

**Tipo**: Examen recuperativo

**Estado**: Parcial

## Descripción

La parte 1 solicita una simulación completa de Escaleras y Serpientes con resultados por vuelta y estadísticas globales. La parte 2 solicita analizar transacciones de tarjetas.

La solución disponible implementa una parte de la simulación. No existe implementación para Facturando.

## Explicación detallada

Consulta [EXPLICACIÓN.md](EXPLICACIÓN.md) para revisar el tablero bidireccional, los atajos, los turnos y los requisitos pendientes.

## Ejercicios

| Problema | Estado | Evidencia |
| --- | --- | --- |
| A. Escaleras y Serpientes | Parcial y ejecutable | `src/SerpientesEscaleras.py`. |
| B. Facturando | No implementado | `transacciones.txt` disponible. |

## Estructura de la solución

```text
RECA 2025 S2/
├── PRUEBA - PARTE 1.pdf
├── PRUEBA - PARTE 2.pdf
├── tablero.txt
├── transacciones.txt
├── salida ex.txt
├── salida_txt_ejemplo.txt
└── Solución/
    ├── README.md
    ├── EXPLICACIÓN.md
    └── src/
        └── SerpientesEscaleras.py
```

## Cómo ejecutar

Desde la carpeta de evaluación:

```powershell
python "Solución/src/SerpientesEscaleras.py"
```

Se requiere NumPy.

## Resultado esperado

El script carga múltiples partidas, construye numeración bidireccional, mueve jugadores, aplica atajos y muestra una clasificación al terminar cada partida.

No produce todavía todos los resultados por vuelta ni los análisis históricos y de eficiencia exigidos.

## Estado

- [x] Lectura de partidas y tableros.
- [x] Movimiento con regla de sobrepaso.
- [x] Aplicación de escaleras y serpientes.
- [x] Clasificación al final de la partida.
- [ ] Clasificación después de cada vuelta.
- [ ] Ganador y vuelta exacta de victoria.
- [ ] Ranking histórico y jugadores sin victorias.
- [ ] Ganancia y pérdida acumuladas por atajos.
- [ ] Problema Facturando.

La evaluación es parcial.
