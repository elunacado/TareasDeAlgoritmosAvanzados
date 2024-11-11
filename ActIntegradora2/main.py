# Programa para optimizar el cableado de fibra óptica y planificar la ruta de visitas
# Autores:
# Fecha: 
# Descripción: Este programa lee una matriz de adyacencia que representa distancias entre colonias.
# Primero calcula la ruta más corta para visitar cada colonia una vez y regresar al punto de origen.
# Luego calcula la cantidad mínima de cable necesario para conectar todas las colonias usando el Algoritmo de Prim.
# Posteriormente a esto calcula el flujo máximo de información del nodo inicial al nodo final
# Y finalmente calcula la distancia más corta entre la central nueva y la más cercana que ya se tenga.

from sys import maxsize
import numpy as np
from itertools import permutations
from collections import deque
from scipy.spatial import KDTree
import math

def calcularDistancias(grafoDistancias, numColonias):
    """
    Calcula e imprime las distancias entre cada par de colonias siguiendo el algoritmo
    Floyd-Warshall.

    Parámetros:
        grafoDistancias (np.array): Matriz de adyacencia con las distancias entre colonias.
        numColonias (int): Número total de colonias.
    
    Retorno:
        np.array: Matriz de distancias actualizada con las distancias más cortas.
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
    """
    Encuentra la colonia con el valor de llave mínimo que aún no está incluida en el MST.
    
    Parámetros:
        valoresLlave (list): Lista con los valores mínimos de cada nodo.
        incluidoEnMst (list): Lista booleana que indica si el nodo está en el MST.
        numColonias (int): Número total de colonias.

    Retorno:
        int: El índice de la colonia con el valor de llave mínimo.
    """
    valorMinimo = maxsize
    indiceMinimo = -1
    
    for colonia in range(numColonias):
        if not incluidoEnMst[colonia] and valoresLlave[colonia] < valorMinimo:
            valorMinimo = valoresLlave[colonia]
            indiceMinimo = colonia
            
    return indiceMinimo

def mostrarMst(coloniaPadre, grafoDistancias, numColonias):
    """
    Imprime las conexiones y pesos del Árbol de Expansión Mínima (MST).

    Parámetros:
        coloniaPadre (list): Lista que almacena el nodo padre de cada colonia en el MST.
        grafoDistancias (np.array): Matriz de adyacencia de distancias entre colonias.
        numColonias (int): Número total de colonias.
    """
    print("\nCableado óptimo de fibra óptica:")
    print("Conexión \tDistancia")
    for colonia in range(1, numColonias):
        print(f"{chr(coloniaPadre[colonia] + 65)} - {chr(colonia + 65)} \t{grafoDistancias[colonia][coloniaPadre[colonia]]} km")

def calcularMst(grafoDistancias, numColonias):
    """
    Calcula el Árbol de Expansión Mínima (MST) usando el Algoritmo de Prim.

    Parámetros:
        grafoDistancias (np.array): Matriz de adyacencia de distancias entre colonias.
        numColonias (int): Número total de colonias.
    """
    valoresLlave = [maxsize] * numColonias
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

def calcularRutaMinima(grafo, inicio):
    """
    Calcula la ruta óptima para visitar cada colonia una vez y regresar al inicio.

    Parámetros:
        grafo (np.array): Matriz de adyacencia de distancias entre colonias.
        inicio (int): Índice de la colonia inicial.
    
    Retorno:
        tuple: (costo mínimo, lista de nombres de colonias en el recorrido óptimo).
    """
    numColonias = len(grafo)
    nodos = [chr(65 + i) for i in range(numColonias)]
    minPath = maxsize
    optimalPath = []

    vertices = [i for i in range(numColonias) if i != inicio]

    for perm in permutations(vertices):
        currentTravel = 0
        currentPath = [inicio] + list(perm) + [inicio]

        for i in range(len(currentPath) - 1):
            currentTravel += grafo[currentPath[i]][currentPath[i + 1]]

        if currentTravel < minPath:
            minPath = currentTravel
            optimalPath = currentPath

    optimalPathNames = [nodos[i] for i in optimalPath]

    return minPath, optimalPathNames

def busquedaEnAnchura(capacidad, origen, destino, padre):
    """
    Realiza una búsqueda en anchura (BFS) para encontrar un camino aumentante en el grafo de capacidad residual.

    Parámetros:
        capacidad (np.array): Matriz de capacidad residual entre colonias.
        origen (int): Nodo de origen para la búsqueda.
        destino (int): Nodo de destino para la búsqueda.
        padre (list): Lista que registra el camino encontrado.

    Retorno:
        bool: True si se encuentra un camino aumentante, False en caso contrario.
    """
    visitado = [False] * len(capacidad)
    cola = deque([origen])
    visitado[origen] = True
    
    while cola:
        nodoActual = cola.popleft()
        
        for nodoVecino, capRes in enumerate(capacidad[nodoActual]):
            if not visitado[nodoVecino] and capRes > 0:
                cola.append(nodoVecino)
                visitado[nodoVecino] = True
                padre[nodoVecino] = nodoActual
                if nodoVecino == destino:
                    return True
    return False

def fordFulkerson(capacidad, origen, destino):
    """
    Calcula el flujo máximo en un grafo usando el Algoritmo de Ford-Fulkerson.

    Parámetros:
        capacidad (np.array): Matriz de capacidades entre colonias.
        origen (int): Nodo de origen.
        destino (int): Nodo de destino.
    
    Retorno:
        int: Valor del flujo máximo entre el nodo de origen y el nodo de destino.
    """
    padre = [-1] * len(capacidad)
    flujoMaximo = 0
    
    while busquedaEnAnchura(capacidad, origen, destino, padre):
        flujoCamino = float('Inf')
        nodoActual  = destino
        while nodoActual  != origen:
            flujoCamino = min(flujoCamino, capacidad[padre[nodoActual ]][nodoActual ])
            nodoActual  = padre[nodoActual ]
        
        nodoActualizar = destino
        while nodoActualizar != origen:
            nodoAnterior = padre[nodoActualizar]
            capacidad[nodoAnterior][nodoActualizar] -= flujoCamino
            capacidad[nodoActualizar][nodoAnterior] += flujoCamino
            nodoActualizar = padre[nodoActualizar]
        
        flujoMaximo += flujoCamino
    
    return flujoMaximo

def encontrarDistanciaCorta(centrales, nuevaCentral, limite=1000):
    """
    Encuentra la central más cercana a la nueva contratación usando búsqueda lineal o KDTree.

    Parámetros:
        centrales (lista de tuplas): Coordenadas de las centrales existentes.
        nuevaCentral (tupla): Coordenadas de la nueva central.
        limite (int): Límite de centrales para elegir entre búsqueda lineal o KDTree.
    
    Retorno:
        tupla: Distancia más corta y coordenadas de la central más cercana.
    """
    if len(centrales) < limite:
        distanciaMinima = float('inf')
        centralMasCercana = None

        for central in centrales:
            distancia = math.sqrt((central[0] - nuevaCentral[0]) ** 2 + (central[1] - nuevaCentral[1]) ** 2)
            if distancia < distanciaMinima:
                distanciaMinima = distancia
                centralMasCercana = central
        
        return distanciaMinima, centralMasCercana
    
    else:
        centralesKDTree = KDTree(centrales)
        distancia, indice = centralesKDTree.query(nuevaCentral)
        centralMasCercana = centrales[indice]

        return distancia, centralMasCercana

def main():
    """
    Función principal para ejecutar todos los problemas relacionados con el cableado óptimo,
    la ruta de visita a colonias, el cálculo de flujo máximo y la distancia a la central más cercana.

    Parámetros:
        None
    
    Retorno:
        None
    """
    with open("input.txt", "r") as archivoEntrada:
        numColonias = int(archivoEntrada.readline().strip())
        
        # Lectura de la matriz de distancias
        grafoDistancias = []
        for _ in range(numColonias):
            fila = list(map(int, archivoEntrada.readline().strip().split()))
            grafoDistancias.append(fila)

        # Lectura de la matriz de capacidades
        grafoCapacidades = []
        for _ in range(numColonias):
            fila = list(map(int, archivoEntrada.readline().strip().split()))
            grafoCapacidades.append(fila)

        # Lectura de las coordenadas de las centrales
        centrales = []
        for _ in range(numColonias):
            x, y = map(int, archivoEntrada.readline().strip('()\n').split(','))
            centrales.append((x, y))

        # Lectura de la coordenada de la nueva central
        nuevaCentral = tuple(map(int, archivoEntrada.readline().strip('()\n').split(',')))

    grafoDistancias = np.array(grafoDistancias)
    grafoCapacidades = np.array(grafoCapacidades)    
    
    grafoDistancias = calcularDistancias(grafoDistancias, numColonias)
    
    # Problema 1: Calcular el Árbol de Expansión Mínima (MST) para cableado óptimo
    calcularMst(grafoDistancias, numColonias)

    # Problema 2: Calcular la ruta óptima de visita a colonias
    coloniaInicio = 0
    costoMinimo, recorrido = calcularRutaMinima(grafoDistancias, coloniaInicio)
    print("\nRuta de visita a colonias:")
    print(f"Costo mínimo: {costoMinimo}")
    print(f"Recorrido óptimo: {' -> '.join(recorrido)}\n")

    # Problema 3: Calcular el flujo máximo de información
    origen = 0  # Nodo inicial
    destino = numColonias - 1  # Nodo final
    flujoMaximo = fordFulkerson(grafoCapacidades, origen, destino)
    print(f"El flujo máximo de información desde el nodo inicial al nodo final es: {flujoMaximo}\n")

    # Problema 4: Encontrar la distancia más corta entre dos puntos
    distancia, centralMasCercana = encontrarDistanciaCorta(centrales, nuevaCentral)
    print(f"La central más cercana a {list(nuevaCentral)} es {list(centralMasCercana)} con una distancia de {distancia:.3f}.")

if __name__ == "__main__":
    main()