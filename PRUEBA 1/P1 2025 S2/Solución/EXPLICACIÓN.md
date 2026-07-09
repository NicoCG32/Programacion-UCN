# Explicación Detallada - Prueba 1 2025 S2

## Objetivo

Explicar los dos programas disponibles, relacionarlos con el enunciado y precisar los requisitos pendientes.

## Modelo y flujo general

La solución contiene dos programas independientes:

```text
Tiendita.py -> interacción por consola -> boleta
Liga.py     -> partidos.txt -> estadísticas acumuladas
```

Ambos emplean programación estructurada: ciclos, condicionales, contadores, acumuladores y búsquedas de máximos.

## Sistema de boletas

### Control de acceso

Un `while` solicita la contraseña hasta recibir `venta2025`. La condición garantiza que el registro de productos no comienza antes de una autenticación correcta.

### Registro y descuentos

El nombre `fin` actúa como centinela. Para cada producto se obtiene cantidad, precio y decisión de descuento. El total bruto es:

```text
total = precio unitario * cantidad
```

Los descuentos de 2.250 y 5.500 se aplican en los intervalos establecidos. El subtotal acumula el valor después de descuento y el IVA acumulado equivale al 19 % de ese subtotal.

### Limitaciones

- No se rechazan cantidades o precios negativos.
- Si se solicita descuento para un total de 20.000 o más, el descuento permanece en cero, pero el texto indica “Aplicando descuento”.
- La boleta muestra el total bruto de cada producto, lo que es coherente con el ejemplo, pero no muestra el descuento por línea.

## Liga Civil UCN

### Lectura por bloques

Cada jornada declara nombre, cantidad de partidos y fecha. El `for` interior consume exactamente esa cantidad de registros. Este patrón evita confundir cabeceras con partidos.

### Estadísticas

El programa calcula:

- Partidos, goles, empates y victorias locales.
- Victorias de Sumario FC como local o visitante.
- Mayor cantidad de goles de un equipo en un partido.
- Tarjetas por jornada y totales.
- Frecuencia de uso de los cuatro estadios.
- Jornada más goleadora.

Las búsquedas de máximos actualizan valor y etiqueta al encontrar un candidato mayor.

### Limitaciones

- `promedioGoles`, porcentaje local y `promTarjetas` no se redondean a dos decimales.
- La selección del estadio usa comparaciones rígidas y no contempla empates.
- El archivo se abre sin `with`.

## Correctitud y complejidad

Para `n` productos, `Tiendita.py` usa tiempo `O(n)` y memoria `O(n)` por la cadena de boleta. Para `m` partidos, `Liga.py` usa tiempo `O(m)` y memoria adicional `O(1)`.

Los cálculos de la liga reproducen los valores del archivo incluido. Las diferencias observadas son de formato decimal y robustez ante casos no presentes.

## Cobertura del enunciado

Los ejercicios A y B de `Ruteo.pdf` no están resueltos. Por ello la evaluación completa permanece parcial aunque los dos scripts existentes sean ejecutables.

## Cómo verificar la solución

Desde `P1 2025 S2/`:

```powershell
python "Solución/src/Liga.py"
python "Solución/src/Tiendita.py"
```

Para una prueba mínima de la tienda, ingrese `venta2025` y luego `fin`. Debe producir una boleta sin productos y total cero.
