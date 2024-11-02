# Descripción: Este programa resuelve el problema de la mochila 
#              (Knapsack) utilizando programación dinámica.
# Autor: Mónica Martinez  [Matrícula del autor]
# Fecha de creación/modificación: [Fecha]

def knapsack(numElements, itemValues, itemWeights, maxWeight):
    """
    Calcula el beneficio máximo que se puede obtener en la mochila dada una capacidad máxima.
    
    Complejidad computacional: 
    - Espacio: O(maxWeight * numElements) debido a la matriz de programación dinámica dpMatrix.
    - Tiempo: O(maxWeight * numElements) ya que llenamos una matriz de tamaño maxWeight x numElements.
    
    Parámetros:
    - numElements (int): Número de elementos.
    - itemValues (list): Lista con los beneficios de cada elemento.
    - itemWeights (list): Lista con los pesos de cada elemento.
    - maxWeight (int): Capacidad máxima de la mochila.
    
    Retorna:
    - maxBenefit (int): Beneficio óptimo que se puede obtener.
    """
    # Crear la matriz de programación dinámica
    # Complejidad de espacio: O(maxWeight * numElements)
    dpMatrix = [[0 for _ in range(numElements + 1)] for _ in range(maxWeight + 1)]
    
    # Llenar la matriz de programación dinámica
    # Complejidad de tiempo: O(maxWeight * numElements)
    for i in range(1, numElements + 1):
        for w in range(1, maxWeight + 1):
            if itemWeights[i - 1] <= w:
                dpMatrix[w][i] = max(dpMatrix[w][i - 1], itemValues[i - 1] + dpMatrix[w - itemWeights[i - 1]][i - 1])
            else:
                dpMatrix[w][i] = dpMatrix[w][i - 1]
    
    # El beneficio óptimo está en dpMatrix[maxWeight][numElements]
    maxBenefit = dpMatrix[maxWeight][numElements]
    
    # Mostrar la matriz generada
    # Complejidad de tiempo: O(maxWeight)
    print("Matriz generada:")
    for w in range(maxWeight + 1):
        print(f"Peso {w}", dpMatrix[w])
    
    return maxBenefit

# Recibir entradas del usuario
# Complejidad de tiempo: O(numElements) para recopilar las entradas del usuario en un ciclo
numElements = int(input("Número de elementos: "))
itemValues = []
itemWeights = []

for i in range(numElements):
    value = int(input(f"Introduce el beneficio del elemento {i + 1}: "))
    weight = int(input(f"Introduce el peso del elemento {i + 1}: "))
    itemValues.append(value)
    itemWeights.append(weight)

maxWeight = int(input("Peso máximo de la mochila: "))

# Llamada a la función y salida
# Complejidad de tiempo: O(maxWeight * numElements) debido a la llamada a la función knapsack
optimalBenefit = knapsack(numElements, itemValues, itemWeights, maxWeight)
print("Beneficio óptimo:", optimalBenefit)
