# -*- coding: utf-8 -*-
#Pablo Guzmán C2
"""
Salvando las notas
Hackeando Hawaii
"""

contraseña_predefinida = "345"

contraseña = "000"
intentos = 1

i = 0
j = 0
k = 1

comprobador = contraseña != contraseña_predefinida
#Booleano para evitar repetir el contraseña != contraseña_predefinida

while comprobador and i < 10:
    while comprobador and j < 10:
        while comprobador and k < 10:
            contraseña = f"{i}{j}{k}"
            comprobador = contraseña != contraseña_predefinida
            k += 1
            intentos += 1
        j += 1
        k = 0
    i += 1
    j = 0
    k = 0

if not comprobador:
    print(f"Contraseña encontrada: '{contraseña}'")
print(f"Total de intentos = {intentos}")