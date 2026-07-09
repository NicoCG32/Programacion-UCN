# Explicación Detallada - RECA 2025 S2

## Objetivo

Explicar la simulación implementada de Escaleras y Serpientes y documentar con precisión lo que falta para completar ambas partes.

## Modelo de la simulación

`posiciones` es una matriz que traduce coordenadas a una posición lineal. `llenarPosiciones()` alterna la dirección en cada fila para representar el recorrido bidireccional.

Los jugadores y sus posiciones se mantienen en listas paralelas:

```text
jugadores[i] <-> lista_posiciones[i]
```

Las entradas y salidas de atajos también se almacenan como listas paralelas.

## Algoritmo implementado

### Lectura del tablero

`detectarEntradasYSalidas()` clasifica etiquetas en origen y destino. `rellenarEntradasYSalidas()` asocia etiquetas iguales ignorando mayúsculas, y convierte coordenadas en posiciones lineales.

### Avance

`sumarAPosicionUnJugador()` procesa el dado de cada jugador. Solo actualiza la posición si no supera la meta. Si llega exactamente, informa que ganó.

### Atajos

`escalerasOserpientes()` busca la posición actual en `entradas`. Si existe, reemplaza la posición por la salida y distingue avance de retroceso.

### Clasificación

`clasificacion()` ordena posiciones y nombres en paralelo de mayor a menor. Actualmente se ejecuta una vez después de consumir todas las vueltas de cada partida.

## Correctitud y complejidad

Para `j` jugadores, `t` vueltas y `a` atajos, el movimiento cuesta aproximadamente `O(t * j * a)` debido a búsquedas lineales. Un diccionario de origen a destino reduciría la búsqueda de atajos.

La numeración bidireccional y la regla de no sobrepasar la meta están implementadas. La ejecución con `tablero.txt` termina sin excepciones.

## Requisitos pendientes

La parte 1 exige más comportamiento:

- Clasificación tras cada vuelta.
- Mensaje cuando no hay movimientos significativos.
- Finalización e identificación formal de ganador y vuelta.
- Ranking global por victorias y desempate.
- Lista de jugadores nunca ganadores.
- Ganancia neta por escaleras y pérdida por serpientes.

La parte 2 no tiene script para procesar `transacciones.txt`.

## Cómo verificar la solución

Desde la carpeta de evaluación:

```powershell
python "Solución/src/SerpientesEscaleras.py"
```

Compare el recorrido local con los archivos de salida, pero no interprete la ejecución exitosa como cobertura total: los reportes consolidados aún no existen.
