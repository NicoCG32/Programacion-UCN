"""
Ej
"""

def valorabsoluto(numero):
    numero = numero ** 2
    numero = numero ** (1/2)
    return numero

def DeterminarIndice(gravedad, temperatura, radiacion):
    gpuntaje = 2.71 ** - ((gravedad - 9.8)**2 / 8)
    
    if temperatura >= 50 or temperatura <= -20:
        tpuntaje = 0
    else:
        tpuntaje = 1 + (valorabsoluto(temperatura-15) / 35)
    
    rpuntaje = 2.71**-(0.005 * (radiacion - 300))
    
    h = gpuntaje * tpuntaje * rpuntaje * 100
    return h


texto = "Hola gente"
texto += " kiehubo"
print(texto)