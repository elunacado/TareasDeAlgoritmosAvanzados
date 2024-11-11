from sys import maxsize
from itertools import permutations

""" 
Función para encontrar el camino más corto entre colonias.
Parámetros:
- graph: matriz que representa las distancias entre colonias.
- start: nodo de inicio para el recorrido.
Retorno:
- minPath: costo mínimo del recorrido.
- optimalPathNames: lista con los nombres de colonias en el recorrido óptimo.
"""
def colonyTravel(graph, start):
    """
    Para el caso actual, hay 4 filas en el archivo txt en la matriz de adyacencia,
    por lo que las letras de los nodos serán de A a D.
    """
    numColonies = len(graph)
    nodes = [chr(65 + i) for i in range(numColonies)]

    # Variables para almacenar el peso mínimo y el recorrido óptimo
    minPath = maxsize
    optimalPath = []

    """
    Lista de colonias excluyendo la de inicio.
    Como ya tenemos el punto de salida del técnico, se excluye de la lista de colonias
    porque ya lo conocemos.
    """
    vertices = [i for i in range(numColonies) if i != start]

    # Genera todas las combinaciones posibles de las colonias
    for perm in permutations(vertices):
        """
        El viaje inicia en la colonia A, por lo que se agrega al inicio de la lista.
        Se toma la primera combinación de colonias y se agrega al final de la lista,
        después se vuelve a agregar la colonia 0 para cerrar el ciclo.
        """
        currentTravel = 0
        currentPath = [start] + list(perm) + [start]

        # Calcula el peso del camino actual
        for i in range(len(currentPath) - 1):
            # Calculamos el peso del viaje
            currentTravel += graph[currentPath[i]][currentPath[i + 1]]

        # Si el peso del camino actual es menor que el mínimo, actualiza minPath y guarda el camino
        if currentTravel < minPath:
            minPath = currentTravel
            optimalPath = currentPath

    # Convierte el camino óptimo a nombres de colonias
    optimalPathNames = [nodes[i] for i in optimalPath]

    return minPath, optimalPathNames

# Código principal
if __name__ == "__main__":
    # Lee el archivo input.txt
    with open("input.txt", "r") as file:
        # Lee el número de colonias
        numColonies = int(file.readline().strip())
        
        # Lee la matriz de adyacencia
        graph = []
        for _ in range(numColonies):
            row = list(map(int, file.readline().strip().split()))
            graph.append(row)

    # Iniciamos en la colonia A
    startColony = 0

    # Llama a la función para obtener el costo mínimo y el camino
    minCost, path = colonyTravel(graph, startColony)
    print(f"Costo mínimo: {minCost}")
    print(f"Recorrido óptimo: {' -> '.join(path)}")
