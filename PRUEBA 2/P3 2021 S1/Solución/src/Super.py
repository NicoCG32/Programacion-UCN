#C1 Pablo Guzmán 54146125-3
"""
Created on Sun Jan 25 14:47:27 2026

@author: cythg
"""
import numpy as np
def leerPrecios():
    arch = open("precios.txt", "r", encoding="utf-8")
    
    linea = arch.readline().strip()
    
    fila = 0
    
    while linea != "":
    
        partes = linea.split("-")
        producto = partes[0]
        
        precioDumbo = int(partes[1])
        precioSaint = int(partes[2])
        precioDuomarc = int(partes[3])
        
        ProductosXSupermercado[fila][0] = precioDumbo
        ProductosXSupermercado[fila][1] = precioSaint
        ProductosXSupermercado[fila][2] = precioDuomarc
        
        Productos.append(producto)
        
        fila += 1
        linea = arch.readline().strip()
        
ProductosXSupermercado = np.zeros([50,3])

Productos = []
Supermercados = ["Dumbo","Saint Elizabeth","Duomarc"]


leerPrecios()

def buscarMenorPrecio(indice, cantidad):
    precioDumbo = ProductosXSupermercado[indice][0]
    precioSaint = ProductosXSupermercado[indice][1]
    precioDuomarc = ProductosXSupermercado[indice][2]
    
    if precioDumbo < precioSaint and precioDumbo < precioDuomarc:
        cantidades[indice][0] += cantidad
        return precioDumbo
    elif precioSaint < precioDuomarc:
        cantidades[indice][1] += cantidad
        return precioSaint
    else:
        cantidades[indice][2] += cantidad
        return precioDuomarc
    
cantidades = np.zeros([50,3])

#LEYENDO recetas.txt

arch = open("recetas.txt","r", encoding="utf-8")
linea = arch.readline().strip()

recetas = []
precioReceta = []
indiceReceta = -1
while linea != "":
    partes = linea.split("-")
    
    receta = partes[0]
    cantidad = int(partes[1])
    
    recetas.append(receta)
    precioReceta.append(0)
    indiceReceta += 1
    for i in range(2, len(partes)):
        ingrediente = partes[i]
        
        indice = Productos.index(ingrediente)
        precio = buscarMenorPrecio(indice, cantidad)
        precioReceta[indiceReceta] += precio
    
    linea = arch.readline().strip()
    

for i in range(len(Supermercados)):
    print(Supermercados[i] + ":")
    for f in range(len(Productos)):
        elemento = int(cantidades[f][i])
        if elemento != 0:
            producto = Productos[f]
            
            print(f"- {producto}: {elemento}")
        

for i in range(len(Supermercados)):
    acumulador = 0
    
    for f in range(len(Productos)):
        if cantidades[f][i] != 0:
            acumulador += cantidades[f][i] * ProductosXSupermercado[f][i]
    
    print(f"{Supermercados[i]}: ${int(acumulador)}")

for i in range(len(recetas)):
    print(f"{recetas[i]}: {int(precioReceta[i])}")
    
    