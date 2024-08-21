import random

# Que solicite un número que indica cuántos números aleatorios (positivos y
# negativos) se mostrarán.
numOfRandom = abs(int(input("Enter the number of random numbers you wish to generate: ")))
for x in range (numOfRandom):
    print(random.randint(0,1000))

# Se desea calcular el factorial de un número dado por el usuario.
numToFactorial = int(input("Enter the number you wish to calculate their factorial: "))
def factorial(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return num * factorial(num - 1)

print("The factorial of ", numToFactorial, "is ", factorial(numToFactorial), ".")