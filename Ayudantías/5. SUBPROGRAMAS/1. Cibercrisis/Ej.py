"""
Ej
"""

arch = open("ataques.txt","r",encoding="utf-8")
line = arch.readline().strip()

while line != "":
    print(line)    
    partes = line.split(";")
    continente = partes[0]
    cantidadPaises = int(partes[1])
    
    for i in range(cantidadPaises):
        line = arch.readline().strip()
        
        partes = line.split(", ")
        pais = partes[0]
        cantidadAtaques = int(partes[1])
    
        for j in range(2, len(partes), 2):
            
            tipoAtaque = partes[j]
            efectividad = partes[j+1]
            
    line = arch.readline().strip()
