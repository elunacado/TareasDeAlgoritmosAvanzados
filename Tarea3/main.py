howManyTypesOfCoins = int(input("Cuantas denominaciones hay? "))
coins = []
coinsInChange = []

for _ in range(howManyTypesOfCoins):
    coin_value = int(input("¿Cuál es el valor de la moneda? "))
    if coin_value > 0:  # Evitar denominaciones de monedas que sean 0
        coins.append(coin_value)
        
coins.sort(reverse=True)

P= input("Cual es el Precio del Objeto? ")
Q=input("Con cuanto pagaste? ")
change = int(Q) - int(P)

for coin in coins:
    amountOfCoins = change // coin
    coinsInChange.append(amountOfCoins)
    change -= amountOfCoins*coin

print("Se necesitan: " + str(coinsInChange))