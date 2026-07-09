# Solución - Prueba 1 - Verano 2023

**Asignatura**: Programación

**Período**: Verano 2023

**Tipo**: Prueba 1

**Estado**: Parcial

## Descripción

La evaluación contiene tres problemas: ruteo manual, análisis de vehículos desde `autos.txt` y una máquina expendedora de relojes basada en `relojes.txt`.

Esta carpeta implementa únicamente el problema de vehículos. El ruteo y el sistema de relojes no tienen solución registrada.

## Explicación detallada

La lógica, los acumuladores, las búsquedas y las limitaciones se desarrollan en [EXPLICACIÓN.md](EXPLICACIÓN.md).

## Ejercicios

| Problema | Estado | Evidencia |
| --- | --- | --- |
| 1. Ruteo | No implementado | Solo está disponible `Ruteo.pdf`. |
| 2. Análisis de vehículos | Implementado y ejecutado | `src/Autos.py`. |
| 3. Tic Tac | No implementado | `relojes.txt` está disponible, pero no existe script. |

## Estructura de la solución

```text
P1 2023 VERANO/
├── PRUEBA.pdf
├── Ruteo.pdf
├── autos.txt
├── relojes.txt
└── Solución/
    ├── README.md
    ├── EXPLICACIÓN.md
    └── src/
        └── Autos.py
```

## Cómo ejecutar

La carpeta de trabajo debe ser `P1 2023 VERANO/`, porque el script abre `autos.txt` mediante una ruta relativa.

```powershell
python "Solución/src/Autos.py"
```

## Resultado esperado

El programa informa, por marca, el vehículo de mayor cilindrada, el más eficiente y los porcentajes por transmisión. Al final presenta tres estadísticas globales.

La ejecución finaliza correctamente con el archivo incluido. La salida conserva dos errores de presentación: imprime `$` en vez de `%` para transmisión automática y contiene la palabra `transmisicón`.

## Estado

- [x] Enunciado principal y ruteo disponibles.
- [x] Archivos de entrada disponibles.
- [x] Problema de vehículos implementado y ejecutado.
- [ ] Respuesta del ruteo documentada.
- [ ] Sistema de relojes implementado.

La evaluación no debe clasificarse como completa.
