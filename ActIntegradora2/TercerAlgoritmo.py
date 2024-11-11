from collections import deque
from itertools import permutations
import numpy as np

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
    with open("input.txt", "r") as archivoEntrada:
        # Leer el número de colonias
        numColonias = int(archivoEntrada.readline().strip())
        
        # Leer la matriz de capacidades de flujo
        grafoCapacidades = []
        for _ in range(numColonias):
            fila = list(map(int, archivoEntrada.readline().strip().split()))
            grafoCapacidades.append(fila)
        
        # Capacidades maximas de transmision
        grafoCapTransmision = []
        for _ in range(numColonias):
            fila = list(map(int, archivoEntrada.readline().strip().split()))
            grafoCapTransmision.append(fila)
                
        grafoCapacidades    = np.array(grafoCapacidades)
        grafoCapTransmision = np.array(grafoCapTransmision)

    for perm in permutations(np.arange(numColonias),2):
        source = perm[0]  # Nodo inicial
        sink   = perm[1]  # Nodo final
        max_flow = ford_fulkerson(grafoCapTransmision, source, sink)
        print(f"El flujo máximo de información desde el nodo inicial {source} al nodo final {sink} es: {max_flow}")
        
if __name__ == "__main__":
    main()
