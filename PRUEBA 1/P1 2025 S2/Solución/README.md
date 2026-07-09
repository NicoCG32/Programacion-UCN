# Solución - Prueba 1 - 2025 S2

**Asignatura**: Programación

**Período**: 2025 S2

**Tipo**: Prueba 1

**Estado**: Parcial

## Descripción

La evaluación se divide entre ruteo y reporte veterinario en `Ruteo.pdf`, y sistema de boletas más análisis de liga en `PRUEBA.pdf`.

La solución implementa el sistema de boletas y la Liga Civil UCN. No incluye respuesta para el ruteo ni programa para `pacientes.txt`.

## Explicación detallada

Consulta [EXPLICACIÓN.md](EXPLICACIÓN.md) para revisar los ciclos, acumuladores, validaciones, procesamiento por bloques y diferencias frente al enunciado.

## Ejercicios

| Ejercicio | Estado | Archivo |
| --- | --- | --- |
| A. Ruteo | No implementado | No hay respuesta registrada. |
| B. VetSalud | No implementado | No se incluye `pacientes.txt` ni script. |
| C. Sistema de boletas | Implementado con observaciones | `src/Tiendita.py`. |
| 3. Liga Civil UCN | Implementado y ejecutado | `src/Liga.py`. |

## Estructura de la solución

```text
P1 2025 S2/
├── PRUEBA.pdf
├── Ruteo.pdf
├── partidos.txt
└── Solución/
    ├── README.md
    ├── EXPLICACIÓN.md
    └── src/
        ├── Liga.py
        └── Tiendita.py
```

## Cómo ejecutar

Usar la carpeta de evaluación como directorio de trabajo:

```powershell
python "Solución/src/Liga.py"
python "Solución/src/Tiendita.py"
```

`Tiendita.py` requiere interacción por consola. `Liga.py` lee `partidos.txt`.

## Resultado esperado

`Liga.py` termina sin excepciones y obtiene los valores del ejemplo. Algunos promedios se imprimen con más de dos decimales.

`Tiendita.py` permite registrar productos, aplicar descuentos, calcular IVA y emitir una boleta. No valida cantidades ni precios negativos, aunque el enunciado lo exige.

## Estado

- [x] PDF de ambas partes disponible.
- [x] Sistema de boletas implementado.
- [x] Análisis de liga implementado y ejecutado.
- [ ] Validación de cantidades y valores negativos.
- [ ] Redondeo final conforme al ejemplo.
- [ ] Ruteo y VetSalud resueltos.

La cobertura actual es parcial.
