# -*- coding: utf-8 -*-
# Datos del usuario
nivel = 2
capacitacion = False
supervisor = True

autorizado = False
mensaje = ""

# Evaluación de acceso
if nivel >= 3 and capacitacion == True:
    autorizado = True
    mensaje = "Acceso autorizado por nivel y capacitación"
elif supervisor = True:
    autorizado = True
    mensaje = "Acceso autorizado por rol de supervisor"
else:
    autorizado == False
    mensaje = "Acceso denegado"

print("¿Autorizado?:", autorizado)
print("Mensaje:", mensaje)
