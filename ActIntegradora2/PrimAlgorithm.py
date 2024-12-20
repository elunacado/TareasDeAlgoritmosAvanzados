# Descripción: Este programa lee una matriz de adyacencia que representa distancias entre colonias,
# muestra todas las distancias en un formato organizado y luego calcula el MST usando el Algoritmo de Prim.

import sys
import numpy as np

def calcularDistancias(grafoDistancias, numColonias):
    """
    Imprime las distancias entre cada par de colonias en un formato legible.

    Parámetros:
        grafoDistancias (matriz 2D): La matriz de adyacencia con distancias.
        numColonias (int): El número total de colonias.
    """
    print("Número de nodos:", numColonias)
    print("\nKms de colonia a colonia\n")
    
    n = grafoDistancias.shape[0]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                grafoDistancias[i][j] = min(grafoDistancias[i][j], grafoDistancias[i][k] + grafoDistancias[k][j])
    
    for i in range(n):
        for j in range(n):
            if i != j:
                print(f"{chr(i + 65)} - {chr(j + 65)} \t{grafoDistancias[i][j]} km")
        print()

    return grafoDistancias

def encontrarLlaveMinima(valoresLlave, incluidoEnMst, numColonias):
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
    print("\nCableado óptimo de fibra óptica:")
    print("Conexión \tDistancia")
    for colonia in range(1, numColonias):
        print(f"{chr(coloniaPadre[colonia] + 65)} - {chr(colonia + 65)} \t{grafoDistancias[colonia][coloniaPadre[colonia]]} km")

def calcularMst(grafoDistancias, numColonias):
    valoresLlave = [sys.maxsize] * numColonias
    coloniaPadre = [-1] * numColonias
    incluidoEnMst = [False] * numColonias

    valoresLlave[0] = 0

    for _ in range(numColonias - 1):
        u = encontrarLlaveMinima(valoresLlave, incluidoEnMst, numColonias)
        incluidoEnMst[u] = True

        for v in range(numColonias):
            if grafoDistancias[u][v] and not incluidoEnMst[v] and grafoDistancias[u][v] < valoresLlave[v]:
                coloniaPadre[v] = u
                valoresLlave[v] = grafoDistancias[u][v]

    mostrarMst(coloniaPadre, grafoDistancias, numColonias)

def main():
    """
    Función principal para leer el archivo de entrada, imprimir las distancias entre colonias y calcular el MST.
    """
    with open("input.txt", "r") as archivoEntrada:
        numColonias = int(archivoEntrada.readline().strip())
        grafoDistancias = []

        for _ in range(numColonias):
            fila = list(map(int, archivoEntrada.readline().strip().split()))
            grafoDistancias.append(fila)

    grafoDistancias = np.array(grafoDistancias)

    # Imprimir las distancias entre cada colonia
    grafoDistancias = calcularDistancias(grafoDistancias, numColonias)

    # Calcular el MST para el cableado óptimo
    calcularMst(grafoDistancias, numColonias)

if __name__ == "__main__":
    main()
