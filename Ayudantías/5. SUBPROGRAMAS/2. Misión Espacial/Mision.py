"""
Sistema de Análisis de Exploración Espacial
"""

def CalcularKM(distanciaYMedida):
    partes = distanciaYMedida.split(" ")
    distancia = float(partes[0])
    unidad = partes[1]
    
    if unidad == "[LY]":
        distancia *= 9_460_800_000_000
    if unidad == "[PM]":
        distancia *= 1_000_000_000_000
    if unidad == "[PC]":
        distancia *= 30_856_804_799_935
    
    return int(distancia)

def DeterminarIndice(G, T, R):
    
    puntajeGravedad = 2.71**(-((G - 9.8)**2) / 8)
    
    if T > -20 and T < 40:
        puntajeTemperatura = 1 + ((((T - 15)**2)**(1/2)) / 35)
    else:
        puntajeTemperatura = 0
        
    puntajeRadiacion = 2.71**(-0.005 * (R - 300))
    
    indice = puntajeGravedad * puntajeTemperatura * puntajeRadiacion * 100  
  
    return round(indice, 2)

def Clasificar(H):
    if H >= 80:
        return "ÓPTIMO"
    elif H >= 30:
        return "HABITABLE"
    return "INHÓSPITO"

def DeterminarSimilitudes(gravedad, temperatura, radiacion):
    formato = ""
    if gravedad:
        formato += "Gravedad "
    if temperatura:
        formato += "Temperatura "
    if radiacion:
        formato += "Radiación "
    return formato
        
def ImprimirInforme(nombre, indice, clasificacion, formatoSimilitudes):
    print(f"🪐 {nombre.upper()} | Índice: {indice} | Clase: {clasificacion} | Similitudes: {formatoSimilitudes}")

def DeterminarDiferencia(gravedad, temperatura, radiacion):
    difGravedad = (((gravedad - 9.8)**2)**1/2)
    difTemp = (((temperatura - 15)**2)**1/2)
    difRad = (((radiacion - 300)**2)**1/2)
    
    return difGravedad + difTemp + difRad

archivo = open("exoplanetas.txt", 'r')
linea = archivo.readline().strip()

#Contador similes
contSimiles = 0

#Para comenzar a identificar al más extremo
planetaMasExtremo = ""
difMasExtremo = 0

#Identificar al más cercano
planetaMasCercano = ""
distanciaMasCercano = -1 #También podría poner un número muy grande

#Promedios
gravedadTotal = 0
contGravedad = 0
temperaturaTotal = 0
contTemperatura = 0
radiacionTotal = 0
contRadiacion = 0

while linea != "":
    partes = linea.split('|')
    
    gravedadTerrestre = False
    temperaturaTerrestre = False
    radiacionTerrestre = False
    
    nombrePlaneta = partes[0]
    
    gravedad = float(partes[1])
    temperatura = int(partes[2])
    radiacion = int(partes[3])
    
    distancia = partes[4]
    distanciaEnKM = CalcularKM(partes[4])
    
    indiceCalculado = DeterminarIndice(gravedad, temperatura, radiacion)
    categoria = Clasificar(indiceCalculado)
    
    if gravedad == 9.8:
        gravedadTerrestre = True   
    if temperatura == 15:
        temperaturaTerrestre = True
    if radiacion == 300:
        radiacionTerrestre = True

    formatoSimilitudes = DeterminarSimilitudes(gravedadTerrestre, temperaturaTerrestre, radiacionTerrestre)
    
    ImprimirInforme(nombrePlaneta, indiceCalculado, categoria, formatoSimilitudes)
    
    #Contando planetas símiles a la Tierra
    if gravedadTerrestre and temperaturaTerrestre and radiacionTerrestre:
        contSimiles += 1
        print(f"El planeta {nombrePlaneta} es idéntico a la Tierra!")
        
    #Identificando al mas extremo
    difTotal = DeterminarDiferencia(gravedad, temperatura, radiacion)
    if difTotal > difMasExtremo:
        difMasExtremo = difTotal
        planetaMasExtremo = nombrePlaneta
    
    #Identificando el más cercano y sumando para promediar
    if categoria == "ÓPTIMO" or categoria == "HABITABLE":
        
        if distanciaEnKM < distanciaMasCercano or distanciaMasCercano < 0:
            planetaMasCercano = nombrePlaneta
            distanciaMasCercano = distanciaEnKM
        
        gravedadTotal += gravedad
        contGravedad += 1
        temperaturaTotal += temperatura
        contTemperatura += 1
        radiacionTotal += radiacion
        contRadiacion += 1

    linea = archivo.readline().strip()

print()
print(f"Hay un total de {contSimiles} planetas idénticos a la Tierra")
    
distanciaMasCercano = int(distanciaMasCercano / 100000)
print(f"El planeta más extremo respecto de la Tierra es {planetaMasExtremo}")
print(f"El planeta habitable u óptimo más cerca de la Tierra es {planetaMasCercano} a una distancia de {distanciaMasCercano} [GM]")

promedioGrav = round(gravedadTotal/contGravedad, 2)
promedioTemp = round(temperaturaTotal/contTemperatura, 2)
promedioRad = round(radiacionTotal/contRadiacion, 2)
print("--- PROMEDIOS ---")
print(f"Gravedad: {promedioGrav}, Temperatura: {promedioTemp}, Radiación: {promedioRad}")