from sys import maxsize
from itertools import permutations

#
def colonyTravel(graph, start):
    #Asignamos letras a las colonias
    num_colonies = len(graph)
    nodes = [chr(65 + i) for i in range(num_colonies)]

    # Lista de colonias excluyendo la de inicio
    vertices = [i for i in range(num_colonies) if i != start]

    # Variables para almacenar el peso mínimo y el recorrido óptimo
    min_path = maxsize
    optimal_path = []

    # Genera todas las combinaciones posibles de las colonias
    for perm in permutations(vertices):
        current_travel = 0
        current_path = [start] + list(perm) + [start]  # salimos de casa, tomamos el camino mas corto y volvemos

        # Calcula el peso del camino actual le restamos 1 porque el camino es circular
        for i in range(len(current_path) - 1):
            current_travel += graph[current_path[i]][current_path[i + 1]]

        # Si el peso del camino actual es menor que el mínimo, actualiza min_path y guarda el camino
        if current_travel < min_path:
            min_path = current_travel
            optimal_path = current_path

    # Convierte el camino óptimo a nombres de colonias
    optimal_path_names = [nodes[i] for i in optimal_path]

    return min_path, optimal_path_names

# Código principal
if __name__ == "__main__":
    # Lee el archivo input.txt
    with open('input.txt', 'r') as file:
        # Lee el número de colonias
        num_colonies = int(file.readline().strip())
        
        # Lee la matriz de adyacencia
        graph = []
        for _ in range(num_colonies):
            row = list(map(int, file.readline().strip().split()))
            graph.append(row)

    # Iniciamos en la colonia A
    start_colony = 0

    # Llama a la función para obtener el costo mínimo y el camino
    min_cost, path = colonyTravel(graph, start_colony)
    print(f"Costo mínimo: {min_cost}")
    print(f"Recorrido óptimo: {' -> '.join(path)}")
