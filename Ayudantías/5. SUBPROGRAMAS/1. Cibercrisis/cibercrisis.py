"""
Cibercrisis
"""

def DeterminarSiEsMalware(texto): #Función dada en el problema
    texto += " "
    if "ware " in texto:
        return True
    return False

def DeterminarCosto(efectividad):
    if efectividad > 95:
        return 1
    if efectividad > 60:
        return 0.1 * 3
    return 0.1

def DetAtaqueMasRec(Phishing, Malware, SQLInjection, DDoS):

    if Phishing > Malware and Phishing > SQLInjection and Phishing > DDoS:
        return "Phishing"
    if Malware > Phishing and Malware > SQLInjection and Malware > DDoS:
        return "Malware"
    if SQLInjection > Phishing and SQLInjection > Malware and SQLInjection > DDoS:
        return "SQLInjection"
    if DDoS > Phishing and DDoS > Malware and DDoS > SQLInjection:
        return "DDoS"
    return "Variado"
    
arch = open("ataques.txt", "r", encoding= "utf-8")
line = arch.readline().strip()

proximoFoco = ""
promedioProximoFoco = 0

while line != "":
    partes = line.split(";")
    
    continente = partes[0]
    cantidadPaises = int(partes[1])
    
    #Variables requeridas
    contAtaques = 0
    contAtaquesEfectivos = 0
    costoTotal = 0
    
    sumaEfectividad = 0
    
    for i in range(cantidadPaises):
        
        line = arch.readline().strip()
        partes = line.split(", ") #Nótese el espacio
        
        pais = partes[0]
        cantidadAtaques = int(partes[1])
        
        contAtaques += cantidadAtaques
        
        #Variables requeridas
        contPhishing, contMalware, contSQLInjection, contDDoS = 0,0,0,0
        totalEfectividad = 0
        
        for j in range(2, cantidadAtaques * 2 + 1, 2): #También se puede trabajar con el len(partes)
            
            tipoAtaque = partes[j]
            efectividad = int(partes[j + 1])
            
            totalEfectividad += efectividad
            
            if DeterminarSiEsMalware(tipoAtaque):
                contMalware += 1
                
            elif tipoAtaque == "SQLInjection":
                contSQLInjection += 1
                
            elif tipoAtaque == "Phishing":
                contPhishing += 1
                
            elif tipoAtaque == "DDoS":
                contDDoS += 1
                
                
            if efectividad >= 60:
                contAtaquesEfectivos += 1
                
            costoTotal += DeterminarCosto(efectividad)
        
        ataqueMasRecurrente = DetAtaqueMasRec(contPhishing, contMalware, contSQLInjection, contDDoS)
        print(f"- El ataque más recurrente en {pais} es {ataqueMasRecurrente}")
        
        promedioEfectividad = round(totalEfectividad/cantidadAtaques, 2)
        print(f"  El promedio de efectividad fue de {promedioEfectividad}")
        
        sumaEfectividad += promedioEfectividad
    
    if contAtaquesEfectivos == contAtaques:
        print(f"* Desastre TOTAL, es urgente mejorar los recursos defensivos de {continente} *")
    costoTotal = round(costoTotal, 1) #Para cortar el margen de fallo que da el float
    print(f"La cantidad de ataques efectivos en {continente} fue de: {contAtaquesEfectivos}")
    print(f"El costo total en reparaciones fue de ${costoTotal} M")
    print() #Salto de linea
    
    promedioContinente = round(sumaEfectividad / cantidadPaises, 2)

    if promedioContinente > promedioProximoFoco:
        proximoFoco = continente
        promedioProximoFoco = promedioContinente
        
    line = arch.readline().strip()
    
print(f"El próximo continente foco de los ataques de Anonymous posiblemente sea {proximoFoco} con promedio de efectividad del {promedioProximoFoco} %")