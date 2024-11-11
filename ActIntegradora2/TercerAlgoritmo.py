from collections import deque
from itertools import permutations
import numpy as np

""" 
BFS para encontrar un camino aumentante en el grafo de capacidad residual.
Parámetros:
- capacity: matriz que representa la capacidad residual entre colonias.
- source: nodo de origen para la búsqueda.
- sink: nodo de destino para la búsqueda.
- parent: lista que registra el camino encontrado.
Retorno: True si se encuentra un camino aumentante, False en caso contrario.
"""
def bfsFlowMax(capacity, source, sink, parent):
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

""" 
Algoritmo Ford-Fulkerson para calcular el flujo máximo.
Parámetros:
- capacity: matriz que representa la capacidad entre colonias.
- source: nodo de origen para el flujo.
- sink: nodo de destino para el flujo.
Retorno: valor del flujo máximo.
"""
def fordFulkersonFlowMax(capacity, source, sink):
    parent = [-1] * len(capacity)
    maxFlow = 0
    
    while bfsFlowMax(capacity, source, sink, parent):
        pathFlow = float('Inf')
        s = sink
        while s != source:
            pathFlow = min(pathFlow, capacity[parent[s]][s])
            s = parent[s]
        
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= pathFlow
            capacity[v][u] += pathFlow
            v = parent[v]
        
        maxFlow += pathFlow
    
    return maxFlow

""" 
Función principal para la ejecución del programa.
Lee un archivo de entrada con el número de colonias, la matriz de capacidades de flujo y la matriz de capacidades máximas de transmisión.
Calcula y muestra el flujo máximo de información para cada par de colonias.
"""
def main():
    with open("input.txt", "r") as archivoEntrada:
        # Leer el número de colonias
        numColonias = int(archivoEntrada.readline().strip())
        
        # Leer la matriz de capacidades de flujo
        grafoCapacidades = []
        for _ in range(numColonias):
            fila = list(map(int, archivoEntrada.readline().strip().split()))
            grafoCapacidades.append(fila)
        
        # Leer las capacidades máximas de transmisión
        grafoCapTransmision = []
        for _ in range(numColonias):
            fila = list(map(int, archivoEntrada.readline().strip().split()))
            grafoCapTransmision.append(fila)
                
        grafoCapacidades = np.array(grafoCapacidades)
        grafoCapTransmision = np.array(grafoCapTransmision)

    for perm in permutations(np.arange(numColonias), 2):
        source = perm[0]
        sink = perm[1] 
        maxFlow = fordFulkersonFlowMax(grafoCapTransmision, source, sink)
        print(f"El flujo máximo de información desde el nodo inicial {source} al nodo final {sink} es: {maxFlow}")

if __name__ == "__main__":
    main()
