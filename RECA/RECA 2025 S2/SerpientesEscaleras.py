# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 17:11:57 2026

@author: cythg
"""
import numpy as np

def llenarPosiciones(filas, columnas, matriz):
    
    #AVANZA SI LA FILA ES PAR, RETROCEDE SI LA FILA ES IMPAR
    posicion = 0
    for f in range(filas):
        if f % 2 == 0:
            for c in range(columnas):
                matriz[f][c] = posicion
                posicion += 1
        else:
            for c in range(columnas):
                matriz[f][columnas - c - 1] = posicion
                posicion += 1
    
def detectarEntradasYSalidas(linea):
    for f in range(filas):
        linea = arch.readline().strip()
        partes = linea.split(" ")
        for c in range(columnas):
            
            elemento = partes[c]
            posicion = [f,c]
            if elemento != "0":
                if "E" in elemento or "S" in elemento:
                    lista_entradas.append(elemento)
                    lista_posiciones_entrada.append(posicion)
                    
                else:
                    lista_salidas.append(elemento)
                    lista_posiciones_salida.append(posicion)

def rellenarEntradasYSalidas():
    
    for i in range(len(lista_entradas)):
        entry = lista_entradas[i]
        pos_entry = lista_posiciones_entrada[i]
        f_entry = pos_entry[0]
        c_entry = pos_entry[1]
        
        for j in range(len(lista_salidas)):
            out = lista_salidas[j]
            pos_out = lista_posiciones_salida[j]
            f_out = pos_out[0]
            c_out = pos_out[1]
            
            if entry == out.upper():
            
                entradas.append(int(posiciones[f_entry][c_entry]))
                salidas.append(int(posiciones[f_out][c_out]))
                

def sumarAPosicionUnJugador(filas, columnas):
    meta = filas * columnas - 1
    for i in range(len(jugadores)):
        
        posicion_jugador = lista_posiciones[i]
        jugador = jugadores[i]
        dado = int(dados[i])
        
        # Verificar que no se pase del final
        if (posicion_jugador + dado) <= (meta):
            lista_posiciones[i] += dado
            if lista_posiciones[i] == meta:
                print(jugador + " ganó")
        
        print(f"{jugador} lanza {dado}. Posición {lista_posiciones[i]}. (Inicio: {posicion_jugador}) )")
        # Si se pasa de la meta, se queda en la posición
        
def escalerasOserpientes():
    for i in range(len(jugadores)):
        jugador = jugadores[i]
        posicion = lista_posiciones[i]
        
        #si posición está dentro de entradas
        if posicion in entradas:
            
            indice_salida = entradas.index(posicion)
            salida = salidas[indice_salida]
            
            if salida > posicion: # avanzó
                print(f"{jugador} tomó un escalera: {posicion} -> {salida}")
            else: # retrocedió
                print(f"{jugador} cayó en una serpiente: {posicion} -> {salida}")
            lista_posiciones[i] = salida
            
def clasificacion():
    def intercambiar(i,j,li):
        aux = li[i]
        li[i] = li[j]
        li[j] = aux
        
    def ordenar(li1,li2):
        for i in range(0, len(li1) - 1):
            for j in range(i + 1, len(li1)):
                
                if li1[i] < li1[j]:
                    intercambiar(i, j, li1)
                    intercambiar(i, j, li2)
                    
    ordenar(lista_posiciones, jugadores)
    for i in range(len(jugadores)):
        print(f"{i+1} - {jugadores[i]}: Posicion {lista_posiciones[i]}")
    print()
   
            
            
        
arch = open("tablero.txt","r",encoding="utf-8")
linea = arch.readline().strip()

cantidadDePartidas = int(linea)

for partidas in range(cantidadDePartidas):
    
    linea = arch.readline().strip()
    jugadores = linea.split(",")
        
    linea = arch.readline().strip()
    dimensiones = linea.split(" ")
    
    filas = int(dimensiones[0])
    columnas = int(dimensiones[1])
    
    posiciones = np.zeros([filas,columnas])
    llenarPosiciones(filas, columnas, posiciones)
    
    print(f"Partida {partidas + 1}: {jugadores}")
    print(f"Tablero {filas}x{columnas} ({filas*columnas} casillas)")
    print()
    
    lista_entradas = []
    lista_posiciones_entrada = []
    lista_salidas = []
    lista_posiciones_salida = []
    
    detectarEntradasYSalidas(linea)
    
    entradas = []
    salidas = []
    rellenarEntradasYSalidas()
    
    linea = arch.readline().strip()
    cantidadDados = int(linea)
    
    lista_posiciones = []
    for i in range(len(jugadores)):
        lista_posiciones.append(0)
        
    # jugadores = [pablo, juan, ... ,  pedrito]
    # posiciones = [0,      0, ... ,       0] paralela a jugadores
    # Esta posicion refiere a la de la matriz posiciones
    # Para ubicar fila y columna corresponde simplemente 
    # ubicar el número en la matriz
    
    for d in range(cantidadDados):
        linea = arch.readline().strip()
        dados = linea.split(" ")
        
        print(f"Vuelta {d + 1}:")
        sumarAPosicionUnJugador(filas, columnas)
        print()
        escalerasOserpientes()
    print()
    clasificacion()
        
    
        
    
            
            
    
    
    
    
    