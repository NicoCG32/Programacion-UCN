# -*- coding: utf-8 -*-
"""

- Permitir el ingreso de temperaturas una a una, utilizando un ciclo.
- El ingreso de datos finaliza cuando se ingresa una temperatura igual a -100.
- Calcular: Cantidad total de registros, temperatura mayor, temperatura menor y promedio de
temperatura
- Si la temperatura anteriormente ingresada tiene una diferencia de 5° con la nueva, entonces
debes aplicar la siguiente fórmula para la temperatura:
Nota: Recuerda que la primera vez no se debe considerar la temperatura anterior, pues no
existe.
- Imprimir un reporte final que debe mostrar todas las veces que se aplicó la fórmula y el ajuste
que se tuvo que realizar, bajo el siguiente formato:
ID,Ajuste (El ID parte en 1 y sigue al infinito) (Ajuste es la diferencia entre la Temperatura
nueva y la Temperatura Ajustada)

"""

cantidad_total = 0
mayor = -99999
menor = 99999
acumulador = 0
informe = ""
temp = float(input("Ingrese la temperatura: "))
previo = -100
ID = 1

while temp != -100:
    
    if cantidad_total != 0:
        if previo == temp + 5 or previo == temp - 5:
            tempSinAjuste = temp
            temp = (2 * temp + previo)/ 3
            
            ajuste = tempSinAjuste - temp
            
            informe += f"{ID},{ajuste}\n"
            ID += 1
        
    cantidad_total += 1
    
    if temp > mayor:
        mayor = temp
        
    if temp < menor:
        menor = temp
    
    acumulador += temp
    
    previo = temp
    temp = float(input("Ingrese la temperatura: "))

if cantidad_total != 0:
    print("---- Reporte final ----")
    print(f"Total de registros: {cantidad_total}")
    print(f"Temperatura Mayor: {mayor} °C")
    print(f"Temperatura Menor: {menor} °C")
    
    print(f"Promedio: {acumulador / cantidad_total} °C")
    
    print("---- AJUSTES APLICADOS ----")
    print(informe)
else:
    print("No se ingresaron datos")

    
    
    
    
    
    
    
    
    
    
    
    