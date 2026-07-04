# -*- coding: utf-8 -*-
"""
LISTAS PARALELAS, JUEGO DE INDICES Y LÓGICA DE SUBPROGRAMAS (DIFÍCIL)
"""
#SEGUNDO
def desglosarRecord(r):
    #vic-derr-emp
    aux = r.split("-")
    victorias = int(aux[0])
    derrotas = int(aux[1])
    record = [victorias, derrotas]
    if len(aux) == 3:
        empates = int(aux[2])
        record.append(empates)
    else:
        #para el manejo optimo de datos en caso de no haber empates le agregamos un 0
        record.append(0)
    return record

# PRIMERO
def CargarPeleadores():
    arch = open("peleadores.txt")
    linea = arch.readline().strip()
    
    while linea != "":
        
        partes = linea.split(",")
        
        nombre = partes[0]
        estilo = partes[1]
        
        #vic-derr-emp;racha
        record = partes[2]
        aux = record.split(";")
        
        record = aux[0]
        racha = int(aux[1])
        
        #vic-derr-emp
        record = desglosarRecord(record)
        
        apodo = partes[3]
        
        if len(partes) == 5:
            campeon = apodo #Si la linea es más larga entonces es campeón
        
        nombres.append(nombre)
        estilos.append(estilo)
        records.append(record) #Lista de listas
        rachas.append(racha)
        apodos.append(apodo)
        
        linea = arch.readline().strip()
        
    return campeon

nombres = []
estilos = []
records = []
rachas = []
apodos = []

campeon = CargarPeleadores()
defensas = 0
print(f"{campeon} es campeón indiscutido")

#Se puede ocupar INDEX
def buscarPeleador(peleador):
    for i in range(len(nombres)):
        if nombres[i] == peleador:
            return i
    return -1

#CUARTO
def buscarGanador(i1, record1, i2, record2):
    nuevo_r1 = record1
    nuevo_r2 = record2
    
    antiguo_r1 = records[i1]
    antiguo_r2 = records[i2]
    
    if nuevo_r1[0] > antiguo_r1[0]:
        return [i1,i2]
    
    if nuevo_r2[0] > antiguo_r2[0]:
        return [i2,i1]

    return ["Empate","Empate"] #PARA EVITAR ERRORES, aunque no es necesario en el fondo
    
#QUINTO 
def actualizarRecords(indice, nuevo_record):
    records[indice] = nuevo_record
    
#SEXTO
def imprimiCambioDeCampeon(prev, nuevo, metodo, defensas):
    mensaje = f"{nuevo} es nuevo campeón indiscutido, arrebatándole el título a {prev} via {metodo}, "
    if defensas == 0:
        mensaje += "que NO pudo defender su título"
    else:
        mensaje += f"que pudo defender su título {defensas} veces"
    print(mensaje)
    
#SEPTIMO
def actualizarRachas(i_gan, i_per):
    rachas[i_gan] += 1
    rachas[i_per] = 0
    
#TERCERO
def CargarCombates(campeon):
    arch = open("combates.txt")
    linea = arch.readline().strip()
    
    #El primer campeón no tiene defensas (o no se mencionan, así que no son relevantes)
    defensas = 0
    while linea != "":
        partes = linea.split(";")
        
        peleador1 = partes[0]
        record_p1 = desglosarRecord(partes[1])
        
        indice_p1 = buscarPeleador(peleador1)
        
        peleador2 = partes[2]
        record_p2 = desglosarRecord(partes[3])
        indice_p2 = buscarPeleador(peleador2)
        
        metodo = partes[4]
        
        indicesGanadorYPerdedor = buscarGanador(indice_p1, record_p1, indice_p2, record_p2)
        indice_ganador = indicesGanadorYPerdedor[0]
        indice_perdedor = indicesGanadorYPerdedor[1]
    
        #LÓGICA DEL CAMBIO DE CAMPEÓN Y DEFENSAS
        if indice_ganador == "Empate":
            #No hacemos nada es para evitar que el código se rompa con
            #apodos[indice_perdedor]
            variable = "hola"
            
        else:
            if campeon == apodos[indice_perdedor]:
                prev_campeon = campeon #ESTO ES SÓLO PARA HACERLO EXPLÍCITO
                nuevo_campeon = apodos[indice_ganador]
                imprimiCambioDeCampeon(prev_campeon, nuevo_campeon, metodo, defensas)
                
                defensas = 0
                campeon = nuevo_campeon
                
            elif campeon == apodos[indice_ganador]:
                defensas += 1
        
        #Para la fórmula
            #LOGICA DE LAS RACHAS, cuidado con el "empate"
            actualizarRachas(indice_ganador, indice_perdedor)
        #LÓGICA DE RECORDS
        actualizarRecords(indice_p1, record_p1)
        actualizarRecords(indice_p2, record_p2)
        
        linea = arch.readline().strip()
    
    mensaje = f"El campeón final fue {campeon} y "
    if defensas == 0:
        mensaje += "NO tiene defensas."
    else:
        mensaje += f"tiene {defensas} defensas"
    print(mensaje)
    
CargarCombates(campeon)

print()
print("--------------------------------")
print()
print("PELEADORES INVICTOS")
#logica de invictos
def BuscarInvictos():
    for i in range(len(nombres)):
        if records[i][1] == 0: #Derrotas del peleador I
            print(f"El peleador {nombres[i]} está invicto!")
            
BuscarInvictos()

print()
print("--------------------------------")
print()
print("ESTILO O ESTILOS MÁS EFECTIVOS")
#Estilo más efectivo
def buscarUnicos(lista):
    unicos = []
    for i in lista:
        if i not in unicos:
            unicos.append(i)
    return unicos
            
estilos_unicos = buscarUnicos(estilos)
victorias_por_estilo = [0] * len(estilos_unicos)

def sumarVictoriasPorEstilo():
    for i in range(len(estilos_unicos)):
        estilo = estilos_unicos[i]
        for j in range(len(nombres)):
            if estilos[j] == estilo:
                victorias_por_estilo[i] += records[j][0] #Peleador j - victorias
            
sumarVictoriasPorEstilo()

#De las lógicas más complicadas: búsqueda de N mayores
def buscarMayores(lista):
    mayor = -1
    mayores = []
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            mayores = [i]
        elif lista[i] == mayor:
            mayores.append(i)
    return mayores

indices_mayor = buscarMayores(victorias_por_estilo)
#para imprimir N mayores
mensaje = ""
for i in range(len(indices_mayor)):
    indice = indices_mayor[i]
    mensaje += f"{estilos_unicos[indice]} "
    if i == len(indices_mayor) - 2: #El penúltimo
        mensaje += "y "
    elif i != len(indices_mayor) - 1: #Distinto del último
        mensaje += ", "
        
if len(indices_mayor) == 1:
    mensaje += "es el estilo más efectivo"
else:
    mensaje += "son los estilos más efectivos"
    
print(mensaje)

#Siguiente retador
def calcularVictoriasPuras(indice):
    return records[indice][0] - records[indice][1]
    
def calcularFormula(indice):
    x = calcularVictoriasPuras(indice) #victorias puras
    y = rachas[indice]
    f = 4 * (x-5) + 2 ** (y - 1)
    return f

print()
print("--------------------------------")
print()

print("SIGUIENTE O SIGUIENTES RETADORES")
#teóricamente podríamos hacer lo tipico
#asignar una variable con el menor valor posible y busqueda del mayor
#sin embargo la ecuacion nos podría dar perfectamente un número muy negativo 
#(si el peleador es muy malo), así que lo mejor debería ser trabajarlo como una lista
calculos = []
for i in range(len(nombres)):
    calculo = calcularFormula(i)
    calculos.append(calculo)

#y ahora buscamos al mayor
mayores = buscarMayores(calculos)

mensaje = ""
for i in range(len(mayores)):
    indice = mayores[i]
    mensaje += f"{nombres[indice]} ({calculos[indice]}) "
    if i == len(mayores) - 2: #El penúltimo
        mensaje += "y "
    elif i != len(mayores) - 1: #Distinto del último
        mensaje += ", "
        
if len(mayores) == 1:
    mensaje += "es el siguiente retador al título"
else:
    mensaje += "son los siguientes retadores al titulo"
    
print(mensaje)
    
#Ordenar
def intercambiar(i, j, lista):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
    
def ordenar():
    for i in range(0, len(nombres) - 1):
        for j in range(i + 1, len(nombres)):
            if calcularVictoriasPuras(i) < calcularVictoriasPuras(j):
                intercambiar(i, j, nombres)
                intercambiar(i, j, estilos)
                intercambiar(i, j, records)
                intercambiar(i, j, rachas)
                intercambiar(i, j, apodos)

print()
print("--------------------------------")
print()
print("PELEADORES EN ORDEN DE VICTORIAS PURAS:")     
ordenar()   
for i in range(len(nombres)):
    print(f"{nombres[i]} '{apodos[i]}', con un record de {records[i][0]}-{records[i][1]}-{records[i][2]} y una racha de {rachas[i]}")
    
