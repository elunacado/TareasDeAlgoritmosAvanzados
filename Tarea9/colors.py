#Verifica que las reglas se esten respetando
# 2 colores juntos no esta permitido
# Complejidad: O(n), donde n es el número de nodos
def es_seguro(nodo, grafo, colores, color):
    for i in range(len(grafo)):
        if grafo[nodo][i] == 1 and colores[i] == color:
            return False
    return True

# Función para colorear el grafo (grafo, número de colores, colores_temporalmente_asignados, nodo)
# Complejidad: O(c^n), donde c es el número de colores y n es el número de nodos
def colorear_grafo(grafo, num_colores, colores, nodo):
    # Si todos los nodos han sido coloreados
    # Se llama el termino de la función  
    if nodo == len(grafo):
        return True

    # Probamos todos los colores posibles
    for color in range(num_colores):
        #Si el color es valido
        if es_seguro(nodo, grafo, colores, color):
            colores[nodo] = color  # Asigna el color temporalmente

            # Coloreamos el siguiente nodo de manera recursiva
            if colorear_grafo(grafo, num_colores, colores, nodo + 1):
                return True

            # Si no se puede colorear el siguiente nodo se reestablece el default
            colores[nodo] = -1

    return False  # Retorna False si no se puede colorear el grafo

# Función principal
# Complejidad: O(n^2) debido a la entrada de la matriz de adyacencias
def main():
    n = int(input("Ingrese el número de nodos: "))

    # Leer la matriz de adyacencias
    grafo = []
    print("Ingrese la matriz de adyacencias:")
    for _ in range(n):
        fila = list(map(int, input().split()))
        grafo.append(fila)

    colores = [-1] * n  # Inicializa el vector de colores con -1 como default
    num_colores = n  # En el peor de los casos, se necesitaran la misma cantidad de nodos que de colores

    # Llama a la función de coloreado de grafo
    if colorear_grafo(grafo, num_colores, colores, 0):
        #Por cada nodo se imprime el color asignado a ese nodo
        for i in range(n):
            #Imprime el nodo y el color asignado
            print(f"Vértice: {i}, Color asignado: {colores[i]}")
    else:
        #Por alguna razon el grafo no se puede colorear
        print("No es posible asignar colores a los nodos")

main()