#C1 PABLO GUZMÁN
"""
CINEMARK
"""

import numpy as np
sala = np.zeros([10,10])
columnas= [1,2,3,4,5,6,7,8,9,10]
filas = ["A","B","C","D","E","F","G","H","I","J"]
filasrecaudacion = [0,0,0,0,0,0,0,0,0,0]
filasperdidas = [0,0,0,0,0,0,0,0,0,0]

def burbuja(li1,li2):
    def intercambiar(i,j,li):
        aux = li[i]
        li[i] = li[j]
        li[j] = aux
        
    for i in range(len(li1)-1):
        for j in range(i,len(li1)):
            if li1[i] > li1[j]:
                intercambiar(i,j,li1)
                intercambiar(i,j,li2)
                
for i in range(len(filas)):
    for j in range(len(columnas)):
        
        sala[i][j] = -1
            
for i in range(len(filas)):
    for j in range(len(columnas)):
        
        if i % 2 == 0 and j % 2 != 0:
            sala[i][j] = 0
        if j % 2 == 0 and i % 2 != 0:
            sala[i][j] = 0
            
arch = open("ventas_avatar.txt","r",encoding="utf-8")
line = arch.readline().strip()

while line != "":
    parts = line.split(",")
    fila = parts[0]
    f = filas.index(fila)
    columna = int(parts[1])
    c = columnas.index(columna)
    
    tipo = parts[2]
    
    
    verificador = sala[f][c]
    if verificador == -1:
        print(f"no se puede vender en la fila {fila} el asiento {columna}")
        if tipo == "estandar": 
            filasperdidas[f] += 4500
        else:
            filasperdidas[f] += 6000
    else:
        if tipo == "estandar": 
            sala[f][c] = 1
            filasrecaudacion[f] += 4500
        else:
            sala[f][c] = 2
            filasrecaudacion[f] += 6000
    
    line = arch.readline().strip()

totalperdido = 0
for i in filasperdidas:
    totalperdido += i
    
print("-----------------------------------------------------------")

print(f"el total perdido por las restricciones es {totalperdido}")

for i in range(len(filas)):
    for j in range(len(columnas)):
        if sala[i][j] == -1:
           sala[i][j] = 0
           
           
print("-----------------------------------------------------------")   
print(sala)
print("-----------------------------------------------------------")

filamayor = 0
filamayorletra = ""
for i in range(len(filas)):
    if filasrecaudacion[i] > filamayor:
        filamayor = filasrecaudacion[i]
        filamayorletra = filas[i]
print(f"la fila que mas dinero recaudo fue la fila {filamayorletra}")

burbuja(filasperdidas,filas)

print("-----------------------------------------------------------")

for i in range(10):
    print(f"fila {filas[i]} : {filasperdidas[i]}")