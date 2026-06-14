# Paralelo C6 - Pablo Guzmán
"""
Created on Thu Oct 30 14:40:31 2025

@author: niconiconi
"""

contraseña_ingresada = input("ingrese contraseña: ")

while contraseña_ingresada != "venta2025":
    print("error, contraseña equivocada")
    contraseña_ingresada = input("ingrese contraseña: ")
    
print("---- Acceso al sistema ----\n===========================\n Registrando productos\n===========================")

nombre_producto = input("Ingrese el producto: ")

#Variables acumuladoras
descuentos = 0
subtotal = 0
total_iva = 0
boleta = "" #La boleta, acumuladora de strings

while nombre_producto != "fin":

    cantidad = int(input("Ingrese la cantidad vendida: "))
    precio_unidad = float(input("Ingrese el valor del producto: "))
    
    desc = input("indique si aplica descuento(si/no): ")
    
    while desc != "si" and desc != "no":
        desc = input("indique si aplica descuento(si/no): ")
    
    total = precio_unidad * cantidad
    
    descuento = 0
    if desc == "si":
        
        #Aquí la prueba se explica mal, porque dice si el
        #total del producto, pero se refiere al total de la venta
        if total < 5000:
            print("No aplica descuento")
        else:
            if total >= 5000 and total < 10000:
                descuento = 2250
            elif total >= 10000 and total < 20000:
                descuento = 5500
            
            print("Aplicando descuento")
            print("Procesando monto...")
            
            print(f"Aplica descuento de: ${descuento}")
    else:
        print("No aplica descuento")
        
    precio_final = total - descuento
    
    subtotal += precio_final
    descuentos += descuento
    
    iva = precio_final * 0.19
    total_iva += iva
    boleta += f"Producto: {nombre_producto}| Cantidad: {cantidad}| Total: {total}\n"

    #saltodelínea
    print()
    nombre_producto = input("Ingrese el producto: ")

print("=========== BOLETA ==========")
if subtotal == 0:
    print("sin productos")

print()
print(boleta)
print(f"Descuentos aplicados: ${descuentos}")
print(f"Subtotal: ${subtotal}")
print(f"Iva(19%): ${total_iva}")

total_a_pagar = subtotal + total_iva
print(f"Total a pagar: ${total_a_pagar}")