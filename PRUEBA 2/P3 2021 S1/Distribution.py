#C1 Pablo Guzmán
"""
Created on Sun Jan 25 16:19:52 2026

@author: cythg
"""

import numpy as np

def verificarDespacho(fecha):
    for f in range(matriz.shape[0]):
        for c in range(matriz.shape[1]):
        
            if matriz[f][c] > 100:
                matriz[f][c] -= 100
                cantDepachos[f][c] += 1
                #Se realiza un despacho en A 1 el 2021-06-10
                print(f"Se realiza un despacho en {filas[f]} {c + 1} el {fecha}")
    
    
filas = ["A","B","C","D","E","F"]


matriz = np.zeros([6,6])
cantDepachos = np.zeros([6,6])

arch = open("recibidos.txt","r",encoding="utf-8")
linea = arch.readline().strip()

while linea != "":
    partes = linea.split(";")
    fecha = partes[0]
    filaColumna = partes[1]
    cantidad = int(partes[2])
    
    aux = filaColumna.split("-")
    fila = filas.index(aux[0])
    columna = int(aux[1]) - 1
    
    matriz[fila][columna] += cantidad
    
    verificarDespacho(fecha)
    
    linea = arch.readline().strip()

print(cantDepachos)
    
def calcularCostoTotal():
    contadorDespachos = 0
    acumuladorCosto = 0
    
    for c in range(6):
        for f in range(6):
            elemento = cantDepachos[f][c]
            contadorDespachos += elemento
            acumuladorCosto += elemento * costos[c]
    
    print(f"El costo total de los {contadorDespachos} despachos es {acumuladorCosto}")
    
costos = [125, 325, 198, 635, 312, 185]

calcularCostoTotal()

def busquedaMayoresPendientes():
    mayores = []
    mayor = -999
    
    for f in range(matriz.shape[0]):
        for c in range(matriz.shape[1]):
            posicion = f"{filas[f]} - {c + 1}"
            elemento = matriz[f][c]
            
            if elemento > mayor:
                
                mayores = [posicion]
                mayor = elemento
                
            elif elemento == mayor:
                mayores.append(posicion)
    
    printeo = ""
    for i in range(len(mayores)):
        printeo += f"{mayores[i]}"
        if i != len(mayores) - 1:
            printeo += ", "
    
    print(f"{printeo} con {mayor}")

busquedaMayoresPendientes()


def sumarFilas():
    
    for f in range(6):
        acumulador = 0
        for c in range(6):
            acumulador += matriz[f][c]
        itemsPendientes[f] = int(acumulador)
    
itemsPendientes = [0,0,0,0,0,0]
sumarFilas()

def intercambiar(i,j,li):
    aux = li[i]
    li[i] = li[j]
    li[j] = aux
    
def ordenar(li1,li2):
    for i in range(0, len(li1) - 1):
        
        for j in range(i + 1, len(li1)):
            
            if li1[i] < li1[j]:
                intercambiar(i, j, li1)
                intercambiar(i, j, li2)

ordenar(itemsPendientes, filas)

for i in range(len(filas)):
    print(f"Zona {filas[i]} - {itemsPendientes[i]}")








