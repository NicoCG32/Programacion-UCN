# -*- coding: utf-8 -*-
#Pablo Guzmán C2
"""
Salvando las notas
Hackeando Hawaii
EXTRA
"""

contraseña_predefinida = "bbb"

contraseña = ""
intentos = 1

string = "abcdefghijklmnñopqrstuvwxyz"

contraseña_final = ""

for i in string:
    contraseña += i
    
    for j in string:
        contraseña = f"{i}" + j
        
        for k in string:
            contraseña = f"{i}{j}" + k
            
            if contraseña == contraseña_predefinida:
                contraseña_final = contraseña
            elif contraseña_final == "":
                intentos += 1
                
    contraseña = ""

print(f"Contraseña encontrada: '{contraseña_final}'")
print(f"Total de intentos = {intentos}")