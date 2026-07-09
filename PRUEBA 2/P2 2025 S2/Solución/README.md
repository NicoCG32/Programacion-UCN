# Solución - Prueba 2 - 2025 S2

**Asignatura**: Programación

**Período**: 2025 S2

**Tipo**: Prueba 2, partes 1 y 2

**Estado**: Parcial

## Descripción

La parte 1 solicita procesar 350 archivos de lotes y producir cuatro reportes. La parte 2 solicita clasificación acumulada, adelantamientos y vuelta rápida del GP Huachalalume.

`Lotes.py` cubre parte del primer problema. No existe solución para el Grand Prix.

## Explicación detallada

La estructura de matrices, listas paralelas y recorrido de archivos se explica en [EXPLICACIÓN.md](EXPLICACIÓN.md).

## Ejercicios

| Requisito | Estado |
| --- | --- |
| Coste de cada lote | Implementado. |
| Unidades producidas por producto | Acumulado internamente, pero no impreso. |
| Valor total del inventario | Implementado, sin redondeo de presentación. |
| Producción por año y producto | No implementado. |
| GP Huachalalume | No implementado. |

## Estructura de la solución

```text
P2 2025 S2/
├── archivos.zip
├── gp.txt
├── PRUEBA - PARTE 1.pdf
├── PRUEBA - PARTE 2.pdf
├── Ejecucion_completa.txt
├── salida.txt
└── Solución/
    ├── README.md
    ├── EXPLICACIÓN.md
    └── src/
        └── Lotes.py
```

## Cómo ejecutar

1. Descomprime `archivos.zip`.
2. Usa la carpeta extraída `archivos/` como directorio de trabajo.
3. Ejecuta el script mediante su ruta completa o cópialo temporalmente dentro de esa carpeta.

Ejemplo conceptual:

```powershell
Set-Location archivos
python "../Solución/src/Lotes.py"
```

La ruta relativa exacta depende de dónde se extraiga el ZIP.

## Resultado esperado

El programa recorre los lotes declarados en `indice.txt`, imprime el coste de cada uno y finalmente el valor potencial del inventario. Con los datos incluidos termina sin excepciones.

## Estado

- [x] Enunciados y archivos de apoyo disponibles.
- [x] Carga de índices, precios y lotes.
- [x] Coste por lote.
- [x] Valor total del inventario.
- [ ] Listado impreso de unidades por producto.
- [ ] Agrupación por año.
- [ ] Solución de GP Huachalalume.

La evaluación es parcial.
