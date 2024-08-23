base = 3;

def imprimirMultiplosde3(base, multiplicador = 1):
    array= []
    array.append(base*multiplicador)

    if(array[-1] == 99):
        suma = sum(array)
        promedio = suma/len(array)
        return array, suma, promedio
    else:
        subarray, suma, promedio = imprimirMultiplosde3(base, multiplicador + 1)
        array += subarray
        suma = sum(array)
        promedio = suma / len(array)
        return array, suma, promedio
    
array, suma, promedio = imprimirMultiplosde3(base)
print(array)
print("La sumatoria: ")
print(suma)
print("El promedio: ")
print(promedio)