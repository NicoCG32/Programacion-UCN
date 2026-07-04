# -*- coding: utf-8 -*-
#Pablo Guzmán C2
"""
Las Tablas
o la correa
"""
contador_errores = 0

numero = int(input("Ingrese un número entero entre el 1 y el 12: "))

while (numero < 0 or numero > 12):
    print("Error, el número debe estar entre 1 y 12")
    numero = int(input("Ingrese un número entero entre el 1 y el 12: "))

for i in range(1, 13):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    
nuevo_nuevo = ((numero * 7) % 12) + 1

for i in range(1, 13):
    resultado = nuevo_nuevo * i
    ingreso = int(input(f"{nuevo_nuevo} x {i} = "))
    while ingreso != resultado:
        print("Incorrecto!")
        contador_errores += 1
        ingreso = int(input(f"{nuevo_nuevo} x {i} = "))
        
if contador_errores == 0:
    print("Felicitaciones, has acertado todo a la primera.")