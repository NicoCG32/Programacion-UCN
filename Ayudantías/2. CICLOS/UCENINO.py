# -*- coding: utf-8 -*-
#Pablo Guzmán C2
"""
UCENINO
El Aventurero
"""

ruta = input("Ingrese la ruta (L: izquierda, R: derecha, U: arriba, D: abajo): ").upper() #.upper opcional

eje_vertical = 0
eje_horizontal = 0

while ruta != "":    
    
    for i in ruta:
        if i == "L":
            eje_horizontal -= 1
        elif i == "R":
            eje_horizontal += 1
        elif i == "D":
            eje_vertical -= 1
        elif i == "U":
            eje_vertical += 1
        else:
            print("Pedazo de ruta omitida")
            
    ruta_final = ""
    
    for i in range(0, eje_horizontal):
        ruta_final += "R"
        
    for i in range(0, eje_vertical):
        ruta_final += "U"
    
    for i in range(0, eje_horizontal, -1):
        ruta_final += "L"
        
    for i in range(0, eje_vertical, -1):
        ruta_final += "D"
        
    if eje_vertical == -4 and eje_horizontal == -4:
        print("La mamá del Maxi te agarró a correazos")
        
    print(f"La ruta final es {ruta_final}")
    
    ruta = input("Ingrese la ruta (L: izquierda, R: derecha, U: arriba, D: abajo): ").upper()
    
print("Aventura finalizada")