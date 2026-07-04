#C1 Pablo Guzmán
"""
- El sistema debe permitir el ingreso de datos del sismo: zona, magnitud y profundidad (en km)
- Debe calcular el porcentaje de sismos totales por cada zona del país (Norte, Centro, Sur y
Austral)
- Debe calcular el promedio general de magnitud y profundidad.
- Debe guardar todos los sismos en un informe o reporte que se debe imprimir por pantalla al
final del día, el formato es el siguiente: ID,Zona,Magnitud,Profundidad (el ID debe partir en 1,
y seguir indefinidamente) 
"""

zona = input("Ingrese la zona del sismo (Norte/Centro/Sur/Austral/-1 para salir): ")

#Contadores
norte = 0
centro = 0
sur = 0
austral = 0
total = 0

#Promedios
acumuladorMagnitud = 0
acumuladorProfundidad = 0

#Informe
ID = 1
informe = ""

while zona != "-1":
    magnitud = float(input("Ingrese la magnitud: "))
    profundidad = float(input("Ingrese la profundidad: "))
    
    zona = zona.capitalize()
    
    if zona.lower() == "norte":
        norte += 1
        
    elif zona.lower() == "centro":
        centro += 1
        
    elif zona.lower() == "sur":
        sur += 1
        
    elif zona.lower() == "austral":
        austral += 1
    
    total += 1
    acumuladorMagnitud += magnitud
    acumuladorProfundidad += profundidad
    informe += f"{ID},{zona},{magnitud},{profundidad}\n"
    ID += 1
    
    zona = input("Ingrese la zona del sismo (Norte/Centro/Sur/Austral/-1 para salir): ")
    

if total != 0:

    print("INFORME DIARIO")
    print(informe)
    
    print()
    print("Estadísticas")
    print(f"Promedio de magnitud: {acumuladorMagnitud/total}")
    print(f"Promedio de profundidad: {acumuladorProfundidad/total}")
    
    print()
    print("Porcentaje por zona: ")
    print(f"Norte: {round( (norte/total) * 100 , 2)} %")
    print(f"Centro: {round( (centro/total) * 100 , 2)} %")
    print(f"Sur: {round( (sur/total) * 100 , 2)} %")
    print(f"Austral: {round( (austral/total) * 100 , 2)} %")
else:
    print("No hay datos")