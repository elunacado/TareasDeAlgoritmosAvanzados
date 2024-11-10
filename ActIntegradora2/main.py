# Programa para optimizar el cableado de fibra óptica y planificar la ruta de visitas
# Autores:
# Fecha: 
# Descripción: Este programa lee una matriz de adyacencia que representa distancias entre colonias.
# Primero calcula la ruta más corta para visitar cada colonia una vez y regresar al punto de origen.
# Luego calcula la cantidad mínima de cable necesario para conectar todas las colonias usando el Algoritmo de Prim.

from sys import maxsize
import numpy as np
from itertools import permutations
from collections import deque
import sys

# Función para encontrar el árbol de expansión mínima (Problema 1)
def encontrarLlaveMinima(valoresLlave, incluidoEnMst, numColonias):
    """
    Encuentra la colonia con el valor de llave mínimo que aún no está incluida en el MST.
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
    """
    print("\nCableado óptimo de fibra óptica:")
    print("Conexión \tDistancia")
    for colonia in range(1, numColonias):
        print(f"{chr(coloniaPadre[colonia] + 65)} - {chr(colonia + 65)} \t{grafoDistancias[colonia][coloniaPadre[colonia]]} km")

def calcularMst(grafoDistancias, numColonias):
    """
    Calcula el Árbol de Expansión Mínima (MST) usando el Algoritmo de Prim.
    """
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

# Función para calcular el camino más corto que visita cada colonia exactamente una vez (Problema 2)
def colonyTravel(graph, start):
    """
    Calcula la ruta óptima para visitar cada colonia una vez y regresar al inicio.
    """
    num_colonies = len(graph)
    nodes = [chr(65 + i) for i in range(num_colonies)]  # Nombres de las colonias (A, B, C...)

    min_path = maxsize
    optimal_path = []

    vertices = [i for i in range(num_colonies) if i != start]

    for perm in permutations(vertices):
        current_travel = 0
        current_path = [start] + list(perm) + [start]

        for i in range(len(current_path) - 1):
            current_travel += graph[current_path[i]][current_path[i + 1]]

        if current_travel < min_path:
            min_path = current_travel
            optimal_path = current_path

    optimal_path_names = [nodes[i] for i in optimal_path]

    return min_path, optimal_path_names

# BFS para encontrar un camino aumentante en el grafo de capacidad residual
def bfs(capacity, source, sink, parent):
    visited = [False] * len(capacity)
    queue = deque([source])
    visited[source] = True
    
    while queue:
        u = queue.popleft()
        
        for v, cap in enumerate(capacity[u]):
            if not visited[v] and cap > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

# Algoritmo Ford-Fulkerson para calcular el flujo máximo
def ford_fulkerson(capacity, source, sink):
    parent = [-1] * len(capacity)
    max_flow = 0
    
    while bfs(capacity, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    return max_flow

# Función principal
def main():
    """
    Función principal para ejecutar ambos problemas:
    1. Calcular la ruta óptima para visitar cada colonia exactamente una vez.
    2. Encontrar el Árbol de Expansión Mínima (MST) para cableado óptimo.
    3. Calcular el flujo máximo de información entre el nodo inicial y final.
    """
    with open("input.txt", "r") as archivoEntrada:
        numColonias = int(archivoEntrada.readline().strip())
        grafoDistancias = []

        for _ in range(numColonias):
            fila = list(map(int, archivoEntrada.readline().strip().split()))
            grafoDistancias.append(fila)

        grafoCapacidades = []
        for _ in range(numColonias):
            fila = list(map(int, archivoEntrada.readline().strip().split()))
            grafoCapacidades.append(fila)

    grafoDistancias = np.array(grafoDistancias)
    grafoCapacidades = np.array(grafoCapacidades)    
    
    # Problema 1: Calcular el MST para cableado óptimo
    calcularMst(grafoDistancias, numColonias)

    # Problema 2: Calcular la ruta óptima de visita a colonias
    start_colony = 0
    min_cost, path = colonyTravel(grafoDistancias, start_colony)
    print("\nRuta de visita a colonias:")
    print(f"Costo mínimo: {min_cost}")
    print(f"Recorrido óptimo: {' -> '.join(path)}\n")

    # Problema 3: Calcular el flujo máximo de información
    source = 0  # Nodo inicial
    sink = numColonias - 1  # Nodo final
    max_flow = ford_fulkerson(grafoCapacidades, source, sink)
    print(f"El flujo máximo de información desde el nodo inicial al nodo final es: {max_flow}")

if __name__ == "__main__":
    main()
