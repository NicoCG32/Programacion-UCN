# -*- coding: utf-8 -*-
"""
LISTAS PARALELAS, JUEGO DE INDICES Y LÓGICA DE SUBPROGRAMAS (FÁCIL)
"""

def cargarLiga():
    arch = open("equipos.txt","r",encoding="utf-8")
    linea = arch.readline().strip()
    
    while linea != "":
        partes = linea.split(",")
        
        equipo = partes[0]
        ganados = int(partes[1])
        empates = int(partes[2])
        perdidos = int(partes[3])
        
        golesAFavor = int(partes[4])
        golesEnContra = int(partes[5])
        
        equipos.append(equipo)
       
        PG.append(ganados)
        PE.append(empates)
        PP.append(perdidos)
        GA.append(golesAFavor)
        GC.append(golesEnContra)
        
        linea = arch.readline().strip()
        
#Workspace, para almacenamiento de datos
equipos = []
PG = []
PE = []
PP = []
GA = []
GC = []

cargarLiga()

def calcularPuntaje(indice):
    return PG[indice] * 3 + PE[indice]

def calcularDif(indice):
    return GA[indice] - GC[indice]

def imprimirDatos():
    for i in range(len(equipos)):
        puntaje = calcularPuntaje(i)
        dif_goles = calcularDif(i)
        
        print(f"{equipos[i]} | {puntaje} PTS | {dif_goles} Diferencia de Goles | {PG[i]} Victorias")

#Antes de actualizar
print("ANTES")
imprimirDatos()

def buscarEquipo(equipo):
    for i in range(len(equipos)):
        if equipos[i] == equipo:
            return i
    return -1 #Nunca va a pasar en este caso

def cargarPartidos():
    arch = open("partidos.txt","r",encoding="utf-8")
    linea = arch.readline().strip()
    
    while linea != "":
        partes = linea.split(",")
        
        equipoA = partes[0]
        golesA = int(partes[1])
        equipoB = partes[2]
        golesB = int(partes[3])
        
        indice_A = buscarEquipo(equipoA)
        indice_B = buscarEquipo(equipoB)
        
        if golesA > golesB:
            PG[indice_A] += 1
            PP[indice_B] += 1
            
        if golesB > golesA:
            PG[indice_B] += 1
            PP[indice_A] += 1
            
        if golesA == golesB:
            PE[indice_A] += 1
            PE[indice_B] += 1
            
        GA[indice_A] += golesA
        GC[indice_A] += golesB
        
        GA[indice_B] += golesB
        GC[indice_B] += golesA
        
        linea = arch.readline().strip()
        
cargarPartidos()
#Todos los datos cargados, empezamos con los algoritmos

#Después de actualizar
print()
print("DESPUÉS")
imprimirDatos()

def buscarMayores(lista, ver):
    mayor = -999
    mayores = []
    for i in range(len(lista)):
        equipoI = lista[i] #para que se entienda que equipo revisamos
        
        if ver == 1:
            criterio = calcularPuntaje(i)
        elif ver == 2:
            criterio = calcularDif(i)
        else:
            criterio = PG[i]
        
        if criterio > mayor:
            mayor = criterio
            mayores = [i]
        elif criterio == mayor:
            mayores.append(i)
    
    return mayores

def imprimirCampeon(indices_mayores):
    mensaje = ""
    if len(indices_mayores) != 1:
        for i in range(len(indices_mayores)):
            mensaje += f"{equipos[indices_mayores[i]]}"
            if i == len(indices_mayores) - 1:
                mensaje += " " #Ultimo
            elif i == len(indices_mayores) - 2:
                mensaje += " y " #Penúltimo
            else:
                mensaje += ", " #Otro
        mensaje += "son campeones de la liga regional de Coquimbo"
    else:
        mensaje += f"{equipos[indices_mayores[0]]} es el campeón de la liga regional de Coquimbo"
    
    print(mensaje)

def buscarGanador():
    mayores = buscarMayores(equipos, 1)
    if len(mayores) > 1:
        mayores = buscarMayores(equipos, 2)
    if len(mayores) > 1:
        mayores = buscarMayores(equipos, 3)
    
    imprimirCampeon(mayores)

print()
print("GANADOR:")
buscarGanador()

    
#Ordenar
def intercambiar(i, j, lista):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
    
def ordenar():
    for i in range(0, len(equipos) - 1):
        for j in range(i + 1, len(equipos)):
            if calcularPuntaje(i) < calcularPuntaje(j):
                intercambiar(i, j, equipos)
                intercambiar(i, j, PG)
                intercambiar(i, j, PE)
                intercambiar(i, j, PP)
                intercambiar(i, j, GA)
                intercambiar(i, j, GC)
                
print()
print("TABLA FINAL ORDENADA")
ordenar()
imprimirDatos()


