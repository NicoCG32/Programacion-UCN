# Paralelo C6 - Pablo Guzmán
"""
Created on Thu Jan 15 12:56:48 2026

@author: cythg
"""

arch = open("autos.txt","r", encoding="utf-8")
linea = arch.readline().strip()

#Algoritmos por global
menor_cilindrada = 999999
modelo_menor_cilindrada = ""

menor_año = 9999
modelo_menor_año = ""

acumulador_años = 0
descontinuados = 0

while linea != "":
    
    partes = linea.split(",")
    
    marca = partes[0]
    cantAutos = int(partes[1])

    #Algoritmos por marca
    
    mayor_cilindrada_modelo = ""
    mayor_cilindrada_motor = ""
    mayor_cilindrada = -9999
    
    mayor_eficiente_modelo = ""
    mayor_eficiente = -9999
    
    cont_auto = 0
    cont_man = 0
    cont_total = 0
    
    for i in range(cantAutos):
        linea = arch.readline().strip()
        
        partes = linea.split(",")
        
        #Modelo,tipo_motor,cilindrada,hp,transmisión,primera_fabricación,última_fabricación

        modelo = partes[0]
        tipoMotor = partes[1]
        cilindrada = float(partes[2])
        hp = int(partes[3])
        transmision = partes[4]
        primera_fabric = int(partes[5])
        ultima_fabric = partes[6]
        
        eficiencia = hp / cilindrada
        
        if mayor_cilindrada < cilindrada:
            mayor_cilindrada_modelo = modelo
            mayor_cilindrada = cilindrada
            mayor_cilindrada_motor = tipoMotor
        
        if mayor_eficiente < eficiencia:
            mayor_eficiente_modelo = modelo
            mayor_eficiente = eficiencia
    
        if transmision == "Automática":
            cont_auto += 1
        
        if transmision == "Manual":
            cont_man += 1
        
        cont_total += 1
        
        #Algoritmos Globales
        
        if menor_cilindrada > cilindrada:
            menor_cilindrada = cilindrada
            modelo_menor_cilindrada = modelo
        
        if ultima_fabric == "Presente":
            
            if primera_fabric < menor_año:
                menor_año = primera_fabric
                modelo_menor_año = modelo
                
        else:
            descontinuados += 1
            ultima_fabric = int(ultima_fabric)
            
            periodo = ultima_fabric - primera_fabric
            acumulador_años += periodo
        
    print(marca)
    
    print(f"El vehículo con mayor cilindrada es {mayor_cilindrada_modelo} con {mayor_cilindrada}L en motor {mayor_cilindrada_motor}")
    print(f"El vehículo más eficiente es {mayor_eficiente_modelo} con {mayor_eficiente}")
    
    porc_auto = round(cont_auto * 100 / cont_total , 2)
    porc_man = round(cont_man * 100 / cont_total , 2)
    print(f"El {porc_auto}$ de los {marca} tiene transmisicón automática y el {porc_man}% tiene transmisión manual")
        
    linea = arch.readline().strip()

print(f"El vehículo con menor cilindrada es: {modelo_menor_cilindrada} con {menor_cilindrada}L")
print(f"De los vehículos que todavía se fabrican, el que lleva más tiempo es: {modelo_menor_año}")
promedio = round(acumulador_años / descontinuados , 2)
print(f"De los vehículos que ya no se fabrican, en promedio su periodo de fabricación fue de {promedio} años")