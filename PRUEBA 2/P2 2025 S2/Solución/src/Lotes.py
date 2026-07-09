#C1 Pablo Guzmán
"""
Created on Fri Jan 23 13:29:13 2026

@author: cythg
"""
import numpy as np

def CrearMatriz():
    
    arch = open("indice.txt","r", encoding="utf-8")
    linea = arch.readline().strip()
    partes = linea.split(",")
    
    cant_filas = int(partes[0])
    cant_col = int(partes[1])
    
    matriz = np.zeros([cant_filas,cant_col])
    
    for f in range(cant_filas):
        linea = arch.readline().strip()
        partes = linea.split(",")
        for c in range(cant_col):
            matriz[f][c] = int(partes[c])
            
    return matriz
        
def leerProductos():
    
    arch = open("precios.txt", "r", encoding="utf-8")
    linea = arch.readline().strip()  
    
    while linea != "":
        partes = linea.split(",")
        producto = partes[0]
        valor = float(partes[1])
        
        productos.append(producto)
        valor_unitario.append(valor)
        linea = arch.readline().strip()  

def BuscarIndiceElemento(elemento, li):
    for i in range(len(li)):
        if li[i] == elemento:
            return i
        
def leerArchivo(ruta):
    
    arch = open(ruta + ".txt", "r", encoding="utf-8")
    linea = arch.readline().strip()
    
    fecha = linea
    
    linea = arch.readline().strip()
    
    acumulador = 0
    
    while linea != "":
        partes = linea.split(",")
        producto = partes[0]
        indice_prod = BuscarIndiceElemento(producto, productos)
        
        cantidadProducida = int(partes[1])
        unidadesProducidas[indice_prod] += cantidadProducida
        costeTotal = float(partes[2])
        
        acumulador += costeTotal
        linea = arch.readline().strip()
    
    print(f"{ruta} : {round(acumulador,2)}")
    arch.close()
        
matriz = CrearMatriz()

productos = []
valor_unitario = []


leerProductos()

unidadesProducidas = []
for i in range(len(productos)): #Para llenar
    unidadesProducidas.append(0)

for f in range(matriz.shape[0]):
    for c in range(matriz.shape[1]):
        for k in range(int(matriz[f][c])):
            ruta = f"{f}-{c}-{k + 1}"
            leerArchivo(ruta)
            
    
recaudado = 0
for i in range(len(productos)):
    recaudado += valor_unitario[i] * unidadesProducidas[i]

print(recaudado)













