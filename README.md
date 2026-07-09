# Programación - UCN

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Spyder](https://img.shields.io/badge/IDE-Spyder%20%28Anaconda%29-8C0000?logo=spyderide&logoColor=white)
![Anaconda](https://img.shields.io/badge/Distribuci%C3%B3n-Anaconda-44A833?logo=anaconda&logoColor=white)
![Nivel](https://img.shields.io/badge/Nivel-0%20Programaci%C3%B3n%20estructurada-lightgrey)

Repositorio de apoyo para el curso **Programación** de la Universidad Católica del Norte.

Este curso corresponde a la base de la formación: aprender a escribir instrucciones, entender el flujo de ejecución, usar variables, condiciones, ciclos, funciones, archivos, listas y matrices, y construir algoritmos simples que transforman una entrada en una salida.

## Entorno del curso

El curso se desarrolla en **Python**, normalmente usando **Spyder desde Anaconda**. La versión exacta de Python no es especialmente relevante para este material, porque se trabajan elementos básicos del lenguaje: entrada y salida, variables, condicionales, ciclos, funciones, archivos, listas y matrices.

Spyder es útil en este nivel porque permite ejecutar programas completos, revisar variables, probar fragmentos de código y observar errores de forma relativamente clara para estudiantes que están comenzando.

## Estructura

```text
Programacion-UCN/
├── Ayudantías/
├── PRUEBA 1/
├── PRUEBA 2/
├── RECA/
└── README.md
```

Cada evaluación puede contener:

- `PRUEBA.pdf`, `PRUEBA - PARTE 1.pdf`, `PRUEBA - PARTE 2.pdf` o `Ruteo.pdf`: enunciados y material de evaluación.
- Archivos `.txt`: datos de entrada usados por los programas.
- Archivos `.zip`: paquetes de archivos auxiliares, cuando corresponde.
- `Solución/README.md`: cobertura del enunciado y estado verificable.
- `Solución/EXPLICACIÓN.md`: explicación de código, algoritmos, supuestos y limitaciones.
- `Solución/src/`: scripts Python.

En ayudantías, `README.md` y `EXPLICACIÓN.md` permanecen junto a los scripts porque cada carpeta representa directamente una actividad y no una evaluación formal.

## Material disponible

### Ayudantías

| Carpeta | Contenido principal |
| --- | --- |
| [Ayudantías](<Ayudantías/README.md>) | Material elaborado para practicar condicionales, ciclos, algoritmos básicos, subprogramas y listas. |

### Prueba 1

| Periodo | Estado | Contenido principal |
| --- | --- | --- |
| [P1 2025 S2](<PRUEBA 1/P1 2025 S2/Solución/README.md>) | Parcial | Boletas y liga implementadas; ruteo y VetSalud pendientes. |
| [P1 2023 VERANO](<PRUEBA 1/P1 2023 VERANO/Solución/README.md>) | Parcial | Vehículos implementado; ruteo y máquina de relojes pendientes. |

### Prueba 2

| Periodo | Estado | Contenido principal |
| --- | --- | --- |
| [P2 2025 S2](<PRUEBA 2/P2 2025 S2/Solución/README.md>) | Parcial | Lotes parcialmente implementado; GP Huachalalume pendiente. |
| [SIM P2 2024 S2](<PRUEBA 2/SIM P2 2024 S2/Solución/README.md>) | Implementada con observaciones | Tapper y Cinemark. |
| [P3 2021 S1](<PRUEBA 2/P3 2021 S1/Solución/README.md>) | Completa para los datos entregados | Supermercados y distribución. |

### RECA

| Periodo | Estado | Contenido principal |
| --- | --- | --- |
| [RECA 2025 S2](<RECA/RECA 2025 S2/Solución/README.md>) | Parcial | Simulación básica disponible; estadísticas globales y Facturando pendientes. |

## Cómo ejecutar las soluciones

Las soluciones están escritas en Python. La forma más cercana al curso es ejecutarlas desde **Spyder**:

1. Abre Anaconda Navigator.
2. Inicia Spyder.
3. Abre el archivo `.py` desde `Solución/src/`.
4. Configura como carpeta de trabajo la raíz de la evaluación, donde se encuentran los `.txt`.
5. Ejecuta el programa desde Spyder.

También puedes ejecutar los archivos desde terminal si tienes Python configurado:

Ejemplo general desde la raíz de una evaluación:

```bash
python "Solución/src/archivo.py"
```

Para ejercicios con NumPy:

```bash
pip install numpy
python archivo.py
```

## Temario del curso

| Clase | Contenidos principales |
| --- | --- |
| 1 | Tipos de datos `bool`, `int`, `float` y `str`; `print`; `input`; casteo con `str`, `int` y `float`; operadores aritméticos; comparadores; condicionales `if`, `elif` y `else`. |
| 2 | Ciclos indefinidos con `while`; ciclos definidos con `for` y `range`; control de repeticiones. |
| 3 | Algoritmos básicos: guardar el mayor, guardar el menor, usar contadores, acumular valores y calcular promedios. |
| 4 | Lectura de archivos `.txt`; uso de `open`, `readline`, `strip` y `split`; tratamiento de líneas de texto. |
| 5 | Patrones de recorrido de archivos: cantidad indeterminada de líneas, cantidad determinada de líneas y archivos compuestos por bloques. |
| 6 | Subprogramas: procedimientos, funciones, parámetros, retorno de valores y separación básica de responsabilidades. |
| 7 | Variables globales, listas, `append`, `pop`, eliminación de elementos, índices positivos e índices negativos. |
| 8 | Algoritmos con listas: máximo, mínimo, promedio, conteo, ordenamiento burbuja, intercambio de posiciones y funciones auxiliares. |
| 9 | Matrices con NumPy, creación con `np.zeros`, acceso por fila y columna, y representación de datos bidimensionales. |
| 10 | Algoritmos con matrices: recorridos, intercambio de filas, intercambio de columnas, búsqueda y procesamiento por posición. |

## Contenidos esperados por evaluación

### Primera prueba

Generalmente llega hasta subprogramas y lectura de archivos.

Lógicas típicas:

- Búsqueda del mayor.
- Búsqueda del menor.
- Conteo total para proporciones o porcentajes.
- Cálculo de promedios.
- Uso de la lógica del valor previo.
- Cálculo de fórmulas dadas por el enunciado.
- Procesamiento de archivos con estructura fija, variable o por bloques.

### Segunda prueba

Generalmente incorpora listas, ordenamiento, matrices y problemas integradores.

Lógicas típicas:

- Búsqueda del mayor y de los `N` mayores.
- Búsqueda del menor y de los `N` menores.
- Conteo total, proporciones y porcentajes.
- Promedios y fórmulas definidas por el enunciado.
- Listas paralelas para representar datos compuestos mediante índices.
- Ordenamiento según uno o más criterios.
- Matrices paralelas y recorridos por fila/columna.
- Simulaciones con estado, turnos o posiciones.

## Cómo estudiar este material

1. Identifica claramente qué datos entran al programa.
2. Describe el proceso antes de escribir código.
3. Separa el problema en pasos pequeños.
4. Prueba con casos simples, casos borde y casos inválidos si corresponde.
5. Revisa si la salida coincide exactamente con lo solicitado.

La idea central del curso no es memorizar programas completos, sino reconocer patrones de solución: contar, acumular, buscar, comparar, recorrer, ordenar y transformar datos.

## Nota sobre niveles de abstracción

Programación ocupa el **nivel 0** de abstracción dentro de la progresión de cursos. En este punto se trabaja muy cerca del código: instrucciones, líneas, variables, condiciones, ciclos y funciones.

La lógica dominante suele verse así:

```text
input -> proceso 1 -> proceso 2 -> proceso 3 -> output
```

Por eso se habla de programación estructurada: el programa se entiende como una secuencia ordenada de pasos. La abstracción todavía es baja o casi nula; el estudiante memoriza, entiende y aplica líneas de código para resolver problemas concretos.

Este nivel es necesario. Sin esta base no es razonable saltar a clases, objetos, estructuras de datos o patrones de software. Sin embargo, también es importante entender su límite: si solo piensas en instrucciones aisladas, sigues pensando como programador inicial. Los cursos posteriores exigen subir el nivel de abstracción.

| Nivel | Curso o enfoque | Forma principal de pensar |
| --- | --- | --- |
| 0 | [Programación](https://github.com/NicoCG32/Programacion-UCN) | Líneas de código, instrucciones, pasos directos y algoritmos básicos. |
| 1 | [Programación Orientada a Objetos](https://github.com/NicoCG32/Programacion-Orientada-a-Objetos-UCN) y [Técnicas y Metodologías](https://github.com/NicoCG32/Tecnicas-y-Metodologias-de-Programacion-Avanzada-UCN) | Dominio, clases, objetos, relaciones y componentes básicos. |
| 2 | [Estructura de Datos](https://github.com/NicoCG32/Estructura-de-Datos-UCN) | Contenedores, organización de datos, invariantes y algoritmos sobre estructuras. |
| 3 | [Patrones de Software y Programación](https://github.com/NicoCG32/Patrones-de-Software-y-Programacion-UCN) | Componentes, composición de clases, dependencias y arquitectura de software. |

En síntesis: Programación enseña a construir el paso a paso. Los cursos siguientes enseñan a organizar esos pasos dentro de modelos, estructuras y sistemas más grandes.
