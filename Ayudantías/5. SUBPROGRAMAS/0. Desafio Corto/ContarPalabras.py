"""
Contar Palabras
"""
def ContarPalabras(texto):
    textoDividido = texto.split(" ")
    return len(textoDividido)

def ContarPalabras2(texto):
    suma = 1
    for i in texto:
        if i == " ":
            suma += 1
    return suma

texto = input("Ingrese un texto para contar sus palabras: ")
cantidadDePalabras = ContarPalabras(texto)
cantidadDePalabras2 = ContarPalabras2(texto)
print(cantidadDePalabras, cantidadDePalabras2)