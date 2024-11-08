from sys import maxsize
from itertools import permutations

#Funcion para encontrar el camino mas corto
def colonyTravel(graph, start):
    #Asignamos letras a las colonias
    """
        Para el caso actual hay 4 filas en el txt en la matriz de adyacencia
        por lo que las letras de los nodos seran de A : D
    """
    num_colonies = len(graph)
    nodes = [chr(65 + i) for i in range(num_colonies)]

    # Variables para almacenar el peso mínimo y el recorrido óptimo
    min_path = maxsize
    optimal_path = []

    # Lista de colonias excluyendo la de inicio
    """
        Como ya tenemos el punto de salida del tecnico, se excluye de la lista de colonias
        por que ya lo conocemos
    """
    vertices = [i for i in range(num_colonies) if i != start]

    # Genera todas las combinaciones posibles de las colonias
    for perm in permutations(vertices):
        """
            El viaje inicia en la colonia A, por lo que se agrega al inicio de la lista
            se toma la primera combinacion de colonias y se agrega al final de la lista
            despes se vuelve a agregar la colonia 0 para cerrar el ciclo
        """
        current_travel = 0
        current_path = [start] + list(perm) + [start]

        # Calcula el peso del camino actual le restamos 1 porque queremos empezar desde el 0
        for i in range(len(current_path) - 1):
            #Calculamos el peso del viaje
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
