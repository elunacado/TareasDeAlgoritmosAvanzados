# Programa para cableado óptimo de fibra óptica
# Autor:
# Fecha: 
# Descripción: Este programa lee una matriz de adyacencia que representa distancias entre colonias
# y calcula la cantidad mínima de cable necesario para conectar todas las colonias usando el Algoritmo de Prim.

import sys
import numpy as np

def encontrarLlaveMinima(valoresLlave, incluidoEnMst, numColonias):
    """
    Encuentra la colonia con el valor de llave mínimo que aún no está incluida en el MST.

    Parámetros:
        valoresLlave (lista): El peso de la conexión más corta a cada colonia.
        incluidoEnMst (lista): Indica si una colonia está incluida en el MST.
        numColonias (int): El número total de colonias.

    Retorna:
        int: El índice de la colonia con el valor de llave mínimo.
    """
    valorMinimo = sys.maxsize
    indiceMinimo = -1
    
    for colonia in range(numColonias):
        if not incluidoEnMst[colonia] and valoresLlave[colonia] < valorMinimo:
            valorMinimo = valoresLlave[colonia]
            indiceMinimo = colonia
            
    return indiceMinimo

def mostrarMst(coloniaPadre, grafoDistancias, numColonias):
    """
    Imprime las conexiones (aristas) y pesos del Árbol de Expansión Mínima (MST).

    Parámetros:
        coloniaPadre (lista): Almacena la colonia padre para cada colonia en el MST.
        grafoDistancias (matriz 2D): La matriz de adyacencia con distancias.
        numColonias (int): El número total de colonias.
    """
    print("Conexión \tDistancia")
    for colonia in range(1, numColonias):
        print(f"{chr(coloniaPadre[colonia] + 65)} - {chr(colonia + 65)} \t{grafoDistancias[colonia][coloniaPadre[colonia]]} km")

def calcularMst(grafoDistancias, numColonias):
    """
    Calcula el Árbol de Expansión Mínima (MST) usando el Algoritmo de Prim.

    Parámetros:
        grafoDistancias (matriz 2D): La matriz de adyacencia con distancias.
        numColonias (int): El número total de colonias.
    """
    valoresLlave = [sys.maxsize] * numColonias  # Valores iniciales grandes
    coloniaPadre = [-1] * numColonias           # Almacena el MST
    incluidoEnMst = [False] * numColonias       # Controla las colonias incluidas

    valoresLlave[0] = 0                         # Empezamos desde la primera colonia

    for _ in range(numColonias - 1):
        u = encontrarLlaveMinima(valoresLlave, incluidoEnMst, numColonias)  # Encuentra la colonia no conectada más cercana
        incluidoEnMst[u] = True

        for v in range(numColonias):
            if grafoDistancias[u][v] and not incluidoEnMst[v] and grafoDistancias[u][v] < valoresLlave[v]:
                coloniaPadre[v] = u
                valoresLlave[v] = grafoDistancias[u][v]

    mostrarMst(coloniaPadre, grafoDistancias, numColonias)

def main():
    """
    Función principal para leer el archivo de entrada, construir el grafo de distancias y calcular el MST.
    """
    with open("input.txt", "r") as archivoEntrada:
        numColonias = int(archivoEntrada.readline().strip())  # Lee el número de colonias
        grafoDistancias = []

        for _ in range(numColonias):
            fila = list(map(int, archivoEntrada.readline().strip().split()))
            grafoDistancias.append(fila)

        grafoDistancias = np.array(grafoDistancias)  # Convierte la lista a un arreglo 2D

    print("Cableado óptimo de fibra óptica:")
    calcularMst(grafoDistancias, numColonias)

if __name__ == "__main__":
    main()
