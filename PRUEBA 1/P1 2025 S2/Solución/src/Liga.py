# Paralelo C6 - Pablo Guzmán
"""
Created on Thu Oct 30 15:28:36 2025

@author: cythg
"""

archivo = open("partidos.txt", "r", encoding="utf-8")
linea = archivo.readline().strip()

#Variables necesarias

#contadores
cantidad_total_partidos = 0
victorias_sumario = 0
cantidad_total_goles = 0

empates = 0
victorias_eq_local = 0

total_amarillas = 0
total_rojas = 0

#estadios
coloso = 0
sanchez = 0
la_portada = 0
municipal = 0

#busqueda mayor
mayor_cant_goles = -99999
equipo_mayor_cant_goles = ""

mayor_tarjetas_jornada = -9999
jornada_mayor_tarjetas = ""

cant_goles_jornada_mayor_goles = -999999
fecha_mayor_goles = ""

while linea != "":
    
    partes = linea.split(";")
    
    jornada = partes[0]
    cant_partidos = int(partes[1])
    fecha = partes[2]
    
    cantidad_total_partidos += cant_partidos
    
    total_tarjetas_jornada = 0
    total_goles_jornada = 0
    
    print(f"Procesando {jornada} ({fecha}) con {cant_partidos} partidos")
    print()
    
    for i in range(cant_partidos):
        linea = archivo.readline().strip()
        
        partes = linea.split(",")
        eq_local = partes[0]
        eq_vis = partes[1]
        
        GolesL = int(partes[2])
        GolesV = int(partes[3])
        Amarillas = int(partes[4])
        Rojas = int(partes[5])
        estadio = partes[6]
        
        if eq_local == "Sumario FC":
            if GolesL > GolesV:
                victorias_sumario += 1
                
        if eq_vis == "Sumario FC":
            if GolesL < GolesV:
                victorias_sumario += 1
        
        cantidad_total_goles += GolesL + GolesV
        
        if GolesL > mayor_cant_goles:
            mayor_cant_goles = GolesL
            equipo_mayor_cant_goles = eq_local
        
        if GolesV > mayor_cant_goles:
            mayor_cant_goles = GolesV
            equipo_mayor_cant_goles = eq_vis
        
        if GolesL == GolesV:
            empates += 1
        
        if GolesL > GolesV:
            victorias_eq_local += 1
            
        total_amarillas += Amarillas
        total_rojas += Rojas
        
        total_tarjetas_jornada += Amarillas + Rojas
        
        
        
        if estadio == "Coloso De Guayacan":
            coloso += 1
        if estadio == "Sanchez Rumoroso":
            sanchez += 1
        if estadio == "La Portada":
            la_portada += 1
        if estadio == "Estadio Municipal":
            municipal += 1
         
        total_goles_jornada += GolesL + GolesV
    
    if total_tarjetas_jornada > mayor_tarjetas_jornada:
        mayor_tarjetas_jornada = total_tarjetas_jornada
        jornada_mayor_tarjetas = jornada
    
    if total_goles_jornada > cant_goles_jornada_mayor_goles:
        cant_goles_jornada_mayor_goles = total_goles_jornada
        fecha_mayor_goles = fecha
    
    
    linea = archivo.readline().strip()
    
#Fin de Ciclo

print("=================================")
print("ESTADÍSTICAS COMPLETAS LIGA CIVIL UCN 2032")
print("=================================")

#CALCULO DE PROMEDIOS, ideal asegurarse de que no haya divisiones por 0
promedioGoles = cantidad_total_goles / cantidad_total_partidos
porc_victorias_eq_local = (victorias_eq_local / cantidad_total_partidos) * 100

promTarjetas = (total_amarillas + total_rojas) / cantidad_total_partidos

mayor_estadio = ""
mayor_cant_estadio = 0
if coloso > sanchez and coloso > la_portada and coloso > municipal:
    mayor_estadio = "Coloso de Guayacán"
    mayor_cant_estadio = coloso
elif sanchez > la_portada and sanchez > municipal:
    mayor_estadio = "Sanchez Rumoroso"
    mayor_cant_estadio = sanchez
elif la_portada > municipal:
    mayor_estadio = "La Portada"
    mayor_cant_estadio = la_portada
else:
    mayor_estadio = "Estadio Municipal"
    mayor_cant_estadio = municipal
    
"""
1. Total de partidos jugados: 24
2. Victorias de Sumario FC: 5
3. Promedio de goles por partido: 4.08
4. Mejor ataque del torneo: Sumario FC (6 goles en un partido)
5. Total de empates: 4
6. Porcentaje de victorias locales: 45.83%
--- ESTADÍSTICAS DISCIPLINARIAS ---
7. Total de tarjetas amarillas: 58
8. Total de tarjetas rojas: 5
9. Jornada más indisciplinada: Jornada3 (20 tarjetas)
11. Promedio de tarjetas por partido: 2.62
--- ESTADÍSTICAS DE ESTADIOS ---
10. Estadio con más partidos: Coloso De Guayacan (11 partidos)
--- ESTADÍSTICAS POR FECHA ---
12. Fecha de la jornada más goleadora: 05-04-2032 (27 goles totales)
"""

#POSDATA, faltan los rounds nomás
print()
print("--- ESTADÍSTICAS GENERALES ---")

print(f"1. Total de partidos jugados: {cantidad_total_partidos}")
print(f"2. Victorias de Sumario FC: {victorias_sumario}")
print(f"3. Promedio de goles por partido: {promedioGoles}")
print(f"4. Mejor ataque del torneo: {equipo_mayor_cant_goles} ({mayor_cant_goles} goles en un partido)")
print(f"5. Total de empates: {empates}")
print(f"6. Porcentaje de victorias locales: {porc_victorias_eq_local} %")

print()
print("--- ESTADÍSTICAS DISCIPLINARIAS ---")
print(f"7. Total de tarjetas amarillas: {total_amarillas}")
print(f"8. Total de tarjetas rojas: {total_rojas}")
print(f"9. Jornada más indisciplinada: {jornada_mayor_tarjetas} ({mayor_tarjetas_jornada} tarjetas)")
print(f"11. Promedio de tarjetas por partido: {promTarjetas}")

print()
print("--- ESTADÍSTICAS DE ESTADIOS ---")
print(f"10. Estadio con más partidos: {mayor_estadio} ({mayor_cant_estadio} partidos)")

print()
print("--- ESTADÍSTICAS POR FECHA ---")
print(f"12. Fecha de la jornada más goleadora: {fecha_mayor_goles} ({cant_goles_jornada_mayor_goles} goles totales)")
