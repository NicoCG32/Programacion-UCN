"""
Desafío Fit: Rumbo al Verano
"""
def CalcularTiempo(MMSS):
    tiempo = MMSS.split(":")
    minutos = int(tiempo[0])
    segundos = int(tiempo[1])
    segundos += minutos * 60
    return segundos

def leerEntrenamiento(fecha):
    entrenamiento = open("entrenamiento.txt", "r", encoding= "utf-8")
    line = entrenamiento.readline().strip()
    partes = line.split(",")
    fechaEntreno = partes[0]
    
    #Se busca la fecha en concreto
    while fechaEntreno != fecha and fechaEntreno != "":
        line = entrenamiento.readline().strip()
        partes = line.split(",")
        fechaEntreno = partes[0]
    
    caloriasQuemadas = 0
    
    #Se asegura que la fecha no es vacío
    if fechaEntreno != "": 
        cantEjercicios = int(partes[1])
        
        for i in range(cantEjercicios):
            line1 = entrenamiento.readline().strip()
            
            partesEntreno = line1.split(",")
            
            ejercicio = partesEntreno[0]
            tipo = partesEntreno[1].lower()
    
            if tipo == "cardio":
                segundos = CalcularTiempo(partesEntreno[2])
                caloriasQuemadas += segundos * 0.42
                
            elif tipo == "sets":
                sets = int(partesEntreno[2])
                caloriasQuemadas += sets * 0.16
    
            else:
                calorias = int(partesEntreno[2])
                print(f"Se ha realizado un entrenamiento especial llamado {ejercicio} y se han quemado {calorias} calorias")
                caloriasQuemadas += calorias
                
    return int(caloriasQuemadas)

def leerDieta(fecha):
    dieta = open("dieta.txt", "r", encoding= "utf-8")
    line = dieta.readline().strip()
    partes = line.split(",")
    fechaDieta = partes[0]
    
    #Se busca la fecha en concreto
    while fechaDieta != fecha and fechaDieta != "":
        line = dieta.readline().strip()
        partes = line.split(",")
        fechaDieta = partes[0]
    
    caloriasConsumidas = 0

    #Se asegura que la fecha no es vacío
    if fechaDieta != "":
        cantComidas = int(partes[1])
        
        for i in range(cantComidas):
            line2 = dieta.readline().strip()
            
            partesDieta = line2.split(",")
            
            horario = partesDieta[0].upper()
            comida = partesDieta[1]
            calorias = int(partesDieta[2])
            
            if horario == "DESAYUNO" or horario == "ALMUERZO":
                caloriasConsumidas += calorias / 2
                
            elif horario == "ONCE":
                caloriasConsumidas += calorias * 2.6
              
            else:
                print(f"Se ha consumido {comida}, una comida extra de tipo {horario} que hizo consumir {calorias * 2} calorias")
                caloriasConsumidas += calorias * 2
    
    return int(caloriasConsumidas)

fecha = input("Ingrese la fecha a analizar: ")
while fecha != "-1":
    
    caloriasQuemadas = leerEntrenamiento(fecha)
    caloriasConsumidas = leerDieta(fecha)
    
    if caloriasQuemadas != 0 and caloriasConsumidas != 0:
        deficit = caloriasConsumidas - caloriasQuemadas
        
        if deficit > 700 or deficit < 200:
            print(f"{fecha}: No se ha cumplido con la meta, el deficit fue de {deficit}")
            
        else:
            print(f"{fecha}: ¡Se ha cumplido con la meta! el deficit fue de {deficit}")
    
    else:
        if caloriasQuemadas == 0:
            print(f"En la fecha {fecha} no se realizó ningún entrenamiento!")
            caloriasConsumidas = leerDieta(fecha)
            print(f"se consumieron {caloriasConsumidas} calorias")
            
        if caloriasConsumidas == 0:
            print(f"En la fecha {fecha} se realizó un ayuno!")
            caloriasQuemadas = leerEntrenamiento(fecha)
            print(f"se quemaron {caloriasQuemadas} calorias en entrenamientos")
    
    print() #Salto de linea
    
    fecha = input("Ingrese la fecha a analizar: ")
print("Análisis finalizado.")