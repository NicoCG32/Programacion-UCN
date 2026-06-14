#C1 PABLO GUZMÁN
"""
TAPPER EL JUEGO
"""

arch = open("entregas.txt","r",encoding="utf-8")
line = arch.readline().strip()

def contadormaximos(li):
    maximo = li[0]
    maximos = 0
    for i in li:
        if i == maximo:
            maximos += 1
    return maximos

def contadorminimos(li):
    minimo = li[-1]
    minimos = 0
    for i in li:
        if i == minimo:
            minimos += 1
    return minimos

def burbuja(li1,li2,li3,li4):
    def intercambiar(i,j,li):
        aux = li[i]
        li[i] = li[j]
        li[j] = aux
        
    for i in range(len(li1)-1):
        for j in range(i,len(li1)):
            if li1[i] > li1[j]:
                intercambiar(i,j,li1)
                intercambiar(i,j,li2)
                intercambiar(i,j,li3)
                intercambiar(i,j,li4)
                
def burbujamenor(li1,li2):
    def intercambiar(i,j,li):
        aux = li[i]
        li[i] = li[j]
        li[j] = aux
        
    for i in range(len(li1)-1):
        for j in range(i,len(li1)):
            if li1[i] < li1[j]:
                intercambiar(i,j,li1)
                intercambiar(i,j,li2)

def miniburbuja(li1,li2):
    def intercambiar(i,j,li):
        aux = li[i]
        li[i] = li[j]
        li[j] = aux
        
    for i in range(len(li1)-1):
        for j in range(i,len(li1)):
            if li1[i] > li1[j]:
                intercambiar(i,j,li1)
                intercambiar(i,j,li2)
                
def imprimir(lista):
    contB = 0
    contC = 0
    for i in lista:
        if i == "B":
            contB += 1
        if i == "C":
            contC += 1
            
    if contC > 0:
        print(f"{contC} Cervezas")
    if contB > 0:
        print(f"{contB} Bebidas")
    print("-----------------------------------------------------------")
                
barras = []
barragan = []
barrasrestante = []
barrascontador = []

B = 0
C = 0
T = 0

GananB = 0
GananC = 0
GananT = 0

def detector(lista):
    aux = []
    for i in lista:
        aux.append(i)
        
    if aux[-1] == "T":
        lista.pop()
        return 5000
    
    if len(aux) >= 2:
        if aux[-1] == "C":
            aux.pop()
            if aux[-1] == "C":
                lista.pop()
                lista.pop()
                return 7000
    
    if len(aux) >= 3:
        if aux[-1] == "B":
            aux.pop()
            if aux[-1] == "B":
                aux.pop()
                if aux[-1] == "B":
                    lista.pop()
                    lista.pop()
                    lista.pop()
                    return 3000
    return 0

GananBTotal = 0
GananCTotal = 0
GananTTotal = 0

while line != "":
    parts = line.split(",")
    barra = parts[0]
    
    barraactiva = []
    
    if barra not in barras:
        barras.append(barra)
        barragan.append(0)
        barrasrestante.append([])
        barrascontador.append(1)
        
    else:
        
        i = barras.index(barra)
        barraactiva = barrasrestante[i]
        barrascontador[i] += 1
    
    GananB = 0
    GananC = 0
    GananT = 0

    for i in range(1,len(parts)):
        tipo = parts[i]
        
        

        if tipo == "B" or tipo == "C" or tipo == "T":
            barraactiva.append(tipo)
            
            if tipo == "B":
                ganancia = detector(barraactiva)
                B += 1
                GananB += ganancia
                GananBTotal += ganancia
                
            if tipo == "C":
                C += 1
                ganancia = detector(barraactiva)
                GananC += ganancia
                GananCTotal += ganancia
                
            if tipo == "T":
                T += 1
                ganancia = detector(barraactiva)
                GananT += ganancia
                GananTTotal += ganancia
    
    total = GananB + GananT + GananC
    i = barras.index(barra)
    barrasrestante[i] = barraactiva
    
    barragan[i] += total
    total = 0
    
    line = arch.readline().strip()
        
burbuja(barras, barragan, barrascontador,barrasrestante)


print("a) Los ingresos generados por cada barra son")
for i in range(len(barras)):
    print(f"Barra {i+1} : $ {barragan[i]}")
    
print("======================================================================")

print("b) El porcentaje por producto con respecto al total es:")
GananTotal = GananBTotal + GananCTotal + GananTTotal
porcB = (GananBTotal/GananTotal)*100
porcC = (GananCTotal/GananTotal)*100
porcT = (GananTTotal/GananTotal)*100

print(f"Cervezas: {round(porcC,2)} %")
print(f"Bebidas: {round(porcB,2)} %")
print(f"Tragos: {round(porcT,2)} %")
    

print("======================================================================")

print("c) Los vasos destruidos por barra son:")
for i in range(len(barras)):
    print(f"Barra{i+1}")
    imprimir(barrasrestante[i])


print("======================================================================")

print("d) Estadísticas varias:")
for i in range(len(barras)):
    print(f"La barra {i+1} fue atendida {barrascontador[i]} veces")
    
print("-----------------------------------------------------------")   

burbujamenor(barrascontador, barras)

print(f"Barra(s) más atendida(s) es(son) con {barrascontador[0]} atenciones:")

rango = contadormaximos(barrascontador)
for i in range(rango):
    print(f"Barras {barras.index(barras[i]) + 1}")
    
print("-----------------------------------------------------------")
 
print(f"Barra(s) menos atendida(s) es(son) con {barrascontador[-1]}:")
rango = contadorminimos(barrascontador)
for i in range(rango):
    print(f"Barras {barras.index(barras[-1-i])}")
    
print("-----------------------------------------------------------")

print("El promedio de ingreso por barra es:")

miniburbuja(barras,barrascontador)

for i in range(len(barras)):
    print(f"Barra {i+1} : {round(barragan[i]/barrascontador[i],2)} pesos")
print("======================================================================")

